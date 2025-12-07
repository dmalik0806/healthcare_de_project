from ingestion.ingest_dummy import ingest_dummy_file
from cleaning.member_clean import clean_member_data, save_clean_data  #added for day 3
from transformation.transformation import transform_data #added day 5
from utils.logger import get_logger
from utils.config_reader import load_config  #added for day 3
import os   #added for day 3

logger = get_logger(__name__)

#logger = get_logger(__name__)
#logger.info("Week 1 Day 1 setup complete.")

if __name__ == "__main__":
    #logger.info("Running Day 2 test ingestion.")
    #logger.info('Running day 3: Ingestion --> Cleaning')
    logger.info('Running day 5: Ingestion --> Cleaning --> Transformation')

    config = load_config()
    cleaned_path = config['cleaned_path']

    df_raw = ingest_dummy_file()

    if df_raw is None:
        logger.error('Ingestion failed. Exiting')
        exit()
    #if df_raw is not None:                                     #Added for Day 2
    #    logger.info("Ingestion completed successfully.")
    #    print(df_raw.head())
    #else:
    #    logger.error("Ingestion failed.")

    #Day3: added block for cleaning raw data
    df_cleaned = clean_member_data(df_raw)
    output_file = os.path.join(cleaned_path, 'cleaned_members.csv')
    save_clean_data(df_cleaned, output_file)

    df_transformed = transform_data(df_cleaned)
    df_transformed.to_csv("data/processed/processed_data.csv", index=False)
    print("Pipeline run completed successfully.")

    logger.info('Day 5 pipeline completed')
    print(df_cleaned.head())
