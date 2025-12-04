from ingestion.ingest_dummy import ingest_dummy_file
from utils.logger import get_logger

logger = get_logger(__name__)

#logger = get_logger(__name__)
#logger.info("Week 1 Day 1 setup complete.")

if __name__ == "__main__":
    logger.info("Running Day 2 test ingestion.")

    df = ingest_dummy_file()

    if df is not None:
        logger.info("Ingestion completed successfully.")
        print(df.head())
    else:
        logger.error("Ingestion failed.")
