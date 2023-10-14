from langchain.prompts import PromptTemplate

reference_doc_prmpt = "Given the following answer and context, extract any part of the context *AS IS* that is " \
                      "relevant to the answer. If none of the context is relevant return NO_OUTPUT. " \
                      "Remember, *DO NOT* edit the extracted parts of the context." \
                      "> Answer: {answer}" \
                      "> Context:" \
                      ">>>" \
                      "{context}" \
                      ">>>" \
                      "Extracted relevant parts:"


def return_citation_template():
    return PromptTemplate.from_template(reference_doc_prmpt)

