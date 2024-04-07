from dataclasses import dataclass, field

@dataclass
class SolutionParameters:
    STORAGE_DIR: str = field(default_factory=lambda:"storage")  # NOTE: directory to cache the generated index.
    DATA_DIR: str = field(default_factory= lambda: "data")  # NOTE: directory containing the documents.
    API_KEY_SOLAR_LLM: str = field(default="hack-with-upstage-solar-0407")
    LAYOUT_ANALYZER: str = field(default="hack-with-upstage-docai-0407")
