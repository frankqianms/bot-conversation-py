import os

from typing import List, Tuple, Any, Union
from langchain.schema import AgentAction, AgentFinish
from langchain.agents import BaseSingleActionAgent
from langchain.chat_models import AzureChatOpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

# set llm language model
os.environ["OPENAI_API_TYPE"]=os.environ.get("OPENAI_API_TYPE")
os.environ["OPENAI_API_VERSION"]=os.environ.get("OPENAI_CHAT_API_VERSION")
os.environ["OPENAI_API_BASE"]=os.environ.get("OPENAI_API_BASE")
os.environ["OPENAI_API_KEY"]=os.environ.get("OPENAI_API_KEY")
llm = AzureChatOpenAI(deployment_name='gpt35', model_name='gpt-35-turbo', temperature=0.9)

# load tools
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# initialize agent
agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True,
    max_iterations=10,
    handle_parsing_errors=True,
    handle_llm_errors=True,
)
