import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LLMs.llm import LLM

from langchain_core.output_parsers import  JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

with open(os.path.join(os.path.dirname(__file__), 'prompts', 'story_category.txt'), 'r') as file:
    story_catgory = file.read()

## we also need to make this chain read - input from the actual file we will be using

story_category_prompt = ChatPromptTemplate({
    ("user", story_catgory)
})

story_category_chain = story_category_prompt | LLM | JsonOutputParser()

##For testing

if __name__ == "__main__":
    # test_instruction = f"""I'm thinking about writing a story where the Protaganist struggles a lot in life - he is the most weak person - but then he gets access to 
    # a system - which helps him & trains him to become the best in life"""
    test_instruction = f"""I'm thinking of writing a romantic story - where two people meet during their master's studies - they are originally from different part of the world
    but they meet during their masters & they will be in relationship - the story should be how they enjoy life, difficulties they face, struggles in masters
    how much fun they had - but the story ends with two of them breaking up - the ending should be melodramatic & bittersweet"""

    result = story_category_chain.invoke({"user_prompt":test_instruction})
    print(result)