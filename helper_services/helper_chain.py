from langchain.schema.runnable import Runnable, RunnableConfig

from helper_classes.pii_deidentify_chain import PresidioIdentifyChain
from helper_classes.prompt_injection_chain import PromptInjection
from helper_classes.token_count_chain import TokenCountChain
from helper_services.base_chain import BaseHelper
from helper_services.chain_function_map import chain_map
from prompt_templates.citation_chain import return_citation_template


class HelperChain(BaseHelper):

    def get_citation_chain(self) -> Runnable:
        prompt = return_citation_template()
        chain = prompt | self.llm

        return chain

    def get_presidio_pii_chain(self) -> Runnable:
        presidio_pii_chain = PresidioIdentifyChain()
        return presidio_pii_chain

    def get_prompt_injection_chain(self) -> Runnable:
        prompt_injection_chain = PromptInjection()
        return prompt_injection_chain

    def get_token_count_chain(self) -> Runnable:
        tcount_chain = TokenCountChain()
        return tcount_chain

    def get_chain(self, helper_type) -> Runnable:
        helper_function = chain_map[helper_type]
        return getattr(self, helper_function)()
