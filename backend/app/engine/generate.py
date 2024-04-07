from dotenv import load_dotenv
from abc import abstractmethod, ABC
from dataclasses import dataclass, field

load_dotenv()

import logging
from llama_index.core.indices import (
    VectorStoreIndex,
)
from app.engine.constants import SolutionParameters
from app.engine.loader import InputRepo
from app.settings import init_settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

params = SolutionParameters()
input_layer = InputRepo()


@dataclass
class AbstractService(ABC):

    @abstractmethod
    def execute():
        """ Execute main function for services. """

###

@dataclass
class GenerateDataService(AbstractService):
    task: str = field(init=True)

    def execute(self) -> callable:
        match self.task:
            case default:
                return self.generate_datasource()


    def generate_datasource():
        logger.info("Creating new index")
        # load the documents and create the index
        documents = input_layer.get_documents()
        index = VectorStoreIndex.from_documents(
            documents,
        )
        # store it for later
        index.storage_context.persist(params.STORAGE_DIR)
        logger.info(f"Finished creating new index. Stored in {params.STORAGE_DIR}")


if __name__ == "__main__":
    init_settings()
    generator = GenerateDataService()
    generator.generate_datasource()
