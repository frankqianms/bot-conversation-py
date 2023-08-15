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
    
class FakeAgent(BaseSingleActionAgent):
    """Fake Custom Agent."""
    
    @property
    def input_keys(self):
        return ["input"]
    
    def plan(
        self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """Given input, decided what to do.
 
        Args:
            intermediate_steps: Steps the LLM has taken to date,
                along with observations
            **kwargs: User inputs.
 
        Returns:
            Action specifying what tool to use.
        """
        return AgentAction(tool="Search", tool_input=kwargs["input"], log="")
 
    async def aplan(
        self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """Given input, decided what to do.
 
        Args:
            intermediate_steps: Steps the LLM has taken to date,
                along with observations
            **kwargs: User inputs.
 
        Returns:
            Action specifying what tool to use.
        """
        return AgentAction(tool="Search", tool_input=kwargs["input"], log="")

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
# agent = FakeAgent()
# agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)
