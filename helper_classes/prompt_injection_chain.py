import ast
import json
from typing import Optional

from langchain.schema.runnable import Runnable, RunnableConfig
from langchain.schema.runnable.utils import Input, Output


class PromptInjection(Runnable):
    def invoke(self, input: Input, config: Optional[RunnableConfig] = None) -> Output:
        try:
            from transformers import pipeline
        except ImportError as e:
            raise ImportError(
                "Cannot import transformers, please install with "
                "`pip install transformers`."
            ) from e
        model = pipeline("text-classification", model="deepset/deberta-v3-base-injection")
        injection_classification = model(input)
        injection_classification_json = ast.literal_eval(str(injection_classification[0]))

        return injection_classification_json["label"]
