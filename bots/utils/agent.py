from ast import Dict
from gc import callbacks
import os

from typing import List, Optional, Tuple, Any, Union, Dict
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain.llms import OpenAI
from langchain import SerpAPIWrapper
from langchain.agents.tools import Tool
from langchain import LLMMathChain
from langchain.memory import ConversationBufferMemory, ConversationSummaryBufferMemory
from openapi_schema_pydantic import Callback
from pydantic import BaseModel, Field
from bots.utils.models import llm

## basic tools
# def error_handle(error: str) -> str:
#     return "return final output"
# # load tools
# tools = load_tools(["bing-search", "llm-math"], llm=llm)
# # initialize agent
# agent = initialize_agent(
#     tools, 
#     llm, 
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
#     verbose=True,
#     max_iterations=10,
#     handle_parsing_errors=error_handle,
# )

## user defined Tools
# class MyTool(Tool):
#     def __init__(self, name: str, func: Any, description: str, args_schema: Any):
#         super().__init__(name=name, func=func, description=description, args_schema=args_schema)
#         self.name = name
#         self.func = func
#         self.description = description
#         self.args_schema = args_schema

#     def run(
#         self,
#         *args: Any,
#         callbacks: Callback = None,
#         tags: Optional[List[str]] = None,
#         metadata: Optional[Dict[str, Any]] = None,
#         **kwargs: Any,
#     ) -> Any:
#         # return self.func(query)
#         return "1+1=2; 2023-1953=70; 70^0.43=6.214299"

# class CalculatorInput(BaseModel):
#     query: str = Field()

# llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

# tools.append(
#     MyTool(
#         name="MyCalculator",
#         func=llm_math_chain.run,
#         description="useful for when you need to answer questions about math",
#         args_schema=CalculatorInput
#     )
# )
# agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

## plan and execute
# search = SerpAPIWrapper()
# llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
# tools = [
#     Tool(
#         name = "Search",
#         func=search.run,
#         description="useful for when you need to answer questions about current events"
#     ),
#     Tool(
#         name="Calculator",
#         func=llm_math_chain.run,
#         description="useful for when you need to answer questions about math"
#     ),
# ]

# planner = load_chat_planner(llm)
# executor = load_agent_executor(llm, tools, verbose=True)
# agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

## conversational agent
def create_agent(tool):
    tools = load_tools(["bing-search", "llm-math"], llm=llm)
    tools.append(tool)
    memory = ConversationBufferMemory(memory_key="chat_history")
    agent_chain = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory, handle_parsing_errors=True)
    agent = agent_chain
    return agent
