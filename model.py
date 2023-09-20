from langchain.agents import AgentType,load_tools,initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from key import openai_API
import os
os.environ["OPENAI_API_KEY"] =openai_API 

llm = ChatOpenAI(model="gpt-3.5-turbo",temperature=0)

tools=load_tools(['wikipedia'],llm=llm)

agent=initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True,
    output_key='final answer'
)



custom_prompt="""

if you didn't find the answer, just say that you don't know,
don't try to make up an answer.

for example:
[Sentence]: Cyrus the Great was the king of Italy
[context]: Cyrus the Great was the king of Iran
[You]: No. According to historical data, Cyrus the Great was the king of Iran

[Sentence]: World War II was started by Nazi Germany
[context]: the Second World War began with the Nazi Germany's attack on Poland in 1939
[You]: Correct. According to historical information, the Second World War began with the Nazi Germany's attack on Poland in 1939.

[Sentence]:'1953 Iranian coup was aided by France-and Spain'
[context]:the 1953 Iranian coup d'état was a U.S.- and UK-instigated, Iranian army-led overthrow of the democratically elected Prime Minister Mohammad Mosaddegh in favor of strengthening the monarchical rule of the shah, Mohammad Reza Pahlavi, on 19 August 1953. It was aided by US and UK, and the clergy also played a considerable role. 
[You]:No. According to historical records, the 1953 Iranian coup d'état was a U.S.- and UK-instigated, Iranian army-led overthrow of the democratically elected Prime Minister Mohammad Mosaddegh in favor of strengthening the monarchical rule of the shah, Mohammad Reza Pahlavi, on 19 August 1953. It was aided by US and UK, and the clergy also played a considerable role. 

[Sentence]:{input}
[context]:{context}
[You]:
 
"""



prompt=PromptTemplate(template=custom_prompt,input_variables=['input','context'])



def wiki_fact(query):
    response=agent.run(query)
    chain=LLMChain(llm=llm,prompt=prompt,verbose=False)
    final=chain.run({'input':query,'context':response})
    return final
   
