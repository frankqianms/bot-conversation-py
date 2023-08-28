from datetime import datetime
from langchain import PromptTemplate
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

def returnme() -> str:
    return "return me"

def prompt(query: str, template: str=None) -> str:
    if template is None:
        # template = """{query}"""
        template = """ 
        I want you to reason the query: {query}.
        Please remember the following:
        1) Current year is 2023.
        2) {returnme} is the answer to the query.
        """
    prompt = PromptTemplate(
        input_variables=["query", "returnme"],
        template=template
    )

    return prompt.format(query=query, returnme=returnme())