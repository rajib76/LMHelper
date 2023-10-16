from typing import Optional

from langchain.schema.runnable import Runnable, RunnableConfig
from langchain.schema.runnable.utils import Input, Output
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine


class PresidioIdentifyChain(Runnable):
    """
    Pre-requisites
    To use microsoft presidio we need presidio-analyzer and spacy model
    pip install presidio-analyzer
    python -m spacy download en_core_web_lg
    """
    def get_default_entities(self):
        DEFAULT = ["PHONE_NUMBER","EMAIL_ADDRESS"]
        return DEFAULT

    def invoke(self, input: Input, config: Optional[RunnableConfig] = None) -> Output:
        entities = self.get_default_entities()
        analyzer = AnalyzerEngine()
        results = analyzer.analyze(text=input,
                                   entities=entities,
                                   language='en')
        anonymizer = AnonymizerEngine()

        anonymized_text = anonymizer.anonymize(text=input, analyzer_results=results)

        return anonymized_text.text


if __name__=="__main__":
    pc = PresidioIdentifyChain()
    metadata = {"entities":["PHONE_NUMBER","EMAIL_ADDRESS"]}
    rc = RunnableConfig(metadata=metadata)
    print(rc)
    resp = pc.invoke(input="My phone number is 4694684155 and email is rajib76@yahoo.com")
    print(resp)