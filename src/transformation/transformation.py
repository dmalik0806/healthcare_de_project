from utils.logger import get_logger
import pandas as pd
from datetime import datetime

logger = get_logger(__name__)
today = datetime.today()

def transform_data(df):
    logger.info("Starting transformation process")
    df['first_name'] = df['first_name'].str.title().str.strip()
    df['last_name'] = df['last_name'].str.title().str.strip()

    # standardize gender values
    df['gender'] = df['gender'].str.lower().map({'M':'Male','male':'Male','F':'Female','female':'Female'}).fillna('Unknown')

    # Derived fields
    df["age"] = df["dob"].apply(lambda x: today.year - x.year - ((today.month, today.day) < (x.month, x.day)))
    df['age'] = pd.to_numeric(df['age'], errors = 'coerce')
    df['full_name'] = df['first_name'] + " " + df['last_name']
    df['ingestion_date'] = datetime.now().strftime('%Y-%m-%d')

    def get_age_group(age):
        if pd.isna(age):
            return "Unknown"
        if age < 18:
            return "Child"
        if age < 60:
            return "Adult"
        return "Senior"

    df['age_group'] = df['age'].apply(get_age_group)
    logger.info("transformation process completed")
    return df    
