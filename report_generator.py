import os
from datetime import datetime
import json

class ReportGenerator:
    """Generates comprehensive management reports"""
    
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def generate_executive_summary(self, insights):
        """Generate executive summary report"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        report = f"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                    🏨 HOTEL OCCUPANCY ANALYSIS REPORT                          ║
║                          EXECUTIVE SUMMARY                                     ║
╚════════════════════════════════════════════════════════════════════════════════╝

Generated: {timestamp}

{'─' * 80}
1. OCCUPANCY PERFORMANCE
{'─' * 80}
"""
        
        if 'occupancy_trends' in insights:
            occ = insights['occupancy_trends']
            report += f"""
  • Average Occupancy Rate: {occ['average_rate']}%
  • Maximum Rate: {occ['max_rate']}%
  • Minimum Rate: {occ['min_rate']}%
  • Trend: {occ['trend']}

  Analysis: 
    - If occupancy < 70%, immediate action needed to increase bookings
    - If occupancy 70-85%, good performance with room for improvement
    - If occupancy > 85%, excellent performance
"""
        
        report += f"""
{'─' * 80}
2. ROOM TYPE PERFORMANCE
{'─' * 80}
"""
        
        if 'room_performance' in insights:
            for room in insights['room_performance']:
                status = "✅ Excellent" if room['occupancy_rate'] > 80 else "⚠️  Needs Improvement" if room['occupancy_rate'] < 70 else "✓ Good"
                report += f"""
  {room['room_type']}:
    - Occupancy Rate: {room['occupancy_rate']}% {status}
    - Bookings: {room['completed_bookings']}/{room['total_bookings']}
"""
        
        report += f"""
{'─' * 80}
3. CANCELLATION ANALYSIS
{'─' * 80}
"""
        
        if 'cancellations' in insights:
            cancel_rate = insights['cancellations']['rate']
            status = "🔴 CRITICAL" if cancel_rate > 25 else "🟠 HIGH" if cancel_rate > 15 else "🟢 HEALTHY"
            report += f"""
  Cancellation Rate: {cancel_rate}% {status}
  
  Recommendations:
    - Review cancellation policies
    - Implement deposit requirements
    - Send confirmation reminders
    - Improve customer communication
"""
        
        report += f"""
{'─' * 80}
4. REVENUE INSIGHTS
{'─' * 80}
"""
        
        if 'revenue' in insights:
            rev = insights['revenue']
            report += f"""
  • Total Revenue: ${rev['total']:,.2f}
  • Average Daily Revenue: ${rev['avg_daily']:,.2f}
  • Top Performing Room Type: {rev['top_performer']}
"""
        
        report += f"""
{'─' * 80}
5. SEASONAL PATTERNS
{'─' * 80}
"""
        
        if 'seasons' in insights:
            peak = insights['seasons']['peak']
            low = insights['seasons']['low']
            report += f"""
  Peak Season: {peak['month']}
    - Revenue: ${peak['revenue']:,.2f}
    - Bookings: {peak['bookings']}
    - Avg Price: ${peak['avg_price']:.2f}
  
  Low Season: {low['month']}
    - Revenue: ${low['revenue']:,.2f}
    - Bookings: {low['bookings']}
    - Avg Price: ${low['avg_price']:.2f}
  
  Opportunity Gap: ${peak['revenue'] - low['revenue']:,.2f} per month
"""
        
        report += f"""
{'─' * 80}
6. KEY RECOMMENDATIONS
{'─' * 80}
"""
        
        if 'recommendations' in insights:
            for i, rec in enumerate(insights['recommendations'], 1):
                priority_symbol = "🔴" if rec['priority'] == 'HIGH' else "🟠" if rec['priority'] == 'MEDIUM' else "🟢"
                report += f"""
  {i}. [{priority_symbol} {rec['priority']}] {rec['category']}
     {rec['recommendation']}
"""
        
        report += f"""
{'─' * 80}
7. ACTION ITEMS
{'─' * 80}

  SHORT TERM (1-2 weeks):
    ✓ Implement dynamic pricing for low occupancy periods
    ✓ Review and update room rates based on demand
    ✓ Launch promotional campaigns
  
  MEDIUM TERM (1-3 months):
    ✓ Improve room amenities based on guest feedback
    ✓ Enhance marketing channels
    ✓ Optimize cancellation policies
  
  LONG TERM (3-12 months):
    ✓ Consider property renovations
    ✓ Develop loyalty programs
    ✓ Expand room offerings
    ✓ Implement AI-based pricing strategies

{'─' * 80}
End of Report
{'═' * 80}
"""
        
        return report
    
    def save_report(self, content, filename="occupancy_report.txt"):
        """Save report to file"""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✅ Report saved: {filepath}")
        return filepath
    
    def save_json_report(self, insights, filename="analysis_insights.json"):
        """Save insights as JSON for further processing"""
        filepath = os.path.join(self.output_dir, filename)
        
        # Convert non-serializable objects
        clean_insights = {}
        for key, value in insights.items():
            if key == 'data':
                continue  # Skip DataFrame objects
            elif isinstance(value, dict):
                if 'data' in value and hasattr(value['data'], 'to_dict'):
                    value = value.copy()
                    value['data'] = value['data'].to_dict(orient='records')
                clean_insights[key] = value
            elif hasattr(value, 'to_dict'):
                clean_insights[key] = value.to_dict(orient='records')
            else:
                clean_insights[key] = value
        
        with open(filepath, 'w') as f:
            json.dump(clean_insights, f, indent=2)
        print(f"✅ JSON insights saved: {filepath}")
        return filepath
