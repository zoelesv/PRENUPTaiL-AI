import logging
import os

from app.engine.constants import SolutionParameters
from llama_index.core.storage import StorageContext
from llama_index.core.indices import load_index_from_storage

logger = logging.getLogger("uvicorn")


params = SolutionParameters()


def get_index():
    # check if storage already exists
    if not os.path.exists(params.STORAGE_DIR):
        raise Exception(
            "StorageContext is empty - call 'python app/engine/generate.py' to generate the storage first"
        )

    # load the existing index
    logger.info(f"Loading index from {params.STORAGE_DIR}...")
    storage_context = StorageContext.from_defaults(persist_dir=params.STORAGE_DIR)
    index = load_index_from_storage(storage_context)
    logger.info(f"Finished loading index from {params.STORAGE_DIR}")
    return index
