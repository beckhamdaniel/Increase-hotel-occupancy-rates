# 🏨 Hotel Occupancy Rate Improvement System

A comprehensive Python-based analysis system designed to increase hotel room occupancy rates through data-driven insights and actionable recommendations.

## 📋 Features

- **Automated Database Extraction** - Extracts and analyzes hotel.db from ZIP archive
- **Occupancy Analysis** - Comprehensive analysis of booking patterns and occupancy trends
- **Performance Metrics** - Track occupancy by room type, time period, and seasonal patterns
- **Cancellation Analysis** - Identify and analyze booking cancellation patterns
- **Revenue Insights** - Detailed revenue analysis by room type and time period
- **Dynamic Visualizations** - Professional charts and graphs for management presentations
- **Executive Reports** - Detailed reports with actionable recommendations
- **Automated Recommendations** - AI-powered suggestions to improve occupancy rates

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager
- hotel.zip file in the project root directory

### Installation

1. **Clone or download the project**
   ```bash
   cd Increase-hotel-occupancy-rates
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure hotel.zip is in the root folder**
   ```bash
   ls -la hotel.zip
   ```

### Running the Analysis

```bash
python main.py
```

The system will:
1. Extract `hotels.db` from `hotel.zip`
2. Analyze the database schema
3. Run comprehensive occupancy analysis
4. Generate visualizations (charts and graphs)
5. Create management reports
6. Produce actionable recommendations

## 📁 Project Structure

```
Increase-hotel-occupancy-rates/
├── main.py                      # Main application entry point
├── extract_and_setup.py         # Database extraction and setup
├── database_manager.py          # Database connection and queries
├── occupancy_analyzer.py        # Occupancy analysis engine
├── visualization_generator.py   # Chart and graph generation
├── report_generator.py          # Report generation
├── config.py                    # Configuration settings
├── requirements.txt             # Python dependencies
├── hotel.zip                    # Input database (ZIP archive)
├── hotels.db                    # Extracted database (auto-generated)
├── database_schema.json         # Database schema reference
├── visualizations/              # Generated charts and graphs
│   ├── 01_occupancy_trend.png
│   ├── 02_room_type_performance.png
│   ├── 03_cancellation_analysis.png
│   ├── 04_revenue_analysis.png
│   ├── 05_seasonal_trends.png
│   └── 06_recommendations_summary.png
├── reports/                     # Generated reports
│   ├── occupancy_analysis_report.txt
│   └── analysis_insights.json
└── README.md                    # This file
```

## 📊 Generated Outputs

### Visualizations

The system generates 6 professional charts:

1. **Occupancy Trend Over Time** - Line chart showing occupancy rates across dates
2. **Room Type Performance** - Bar charts comparing occupancy and bookings by room type
3. **Cancellation Analysis** - Pie and bar charts showing booking status distribution
4. **Revenue Analysis** - Bar chart showing revenue by room type
5. **Seasonal Trends** - Line and bar charts showing monthly patterns
6. **Recommendations Summary** - Priority-based recommendation distribution

### Reports

1. **occupancy_analysis_report.txt** - Executive summary with:
   - Overall occupancy performance
   - Room type analysis
   - Cancellation insights
   - Revenue summary
   - Seasonal patterns
   - Key recommendations
   - Action items (short, medium, long-term)

2. **analysis_insights.json** - Detailed data in JSON format for programmatic access

## 🎯 Key Metrics Analyzed

### Occupancy Metrics
- Average occupancy rate (%)
- Maximum and minimum rates
- Occupancy trends (increasing/decreasing)
- Occupancy by room type
- Occupancy by time period

### Revenue Metrics
- Total revenue
- Average daily revenue
- Revenue by room type
- Average price per booking
- Seasonal revenue patterns

### Operational Metrics
- Booking completion rate
- Cancellation rate
- Cancellation reasons (if available)
- Repeat guest percentage
- Room utilization rates

### Performance Indicators
- Peak seasons
- Low seasons
- High-performing room types
- Underperforming areas
- Revenue opportunities

## 💡 Recommendations Engine

The system automatically generates recommendations in three categories:

**HIGH PRIORITY** 🔴
- Address critical occupancy issues (< 70%)
- Reduce high cancellation rates (> 20%)
- Fix underperforming room types (< 50% occupancy)

**MEDIUM PRIORITY** 🟠
- Optimize pricing strategies
- Improve marketing targeting
- Enhance customer communication

**LOW PRIORITY** 🟢
- Refinement strategies
- Long-term improvements
- Guest experience enhancements

## 📈 Usage Tips

### Regular Analysis
- Run the analysis monthly to track progress
- Compare month-over-month improvements
- Monitor KPI trends

### Presentation
- Share visualizations with management team
- Use reports in board meetings
- Track implemented recommendation ROI

### Optimization
- Implement high-priority recommendations first
- Monitor results after each change
- Adjust strategies based on seasonal patterns
- Use revenue data for pricing decisions

## 🔧 Configuration

Edit `config.py` to customize:

- Occupancy target threshold
- Cancellation alert threshold
- Low performance threshold
- Color schemes for visualizations
- Report sections and content

## 📝 Database Requirements

The system expects the following tables in hotels.db:

- **bookings** - Booking records with dates, prices, status
- **rooms** - Room information with type and pricing
- **guests** - Guest information

Required columns:
- bookings: booking_id, room_id, guest_id, check_in_date, check_out_date, price, status
- rooms: room_id, room_type, price_per_night
- guests: guest_id (additional fields optional)

## 🐛 Troubleshooting

### "hotel.zip not found"
- Ensure hotel.zip is in the project root directory
- Check file name is exactly "hotel.zip"

### "hotels.db not found after extraction"
- Verify hotel.zip is not corrupted
- Try extracting manually and checking contents
- Ensure sufficient disk space

### "No data to plot" messages
- Check database has valid data in required tables
- Verify database is not empty
- Review database schema in database_schema.json

### Import errors
- Reinstall requirements: `pip install -r requirements.txt --upgrade`
- Check Python version is 3.7+
- Use virtual environment for isolation

## 📞 Support

For issues or questions:
1. Check this README
2. Review generated reports and logs
3. Verify database integrity
4. Check Python version compatibility

## 📄 License

This project is for hotel occupancy analysis and improvement.

## 🎓 Key Insights from Analysis

The system helps identify:

- **Bottlenecks**: Rooms/periods with low occupancy
- **Opportunities**: Peak seasons and high-performing room types
- **Risks**: High cancellation rates and revenue vulnerabilities
- **Trends**: Booking patterns and seasonal variations
- **Strategies**: Data-driven recommendations for improvement

## 🚀 Next Steps After Analysis

1. **Review Reports** - Examine occupancy_analysis_report.txt
2. **Study Visualizations** - Analyze charts in visualizations/ folder
3. **Prioritize Recommendations** - Focus on HIGH priority items first
4. **Implement Changes** - Execute recommendations
5. **Track Results** - Run analysis again in 1 month
6. **Iterate** - Refine strategies based on results

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Status**: Active
