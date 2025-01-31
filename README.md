# ethiopian-medical-data-warehouse

## Overview
This repository implements a pipeline to scrape and clean data from public Telegram channels relevant to Ethiopian medical businesses, focusing on **Task 1** (Data Scraping) and **Task 2** (Data Cleaning).

## Objectives
- Extract text and image data from specified Telegram channels.
- Store raw data in a structured format.
- Clean and transform the data for analysis and integration.

---

## Task 1: Data Scraping

### Description
Task 1 builds a robust pipeline to extract data using `telethon`.

### Features
- Scrapes text messages and metadata (e.g., sender ID, timestamp).
- Optimized with batch processing and asynchronous execution.
- Logs progress and errors.

### Example Usage
```bash
pip install -r requirements.txt
python scripts/scrape_telegram.py
```

---

## Task 2: Data Cleaning

### Description
Task 2 focuses on cleaning and structuring the scraped data.

### Features
- Removes duplicates and empty messages.
- Standardizes formats for dates and text fields.
- Consolidates raw data for analysis.

### Example Usage
```python
import pandas as pd
raw_data = pd.read_csv("data/raw/DoctorsET.csv")
cleaned_data = clean_raw_data(raw_data)
cleaned_data.to_csv("data/processed/DoctorsET_cleaned.csv", index=False)
```



## Dependencies
Install all required Python packages via:
```bash
pip install -r requirements.txt
```

---
