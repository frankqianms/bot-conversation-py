# agents
from bots.utils.agent import FakeAgent
from bots.utils.agent import agent

async def askAI(query: str):
    # question prompt
    # prompt_template = PromptTemplate.from_template(
    #     "What is the answer of this question: {query}?"
    # )
    # prompt_template.format(query=query)
    # ask question
    answer = agent.run(query)
    # answer = llm(query)
    return answer
