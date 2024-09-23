import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LLMs.llm import LLM

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

with open(os.path.join(os.path.dirname(__file__), 'prompts', 'check_prompt.txt'), 'r') as file:
    check_user_input = file.read()

check_user_prompt = ChatPromptTemplate([
    ('user', check_user_input)
])

prompt_check_chain = check_user_prompt | LLM | StrOutputParser()

## For testing
if __name__ == "__main__":
    #Test the prompt_check_chain
    #test_instruction = "Today we went to a whale watching movie. it was fun"
    # test_instruction = "Stories are so cool"
    # test_instruction = "Someone should write a story about superheros in seattle"1
    test_instruction = "Imagine a story where a superhero is being abduceted by aliens - how we fights and overcomes a stuggle"


    #Invoke the chain
    result = prompt_check_chain.invoke({"user_prompt": test_instruction})

    print("Is user input related to writing a story:")
    print(result)

