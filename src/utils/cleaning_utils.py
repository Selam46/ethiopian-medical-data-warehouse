import pandas as pd
import re
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def clean_text(text):
    """Clean text data by removing special characters and extra whitespace"""
    if pd.isna(text):
        return text
    # Remove special characters except hashtags
    text = re.sub(r'[^\w\s#]', ' ', str(text))
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text

def standardize_date(date):
    """Standardize date format"""
    if pd.isna(date):
        return date
    return pd.to_datetime(date).strftime('%Y-%m-%d %H:%M:%S')

def remove_duplicates(df):
    """Remove duplicate entries based on text and date"""
    initial_len = len(df)
    df = df.drop_duplicates(subset=['text', 'date'], keep='first')
    logger.info(f"Removed {initial_len - len(df)} duplicate entries")
    return df

def validate_data(df):
    """Validate data and return boolean mask of valid rows"""
    valid_mask = (
        df['text'].notna() &
        df['date'].notna() &
        df['channel'].notna()
    )
    return valid_mask