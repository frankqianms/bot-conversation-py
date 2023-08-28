# agents
from bots.utils.agent import agent
from bots.utils.prompt import prompt

async def askAI(query: str):
    # question prompt
    # prompt_template = PromptTemplate.from_template(
    #     "What is the answer of this question: {query}?"
    # )
    # prompt_template.format(query=query)
    # ask question
    answer = agent.run(prompt(query))
    # answer = llm(query)
    return answer
