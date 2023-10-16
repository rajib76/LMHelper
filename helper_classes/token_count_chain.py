from typing import Optional

import tiktoken
from langchain.schema.runnable import Runnable, RunnableConfig
from langchain.schema.runnable.utils import Input, Output


class TokenCountChain(Runnable):

    def invoke(self, input: Input, config: Optional[RunnableConfig] = None) -> Output:
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        num_tokens = len(encoding.encode(input))
        return num_tokens