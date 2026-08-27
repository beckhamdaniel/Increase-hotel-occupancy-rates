import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from datetime import datetime

class VisualizationGenerator:
    """Generates visualizations for hotel occupancy analysis"""
    
    def __init__(self, output_dir="visualizations"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (14, 6)
    
    def plot_occupancy_trend(self, data):
        """Plot occupancy rate trends over time"""
        if data is None or data.empty:
            print("❌ No data to plot")
            return
        
        plt.figure(figsize=(14, 6))
        plt.plot(data['date'], data['occupancy_rate'], marker='o', linewidth=2, markersize=4, color='#2E86AB')
        
        # Add average line
        avg_occupancy = data['occupancy_rate'].mean()
        plt.axhline(y=avg_occupancy, color='red', linestyle='--', linewidth=2, label=f'Average: {avg_occupancy:.2f}%')
        
        plt.title('Hotel Occupancy Rate Trend Over Time', fontsize=16, fontweight='bold')
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Occupancy Rate (%)', fontsize=12)
        plt.ylim(0, 105)
        plt.legend(fontsize=10)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, '01_occupancy_trend.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {filepath}")
        plt.close()
    
    def plot_room_type_performance(self, data):
        """Plot occupancy by room type"""
        if data is None or data.empty:
            print("❌ No room data to plot")
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Occupancy rate by room type
        colors = ['#06A77D' if x >= 70 else '#D62828' for x in data['occupancy_rate']]
        ax1.bar(data['room_type'], data['occupancy_rate'], color=colors, edgecolor='black', linewidth=1.5)
        ax1.axhline(y=70, color='green', linestyle='--', linewidth=2, alpha=0.7, label='Target: 70%')
        ax1.set_title('Occupancy Rate by Room Type', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Occupancy Rate (%)', fontsize=11)
        ax1.set_ylim(0, 105)
        ax1.legend()
        ax1.tick_params(axis='x', rotation=45)
        
        # Booking volume by room type
        ax2.bar(data['room_type'], data['total_bookings'], color='#2E86AB', edgecolor='black', linewidth=1.5)
        ax2.set_title('Total Bookings by Room Type', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Number of Bookings', fontsize=11)
        ax2.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, '02_room_type_performance.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {filepath}")
        plt.close()
    
    def plot_cancellation_analysis(self, data):
        """Plot cancellation statistics"""
        if data is None or data.empty:
            print("❌ No cancellation data to plot")
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Pie chart
        colors = ['#06A77D', '#D62828', '#F77F00']
        ax1.pie(data['count'], labels=data['status'], autopct='%1.1f%%', colors=colors, startangle=90)
        ax1.set_title('Booking Status Distribution', fontsize=14, fontweight='bold')
        
        # Bar chart
        ax2.bar(data['status'], data['count'], color=colors, edgecolor='black', linewidth=1.5)
        ax2.set_title('Booking Count by Status', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Number of Bookings', fontsize=11)
        ax2.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, '03_cancellation_analysis.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {filepath}")
        plt.close()
    
    def plot_revenue_analysis(self, data):
        """Plot revenue by room type"""
        if data is None or data.empty:
            print("❌ No revenue data to plot")
            return
        
        revenue_by_type = data.groupby('room_type')['total_revenue'].sum().sort_values(ascending=False)
        
        plt.figure(figsize=(14, 6))
        bars = plt.bar(revenue_by_type.index, revenue_by_type.values, color='#2E86AB', edgecolor='black', linewidth=1.5)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height:,.0f}',
                    ha='center', va='bottom', fontsize=10)
        
        plt.title('Total Revenue by Room Type', fontsize=16, fontweight='bold')
        plt.xlabel('Room Type', fontsize=12)
        plt.ylabel('Revenue ($)', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, '04_revenue_analysis.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {filepath}")
        plt.close()
    
    def plot_seasonal_trends(self, data):
        """Plot seasonal booking and revenue trends"""
        if data is None or data.empty:
            print("❌ No seasonal data to plot")
            return
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Revenue by month
        ax1.plot(data['month'], data['revenue'], marker='o', linewidth=2, markersize=8, color='#06A77D')
        ax1.fill_between(range(len(data)), data['revenue'].values, alpha=0.3, color='#06A77D')
        ax1.set_title('Revenue by Month', fontsize=14, fontweight='bold')
        ax1.set_ylabel('Revenue ($)', fontsize=11)
        ax1.tick_params(axis='x', rotation=45)
        
        # Bookings by month
        ax2.bar(data['month'], data['bookings'], color='#2E86AB', edgecolor='black', linewidth=1.5)
        ax2.set_title('Bookings by Month', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Number of Bookings', fontsize=11)
        ax2.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        filepath = os.path.join(self.output_dir, '05_seasonal_trends.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {filepath}")
        plt.close()
    
    def plot_recommendations_summary(self, recommendations):
        """Create a visual summary of recommendations"""
        if not recommendations:
            print("⚠️  No recommendations to visualize")
            return
        
        # Count by priority
        priorities = {}
        for rec in recommendations:
            priority = rec.get('priority', 'MEDIUM')
            priorities[priority] = priorities.get(priority, 0) + 1
        
        plt.figure(figsize=(12, 6))
        colors_map = {'HIGH': '#D62828', 'MEDIUM': '#F77F00', 'LOW': '#06A77D'}
        colors = [colors_map.get(p, '#999999') for p in priorities.keys()]
        
        bars = plt.barh(list(priorities.keys()), list(priorities.values()), color=colors, edgecolor='black', linewidth=1.5)
        
        # Add value labels
        for bar in bars:
            width = bar.get_width()
            plt.text(width, bar.get_y() + bar.get_height()/2.,
                    f'{int(width)} recommendations',
                    ha='left', va='center', fontsize=11, fontweight='bold')
        
        plt.title('Recommendations by Priority', fontsize=16, fontweight='bold')
        plt.xlabel('Count', fontsize=12)
        plt.xlim(0, max(priorities.values()) * 1.2)
        plt.tight_layout()
        
        filepath = os.path.join(self.output_dir, '06_recommendations_summary.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {filepath}")
        plt.close()
