import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LLMs.llm import LLM
from dotenv import load_dotenv
from graph import create_workflow

load_dotenv()

# Create the workflow
app = create_workflow(LLM)
user_prompt = input("Enter your story prompt: ")


inputs = {
    "user_prompt": user_prompt
}
output = app.invoke(inputs)