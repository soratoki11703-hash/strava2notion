"""Notion database schema definitions."""

# Schema for strava2notion v2
# Matches the properties used in the original implementation
SCHEMA = {
    "Name": {"title": {}},
    "Type": {"select": {}},
    "Distance (km)": {"number": {"format": "number"}},
    "Moving Time (min)": {"number": {"format": "number"}},
    "Elapsed Time (min)": {"number": {"format": "number"}},
    "Power (W)": {"number": {"format": "number"}},
    "Elevation (m)": {"number": {"format": "number"}},
    "Date": {"date": {}},
    "Strava Link": {"url": {}},
    "Strava ID": {"rich_text": {}},  # For deduplication
}
