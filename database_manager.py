import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import os

class DatabaseManager:
    """Manages all database connections and queries"""
    
    def __init__(self, db_path="hotels.db"):
        self.db_path = db_path
        self.conn = None
        
    def connect(self):
        """Connect to the database"""
        try:
            self.conn = sqlite3.connect(self.db_path)
            print(f"✅ Connected to {self.db_path}")
            return True
        except Exception as e:
            print(f"❌ Error connecting to database: {e}")
            return False
    
    def disconnect(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
            print("✅ Database connection closed")
    
    def get_tables(self):
        """Get list of all tables"""
        if not self.conn:
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [table[0] for table in cursor.fetchall()]
            return tables
        except Exception as e:
            print(f"❌ Error getting tables: {e}")
            return None
    
    def execute_query(self, query):
        """Execute a custom query and return results"""
        if not self.conn:
            print("❌ Not connected to database")
            return None
        try:
            return pd.read_sql_query(query, self.conn)
        except Exception as e:
            print(f"❌ Error executing query: {e}")
            return None
    
    def get_occupancy_by_date(self):
        """Get occupancy rates by date"""
        query = """
        SELECT 
            DATE(check_in_date) as date,
            COUNT(*) as total_bookings,
            SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) as completed_bookings,
            ROUND(CAST(SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) as FLOAT) / COUNT(*) * 100, 2) as occupancy_rate
        FROM bookings
        GROUP BY DATE(check_in_date)
        ORDER BY date
        """
        return self.execute_query(query)
    
    def get_occupancy_by_room_type(self):
        """Get occupancy rates by room type"""
        query = """
        SELECT 
            r.room_type,
            COUNT(b.booking_id) as total_bookings,
            SUM(CASE WHEN b.status = 'Completed' THEN 1 ELSE 0 END) as completed_bookings,
            ROUND(CAST(SUM(CASE WHEN b.status = 'Completed' THEN 1 ELSE 0 END) as FLOAT) / COUNT(b.booking_id) * 100, 2) as occupancy_rate
        FROM rooms r
        LEFT JOIN bookings b ON r.room_id = b.room_id
        GROUP BY r.room_type
        ORDER BY occupancy_rate DESC
        """
        return self.execute_query(query)
    
    def get_cancellation_analysis(self):
        """Analyze cancellation patterns"""
        query = """
        SELECT 
            status,
            COUNT(*) as count,
            ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) as percentage
        FROM bookings
        GROUP BY status
        ORDER BY count DESC
        """
        return self.execute_query(query)
    
    def get_revenue_analysis(self):
        """Get revenue analysis by room type and period"""
        query = """
        SELECT 
            DATE(b.check_in_date) as date,
            r.room_type,
            COUNT(b.booking_id) as bookings,
            ROUND(SUM(b.price), 2) as total_revenue,
            ROUND(AVG(b.price), 2) as avg_price_per_booking
        FROM bookings b
        LEFT JOIN rooms r ON b.room_id = r.room_id
        WHERE b.status = 'Completed'
        GROUP BY DATE(b.check_in_date), r.room_type
        ORDER BY date DESC, total_revenue DESC
        """
        return self.execute_query(query)
    
    def get_guest_demographics(self):
        """Get guest demographic information"""
        query = """
        SELECT 
            COUNT(DISTINCT g.guest_id) as unique_guests,
            COUNT(b.booking_id) as total_bookings,
            ROUND(AVG(b.price), 2) as avg_spending,
            ROUND(SUM(b.price), 2) as total_revenue
        FROM guests g
        LEFT JOIN bookings b ON g.guest_id = b.guest_id
        """
        return self.execute_query(query)
    
    def get_peak_seasons(self):
        """Identify peak and low seasons"""
        query = """
        SELECT 
            strftime('%Y-%m', check_in_date) as month,
            COUNT(*) as bookings,
            ROUND(SUM(price), 2) as revenue,
            ROUND(AVG(price), 2) as avg_price
        FROM bookings
        WHERE status = 'Completed'
        GROUP BY strftime('%Y-%m', check_in_date)
        ORDER BY revenue DESC
        """
        return self.execute_query(query)
    
    def get_repeat_guests(self):
        """Get repeat guest analysis"""
        query = """
        SELECT 
            COUNT(DISTINCT guest_id) as repeat_guests,
            COUNT(booking_id) as total_repeat_bookings,
            ROUND(SUM(price), 2) as revenue_from_repeats,
            ROUND(COUNT(booking_id) * 100.0 / (SELECT COUNT(*) FROM bookings), 2) as repeat_percentage
        FROM (
            SELECT guest_id, booking_id, price
            FROM bookings
            WHERE status = 'Completed'
            GROUP BY guest_id
            HAVING COUNT(*) > 1
        )
        """
        return self.execute_query(query)
    
    def get_room_utilization(self):
        """Get room utilization rates"""
        query = """
        SELECT 
            r.room_id,
            r.room_type,
            r.price_per_night,
            COUNT(b.booking_id) as total_bookings,
            SUM(CASE WHEN b.status = 'Completed' THEN 1 ELSE 0 END) as completed_bookings,
            ROUND(CAST(SUM(CASE WHEN b.status = 'Completed' THEN 1 ELSE 0 END) as FLOAT) / COUNT(b.booking_id) * 100, 2) as utilization_rate
        FROM rooms r
        LEFT JOIN bookings b ON r.room_id = b.room_id
        GROUP BY r.room_id
        ORDER BY utilization_rate DESC
        """
        return self.execute_query(query)
