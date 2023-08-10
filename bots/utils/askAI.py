import os
from langchain import PromptTemplate
from langchain.llms import AzureOpenAI

class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""


    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split(", ")

def askAI(query: str):
    llm = AzureOpenAI(temperature=0.7)
    prompt_template = PromptTemplate(
        "What is the answer of this question: {query}?",
    )
    prompt_template.format(query=query)
    return llm(prompt_template)
