import zipfile
import os
import sqlite3
import json
from pathlib import Path

def extract_database():
    """Extract hotels.db from hotel.zip and place it in the root folder"""
    
    zip_file_path = "hotel.zip"
    root_folder = "."
    
    if not os.path.exists(zip_file_path):
        print(f"❌ Error: {zip_file_path} not found in the current directory")
        print(f"   Please ensure hotel.zip is in the root folder")
        return False
    
    try:
        print(f"📦 Extracting {zip_file_path}...")
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(root_folder)
        
        # Check if hotels.db was extracted
        if os.path.exists("hotels.db"):
            print("✅ Successfully extracted hotels.db to root folder")
            return True
        else:
            print("⚠️  Warning: hotels.db not found after extraction")
            # List extracted files
            extracted_files = [f for f in os.listdir(root_folder) if os.path.isfile(f)]
            print("📄 Extracted files:", extracted_files)
            return False
            
    except Exception as e:
        print(f"❌ Error extracting file: {e}")
        return False


def analyze_database_schema():
    """Analyze the database schema and return table/column information"""
    
    if not os.path.exists("hotels.db"):
        print("❌ Error: hotels.db not found")
        return None
    
    try:
        conn = sqlite3.connect("hotels.db")
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        schema_info = {}
        
        for table in tables:
            table_name = table[0]
            
            # Get columns for this table
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            
            # Get row count
            cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
            row_count = cursor.fetchone()[0]
            
            schema_info[table_name] = {
                "row_count": row_count,
                "columns": []
            }
            
            for col in columns:
                schema_info[table_name]["columns"].append({
                    "name": col[1],
                    "type": col[2],
                    "not_null": col[3],
                    "default": col[4],
                    "pk": col[5]
                })
        
        conn.close()
        return schema_info
        
    except Exception as e:
        print(f"❌ Error analyzing database: {e}")
        return None


def print_schema_summary(schema_info):
    """Print a readable summary of the database schema"""
    
    if not schema_info:
        return
    
    print("\n" + "="*80)
    print("🏨 DATABASE SCHEMA SUMMARY".center(80))
    print("="*80)
    
    total_tables = len(schema_info)
    total_rows = sum(table['row_count'] for table in schema_info.values())
    
    print(f"\n📊 Total Tables: {total_tables}")
    print(f"📈 Total Records: {total_rows:,}\n")
    
    for table_name, table_data in schema_info.items():
        print(f"\n📋 Table: {table_name}")
        print(f"   └─ Rows: {table_data['row_count']:,}")
        print(f"   └─ Columns: {len(table_data['columns'])}")
        print(f"   └─ Fields:")
        for col in table_data['columns']:
            pk_marker = " [PRIMARY KEY]" if col['pk'] else ""
            nn_marker = " [NOT NULL]" if col['not_null'] else ""
            print(f"      • {col['name']}: {col['type']}{pk_marker}{nn_marker}")
    
    print("\n" + "="*80 + "\n")


def save_schema_to_file(schema_info):
    """Save schema information to a JSON file for reference"""
    
    if not schema_info:
        return
    
    try:
        with open("database_schema.json", "w") as f:
            json.dump(schema_info, f, indent=2)
        print("✅ Database schema saved to database_schema.json")
    except Exception as e:
        print(f"❌ Error saving schema: {e}")


def setup_directories():
    """Create necessary project directories"""
    
    directories = [
        "data",
        "analysis",
        "visualizations",
        "reports",
        "logs"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    print("✅ Project directories created")


if __name__ == "__main__":
    print("\n" + "="*80)
    print("🚀 HOTEL OCCUPANCY ANALYSIS - SETUP & DATABASE EXTRACTION".center(80))
    print("="*80 + "\n")
    
    # Step 1: Setup directories
    print("📁 Setting up project directories...")
    setup_directories()
    
    # Step 2: Extract the database
    print("\n🔓 Extracting database...")
    if extract_database():
        # Step 3: Analyze the schema
        print("\n🔍 Analyzing database schema...")
        schema_info = analyze_database_schema()
        
        if schema_info:
            # Step 4: Print summary
            print_schema_summary(schema_info)
            
            # Step 5: Save schema to file
            save_schema_to_file(schema_info)
            
            print("\n✅ Database extraction and analysis complete!")
            print("   You can now run: python main.py\n")
        else:
            print("❌ Failed to analyze database")
    else:
        print("❌ Failed to extract database")
        print("   Please ensure hotel.zip is in the root folder")