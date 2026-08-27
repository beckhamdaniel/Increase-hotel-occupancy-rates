# 🚀 Setup & Installation Guide

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.7 or higher
- **Disk Space**: At least 100MB for database and outputs
- **RAM**: 2GB minimum (4GB recommended)

## Step-by-Step Installation

### Step 1: Prepare Your Environment

#### Option A: Using Virtual Environment (Recommended)

```bash
# Navigate to project directory
cd Increase-hotel-occupancy-rates

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### Option B: Using System Python

```bash
# Navigate to project directory
cd Increase-hotel-occupancy-rates

# No additional setup needed
```

### Step 2: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list
```

You should see:
- pandas
- numpy
- matplotlib
- seaborn

### Step 3: Prepare Database File

1. **Ensure hotel.zip is in the root directory**
   ```bash
   # Check if file exists
   ls -la hotel.zip        # macOS/Linux
   dir hotel.zip           # Windows
   ```

2. **Verify file integrity**
   ```bash
   # Try listing contents (macOS/Linux)
   unzip -l hotel.zip
   
   # If corrupted, you may see errors
   ```

### Step 4: Run the Analysis

```bash
# Execute main program
python main.py
```

### Step 5: Access Results

After successful execution, check:

```bash
# View generated files
ls visualizations/      # Charts and graphs
ls reports/             # Text and JSON reports
cat reports/occupancy_analysis_report.txt  # Read report
```

## Expected Output

When you run `python main.py`, you should see:

```
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║              🏨 HOTEL OCCUPANCY RATE IMPROVEMENT SYSTEM 🏨                    ║
║                                                                                ║
║                    Comprehensive Analysis & Recommendations                   ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

================================================================================
                    STEP 1: DATABASE EXTRACTION & SETUP
================================================================================

📁 Setting up project directories...
✅ Project directories created

📦 Extracting hotel.zip...
✅ Successfully extracted hotels.db to root folder

... [continues with analysis steps] ...

✅ All tasks completed successfully!
```

## File Locations

After running, files are organized as:

```
Increase-hotel-occupancy-rates/
├── hotels.db                          # Extracted database
├── database_schema.json               # Schema reference
├── visualizations/
│   ├── 01_occupancy_trend.png
│   ├── 02_room_type_performance.png
│   ├── 03_cancellation_analysis.png
│   ├── 04_revenue_analysis.png
│   ├── 05_seasonal_trends.png
│   └── 06_recommendations_summary.png
└── reports/
    ├── occupancy_analysis_report.txt
    └── analysis_insights.json
```

## Sharing Results with Management

### For Presentations:
1. Use PNG files from `visualizations/` folder
2. Present charts one by one
3. Reference specific numbers from the report

### For Documentation:
1. Share `occupancy_analysis_report.txt` with key findings
2. Include `analysis_insights.json` for data analysts
3. Attach key visualizations

### For Decision Making:
1. Highlight the "KEY RECOMMENDATIONS" section
2. Emphasize "ACTION ITEMS" with timelines
3. Reference specific metrics and trends

## Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'pandas'"
**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: "FileNotFoundError: hotel.zip not found"
**Solution:**
- Verify hotel.zip exists in root directory
- Check exact filename (case-sensitive on macOS/Linux)
- Ensure file wasn't moved or renamed

### Issue: "Permission denied" on macOS/Linux
**Solution:**
```bash
chmod +x main.py
python main.py
```

### Issue: "No module named 'sqlite3'"
**Solution:**
Reinst Python or use:
```bash
pip install pysqlite3
```

## Advanced Setup

### Schedule Regular Analysis

#### Windows (Task Scheduler):
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (e.g., monthly)
4. Action: Start a program → python main.py
5. Set working directory to project folder

#### macOS/Linux (Cron):
```bash
# Edit crontab
crontab -e

# Add line to run monthly (1st of month at 9 AM)
0 9 1 * * cd /path/to/project && python main.py
```

### Custom Configuration

Edit `config.py` to customize:

```python
# Occupancy targets
OCCUPANCY_TARGET = 75  # Change from 70 to 75

# Alert thresholds
CANCELLATION_THRESHOLD = 15  # Change from 20 to 15
LOW_ROOM_PERFORMANCE_THRESHOLD = 60  # Change from 50 to 60

# Colors for visualizations
COLOR_EXCELLENT = "#00AA00"  # Custom green
```

## Performance Tips

- **First Run**: May take 1-2 minutes with large databases
- **Subsequent Runs**: Usually complete in 30-60 seconds
- **Large Databases**: Consider limiting date ranges in analyzer
- **Memory Usage**: Monitor system resources during execution

## Verification Checklist

- [ ] Python 3.7+ installed
- [ ] All dependencies installed (pip list)
- [ ] hotel.zip in root directory
- [ ] All code files present
- [ ] Execute permissions set (if needed)
- [ ] Sufficient disk space available
- [ ] No other programs locking hotel.zip

## Getting Help

1. **Check this guide** for your specific issue
2. **Review error messages** for clues
3. **Check file paths** and permissions
4. **Verify database integrity** with separate SQL tool
5. **Review logs** if generated

## Next Steps

After successful installation:

1. ✅ Run `python main.py` first time
2. ✅ Review generated visualizations
3. ✅ Read occupancy_analysis_report.txt
4. ✅ Share findings with management
5. ✅ Implement recommendations
6. ✅ Schedule monthly analysis runs
7. ✅ Track improvements over time

---

**Need Help?** Review README.md or check specific error messages above.
