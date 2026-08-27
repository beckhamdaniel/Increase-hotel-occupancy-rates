"""
Configuration settings for the Hotel Occupancy Analysis System
"""

# Database Configuration
DATABASE_PATH = "hotels.db"
ZIP_FILE_PATH = "hotel.zip"

# Directory Configuration
DATA_DIR = "data"
ANALYSIS_DIR = "analysis"
VISUALIZATION_DIR = "visualizations"
REPORT_DIR = "reports"
LOG_DIR = "logs"

# Analysis Configuration
OCCUPANCY_TARGET = 70  # Target occupancy rate percentage
CANCELLATION_THRESHOLD = 20  # Alert if cancellation rate exceeds this
LOW_ROOM_PERFORMANCE_THRESHOLD = 50  # Alert if room occupancy below this

# Visualization Configuration
FIGURE_DPI = 300
FIGURE_SIZE = (14, 6)

# Color Scheme
COLOR_EXCELLENT = "#06A77D"  # Green
COLOR_WARNING = "#F77F00"    # Orange
COLOR_CRITICAL = "#D62828"   # Red
COLOR_PRIMARY = "#2E86AB"    # Blue

# Report Configuration
REPORT_TITLE = "Hotel Occupancy Rate Analysis Report"
REPORT_SECTIONS = [
    "Occupancy Performance",
    "Room Type Performance",
    "Cancellation Analysis",
    "Revenue Insights",
    "Seasonal Patterns",
    "Key Recommendations",
    "Action Items"
]
