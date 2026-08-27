import pandas as pd
import numpy as np
from database_manager import DatabaseManager
from datetime import datetime, timedelta

class OccupancyAnalyzer:
    """Analyzes hotel occupancy data and generates insights"""
    
    def __init__(self, db_manager):
        self.db = db_manager
        self.insights = {}
    
    def analyze_occupancy_trends(self):
        """Analyze occupancy trends over time"""
        print("\n📊 Analyzing occupancy trends...")
        
        occupancy_data = self.db.get_occupancy_by_date()
        if occupancy_data is None or occupancy_data.empty:
            print("❌ No occupancy data available")
            return None
        
        occupancy_data['date'] = pd.to_datetime(occupancy_data['date'])
        
        # Calculate trends
        avg_occupancy = occupancy_data['occupancy_rate'].mean()
        max_occupancy = occupancy_data['occupancy_rate'].max()
        min_occupancy = occupancy_data['occupancy_rate'].min()
        trend = "📈 Increasing" if occupancy_data['occupancy_rate'].iloc[-1] > occupancy_data['occupancy_rate'].iloc[0] else "📉 Decreasing"
        
        self.insights['occupancy_trends'] = {
            'average_rate': round(avg_occupancy, 2),
            'max_rate': round(max_occupancy, 2),
            'min_rate': round(min_occupancy, 2),
            'trend': trend,
            'data': occupancy_data
        }
        
        print(f"✅ Average Occupancy Rate: {avg_occupancy:.2f}%")
        print(f"   Max Rate: {max_occupancy:.2f}% | Min Rate: {min_occupancy:.2f}%")
        print(f"   Trend: {trend}")
        
        return occupancy_data
    
    def analyze_room_type_performance(self):
        """Analyze performance by room type"""
        print("\n🛏️  Analyzing room type performance...")
        
        room_data = self.db.get_occupancy_by_room_type()
        if room_data is None or room_data.empty:
            print("❌ No room type data available")
            return None
        
        self.insights['room_performance'] = room_data.to_dict(orient='records')
        
        print("✅ Room Type Performance:")
        for idx, row in room_data.iterrows():
            print(f"   • {row['room_type']}: {row['occupancy_rate']}% occupancy ({row['completed_bookings']}/{row['total_bookings']} bookings)")
        
        return room_data
    
    def analyze_cancellations(self):
        """Analyze cancellation patterns"""
        print("\n❌ Analyzing cancellation patterns...")
        
        cancel_data = self.db.get_cancellation_analysis()
        if cancel_data is None or cancel_data.empty:
            print("❌ No cancellation data available")
            return None
        
        cancellation_rate = cancel_data[cancel_data['status'] == 'Cancelled']['percentage'].values
        if len(cancellation_rate) > 0:
            cancellation_rate = cancellation_rate[0]
        else:
            cancellation_rate = 0
        
        self.insights['cancellations'] = {
            'rate': cancellation_rate,
            'data': cancel_data.to_dict(orient='records')
        }
        
        print(f"✅ Cancellation Rate: {cancellation_rate:.2f}%")
        print("   Status Breakdown:")
        for idx, row in cancel_data.iterrows():
            print(f"   • {row['status']}: {row['percentage']}%")
        
        return cancel_data
    
    def analyze_revenue(self):
        """Analyze revenue patterns"""
        print("\n💰 Analyzing revenue patterns...")
        
        revenue_data = self.db.get_revenue_analysis()
        if revenue_data is None or revenue_data.empty:
            print("❌ No revenue data available")
            return None
        
        total_revenue = revenue_data['total_revenue'].sum()
        avg_daily_revenue = revenue_data.groupby('date')['total_revenue'].sum().mean()
        top_room_type = revenue_data.groupby('room_type')['total_revenue'].sum().idxmax()
        
        self.insights['revenue'] = {
            'total': round(total_revenue, 2),
            'avg_daily': round(avg_daily_revenue, 2),
            'top_performer': top_room_type
        }
        
        print(f"✅ Total Revenue: ${total_revenue:.2f}")
        print(f"   Average Daily Revenue: ${avg_daily_revenue:.2f}")
        print(f"   Top Performing Room Type: {top_room_type}")
        
        return revenue_data
    
    def analyze_peak_seasons(self):
        """Identify peak and low seasons"""
        print("\n🎯 Identifying peak seasons...")
        
        season_data = self.db.get_peak_seasons()
        if season_data is None or season_data.empty:
            print("❌ No seasonal data available")
            return None
        
        peak_month = season_data.iloc[0]
        low_month = season_data.iloc[-1]
        
        self.insights['seasons'] = {
            'peak': peak_month.to_dict(),
            'low': low_month.to_dict()
        }
        
        print(f"✅ Peak Season: {peak_month['month']} (${peak_month['revenue']:.2f} revenue)")
        print(f"   Low Season: {low_month['month']} (${low_month['revenue']:.2f} revenue)")
        
        return season_data
    
    def generate_recommendations(self):
        """Generate actionable recommendations based on analysis"""
        print("\n💡 Generating recommendations...")
        
        recommendations = []
        
        # Check occupancy rate
        if 'occupancy_trends' in self.insights:
            avg_occ = self.insights['occupancy_trends']['average_rate']
            if avg_occ < 70:
                recommendations.append({
                    'priority': 'HIGH',
                    'category': 'Occupancy',
                    'recommendation': f'Occupancy rate is {avg_occ}%. Implement dynamic pricing or promotional campaigns to increase bookings.'
                })
            elif avg_occ < 85:
                recommendations.append({
                    'priority': 'MEDIUM',
                    'category': 'Occupancy',
                    'recommendation': f'Occupancy rate is {avg_occ}%. Consider targeted marketing to specific guest segments.'
                })
        
        # Check cancellation rate
        if 'cancellations' in self.insights:
            cancel_rate = self.insights['cancellations']['rate']
            if cancel_rate > 20:
                recommendations.append({
                    'priority': 'HIGH',
                    'category': 'Cancellations',
                    'recommendation': f'High cancellation rate ({cancel_rate}%). Review cancellation policies and improve customer communication.'
                })
        
        # Check room performance
        if 'room_performance' in self.insights:
            room_data = self.insights['room_performance']
            low_performers = [r for r in room_data if r['occupancy_rate'] < 50]
            if low_performers:
                types = ', '.join([r['room_type'] for r in low_performers])
                recommendations.append({
                    'priority': 'HIGH',
                    'category': 'Room Performance',
                    'recommendation': f'Room types {types} have low occupancy. Consider renovations or pricing adjustments.'
                })
        
        self.insights['recommendations'] = recommendations
        
        print(f"✅ Generated {len(recommendations)} recommendations:")
        for rec in recommendations:
            print(f"   [{rec['priority']}] {rec['category']}: {rec['recommendation']}")
        
        return recommendations
    
    def get_all_insights(self):
        """Get all analyzed insights"""
        return self.insights
