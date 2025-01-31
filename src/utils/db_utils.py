import os
from dotenv import load_dotenv
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import logging

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

def get_db_connection():
    """Create a database connection using environment variables"""
    try:
        connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT')
        )
        return connection
    except Exception as e:
        logger.error(f"Error connecting to database: {str(e)}")
        raise

def save_to_db(df, table_name, if_exists='replace'):
    """Save DataFrame to PostgreSQL database"""
    try:
        db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@" \
                 f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        
        engine = create_engine(db_url)
        
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists=if_exists,
            index=False
        )
        
        logger.info(f"Successfully saved {len(df)} rows to {table_name}")
        
    except Exception as e:
        logger.error(f"Error saving to database: {str(e)}")
        raise