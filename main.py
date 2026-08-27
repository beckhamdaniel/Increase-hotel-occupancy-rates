#!/usr/bin/env python3
"""
Hotel Occupancy Rate Analysis System
Main application to extract database, analyze data, generate visualizations, and produce reports
"""

import os
import sys
from extract_and_setup import extract_database, analyze_database_schema, print_schema_summary, save_schema_to_file, setup_directories
from database_manager import DatabaseManager
from occupancy_analyzer import OccupancyAnalyzer
from visualization_generator import VisualizationGenerator
from report_generator import ReportGenerator
from datetime import datetime

def print_banner():
    """Print welcome banner"""
    print("""
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║              🏨 HOTEL OCCUPANCY RATE IMPROVEMENT SYSTEM 🏨                    ║
║                                                                                ║
║                    Comprehensive Analysis & Recommendations                   ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
    """)

def main():
    """Main application flow"""
    print_banner()
    
    # Step 1: Setup and Extract
    print("\n" + "="*80)
    print("STEP 1: DATABASE EXTRACTION & SETUP".center(80))
    print("="*80)
    
    setup_directories()
    
    if not extract_database():
        print("\n❌ Failed to extract database. Please ensure hotel.zip is in the root folder.")
        sys.exit(1)
    
    # Step 2: Analyze Schema
    print("\n" + "="*80)
    print("STEP 2: DATABASE SCHEMA ANALYSIS".center(80))
    print("="*80)
    
    schema_info = analyze_database_schema()
    if not schema_info:
        print("\n❌ Failed to analyze database schema.")
        sys.exit(1)
    
    print_schema_summary(schema_info)
    save_schema_to_file(schema_info)
    
    # Step 3: Connect and Analyze Data
    print("\n" + "="*80)
    print("STEP 3: OCCUPANCY DATA ANALYSIS".center(80))
    print("="*80)
    
    db_manager = DatabaseManager()
    if not db_manager.connect():
        print("\n❌ Failed to connect to database.")
        sys.exit(1)
    
    # Run occupancy analysis
    analyzer = OccupancyAnalyzer(db_manager)
    
    print("\n🔍 Running comprehensive analysis...\n")
    analyzer.analyze_occupancy_trends()
    analyzer.analyze_room_type_performance()
    analyzer.analyze_cancellations()
    analyzer.analyze_revenue()
    analyzer.analyze_peak_seasons()
    analyzer.generate_recommendations()
    
    insights = analyzer.get_all_insights()
    
    # Step 4: Generate Visualizations
    print("\n" + "="*80)
    print("STEP 4: GENERATING VISUALIZATIONS".center(80))
    print("="*80)
    
    viz_gen = VisualizationGenerator()
    
    print("\n📊 Creating visualizations...\n")
    
    if 'occupancy_trends' in insights and 'data' in insights['occupancy_trends']:
        viz_gen.plot_occupancy_trend(insights['occupancy_trends']['data'])
    
    if 'room_performance' in insights:
        room_df = insights['occupancy_trends']['data'].copy() if 'occupancy_trends' in insights and 'data' in insights['occupancy_trends'] else None
        if room_df is not None:
            # Get room performance data properly
            db_manager2 = DatabaseManager()
            db_manager2.connect()
            room_perf = db_manager2.get_occupancy_by_room_type()
            if room_perf is not None:
                viz_gen.plot_room_type_performance(room_perf)
            db_manager2.disconnect()
    
    cancel_data = db_manager.get_cancellation_analysis()
    if cancel_data is not None:
        viz_gen.plot_cancellation_analysis(cancel_data)
    
    revenue_data = db_manager.get_revenue_analysis()
    if revenue_data is not None:
        viz_gen.plot_revenue_analysis(revenue_data)
    
    season_data = db_manager.get_peak_seasons()
    if season_data is not None:
        viz_gen.plot_seasonal_trends(season_data)
    
    if 'recommendations' in insights:
        viz_gen.plot_recommendations_summary(insights['recommendations'])
    
    # Step 5: Generate Reports
    print("\n" + "="*80)
    print("STEP 5: GENERATING MANAGEMENT REPORTS".center(80))
    print("="*80)
    
    report_gen = ReportGenerator()
    
    print("\n📝 Creating reports...\n")
    
    # Generate executive summary
    exec_summary = report_gen.generate_executive_summary(insights)
    report_gen.save_report(exec_summary, "occupancy_analysis_report.txt")
    
    # Save JSON insights
    report_gen.save_json_report(insights)
    
    db_manager.disconnect()
    
    # Step 6: Summary
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE".center(80))
    print("="*80)
    
    print("""
✅ All tasks completed successfully!

📁 Generated Files:
   └ visualizations/     - All charts and graphs for management
   └ reports/           - Executive summary and JSON insights
   └ database_schema.json - Database structure reference

📊 Key Visualizations Generated:
   1. Occupancy Trend Over Time
   2. Room Type Performance
   3. Cancellation Analysis
   4. Revenue Analysis
   5. Seasonal Trends
   6. Recommendations Summary

📋 Reports Generated:
   └ occupancy_analysis_report.txt - Executive summary for management
   └ analysis_insights.json - Detailed insights in JSON format

🎯 Next Steps:
   1. Review visualizations in the visualizations/ folder
   2. Share occupancy_analysis_report.txt with management team
   3. Present charts for data-driven decision making
   4. Implement recommendations from the report
   5. Re-run analysis monthly to track improvements

💡 Pro Tips:
   • Schedule monthly analysis runs to track progress
   • Use visualizations in management presentations
   • Monitor KPIs from the reports
   • Adjust strategies based on seasonal patterns
   • Track ROI on implemented recommendations
    """)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
