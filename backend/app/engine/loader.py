from llama_index.core.readers import SimpleDirectoryReader

from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from typing import Any, List
from app.engine.constants import SolutionParameters
import logging

from dotenv import load_dotenv
from abc import abstractmethod, ABC
from dataclasses import dataclass, field

load_dotenv()

import logging
from llama_index.core.indices import (
    VectorStoreIndex,
)
from app.engine.constants import SolutionParameters


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

params = SolutionParameters()


# def get_documents():
#     return SimpleDirectoryReader(params.DATA_DIR).load_data()


@dataclass
class AbstractContractManager(ABC):
    menu: List[str] = field(init=True, default=["prenup"])

    @abstractmethod
    def execute():
        """ Execute main function depending on contract type. """



@dataclass
class AbstractRepository(ABC):
    task: str = field(init=True, default=None)
    menu: List[str] = field(init=True, default=["input", "output"])

    @abstractmethod
    def run(self):
        """ Main function for repositories. """


###

@dataclass
class InputRepo(AbstractRepository):
    task: str = field(init=True, default="input")
    repo: str = field(init=True, default_factory=lambda: params.DATA_DIR)

    def run(self) -> callable:
        match self.task:
            case "input":
                return self.get_documents()
            case default:
                return None


    def get_documents():
        return SimpleDirectoryReader(params.DATA_DIR).load_data()


input_layer = InputRepo()

###   

@dataclass
class OutputRepo(AbstractRepository):
    task: str = field(init=True, default="output")
    repo: str = field(init=True, default_factory=lambda: params.STORAGE_DIR)

    def run(self) -> callable:
        match self.task:
            case "output":
                return self.generate_datasource()
            case default:
                return None


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