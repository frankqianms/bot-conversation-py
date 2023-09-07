# agents
# from bots.utils.agent import agent
from bots.utils.agent import create_agent
from bots.utils.prompt import prompt
from bots.utils.models import llm
from bots.utils.retriever import create_vectorstore

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.agents.tools import Tool
from langchain.agents import load_tools, initialize_agent, AgentType

class AIAsker:
    def __init__(self, loader=None):
        self._loader = loader
        self._chat_history = []
        self._answer = None
        self._memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self._docs = None
        self._vectorstore = None
        self._agent = None

    async def askAI(self, query: str, loader=None):
        # question prompt
        # prompt_template = PromptTemplate.from_template(
        #     "What is the answer of this question: {query}?"
        # )
        # prompt_template.format(query=query)
        # ask question
        # answer = agent.run(prompt(query))
        if self._docs is None:
            docs = await loader.split() if loader else None
            self._vectorstore = await create_vectorstore(docs)

        self._chat_history = [(query, self._answer if self._answer else "")]
        if self._agent is None:
            tools = load_tools(["bing-search", "llm-math"], llm=llm)
            if self._vectorstore:
                qa = ConversationalRetrievalChain.from_llm(llm, self._vectorstore.as_retriever(), memory=self._memory)
                tool = Tool(
                    name='ConversationalRetrievalChain', 
                    func = lambda query: qa({"question": query, "chat_history": self._chat_history}), 
                    description = 'useful for when you need to answer questions about current files' 
                )
                tools.append(tool)
            memory = ConversationBufferMemory(memory_key="chat_history")
            agent_chain = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=memory, handle_parsing_errors=True)
            self._agent = agent_chain
            # self._agent = create_agent(tool)
            

        self._answer = self._agent.run(query)
        return self._answer
