import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)

def clean_member_data(df: pd.DataFrame):
    logger.info('Starting cleaning process for Member')
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    logger.info(f'dropped {before - after} duplicate rows')
    mandetory_cols = ['member_id','first_name','last_name','dob']
    df = df.dropna(subset=mandetory_cols)
    logger.info('Removed rows with missing/null mandetory fields')
    df['first_name'] = df['first_name'].str.title()
    df['last_name'] = df['last_name'].str.title()
    df['city'] = df['city'].str.title()

    df['dob'] = pd.to_datetime(df['dob'], errors='coerce')
    df = df.dropna(subset=['dob'])
    logger.info('Converted dob to datetime')
    logger.info('Cleaning completed successfully')

    return df

def save_clean_data(df, output_path):
    df.to_csv(output_path, index=False)
    logger.info(f'Cleaned data saved at {output_path}')



