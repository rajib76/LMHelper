from abc import abstractmethod, ABC

from langchain.chat_models import ChatOpenAI
from langchain.schema.language_model import BaseLanguageModel
from pydantic import BaseModel, root_validator


class BaseHelper(BaseModel,ABC):
    llm: BaseLanguageModel

    @root_validator
    def validate_llm(cls, values: dict) -> dict:
        if not isinstance(values["llm"], ChatOpenAI):
            raise ValueError("Only supported with ChatOpenAI models.")
        return values

    @abstractmethod
    def get_chain(self,helper_type):
        pass
