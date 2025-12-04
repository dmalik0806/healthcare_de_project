import pandas as pd
import os

from utils.logger import get_logger
from utils.config_reader import load_config

logger = get_logger(__name__)

def ingest_dummy_file():
    logger.info("Starting ingestion process")
    config = load_config()
    input_path = config["input_path"]
    file_path = os.path.join(input_path, "dummy_members.csv")

    if not os.path.exists(file_path):
        logger.error(f'File not found: {file_path}')
        return None
    
    df = pd.read_csv(file_path)
    logger.info(f'Read {len(df)} records from {file_path}')

    return df

    

