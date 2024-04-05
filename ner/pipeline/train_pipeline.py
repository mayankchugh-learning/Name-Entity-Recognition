import sys
from ner.components.data_ingestion import DataIngestion
from ner.configuration.gcloud import GCloud
from ner.constants import *

from ner.entity.artifact_entity import (
    DataIngestionArtifacts,
    )


from ner.entity.config_entity import (
    DataIngestionConfig
)


from ner.exception import NerException
from ner.logger import logging


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.gcloud = GCloud()

    
     # This method is used to start the data ingestion
    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from Google cloud storage")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config, gcloud=self.gcloud
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from Google cloud storage")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact

        except Exception as e:
            raise NerException(e, sys) from e
        

    # This method is used to start the training pipeline
    def run_pipeline(self) -> None:
        try:
            logging.info("Started Model training >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            data_ingestion_artifact = self.start_data_ingestion()
            
            data_ingestion_artifact=data_ingestion_artifact

        except Exception as e:
            raise NerException(e, sys) from e
