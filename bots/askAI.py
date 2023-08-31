# agents
# from bots.utils.agent import agent
from bots.utils.agent import create_agent
from bots.utils.prompt import prompt
from bots.utils.models import llm
from bots.utils.retriever import create_vectorstore

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

class AIAsker:
    def __init__(self, loader=None):
        self._loader = loader
        self._chat_history = []
        self._answer = None
        self._memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self._docs = None
        self._vectorstore = None

    async def askAI(self, query: str, loader=None):
        # question prompt
        # prompt_template = PromptTemplate.from_template(
        #     "What is the answer of this question: {query}?"
        # )
        # prompt_template.format(query=query)
        # ask question
        # answer = agent.run(prompt(query))
        if self._docs is None:
            docs = await loader.split()
            self._vectorstore = await create_vectorstore(docs)
        qa = ConversationalRetrievalChain.from_llm(llm, self._vectorstore.as_retriever(), memory=self._memory)
        self._chat_history = [(query, self._answer["answer"] if self._answer else "")]
        self._answer = qa({"question": query, "chat_history": self._chat_history})
        # index = create_index(loader)
        # answer = index.query(query, llm=llm)
        # answer = llm(query)
        return self._answer["answer"]
