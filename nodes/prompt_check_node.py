from langchain.schema import Document
from chains.prompt_check_chain import prompt_check_chain

def prompt_check_node(state):
    """Takes the user prompt and checks if the prompt is related to writing stories. If user prompt is not related to 
    writing stories - prints appropirate output and exits"""
    print("--Validating User Prompt--")
    
    user_prompt = state['user_prompt']
    is_user_prompt_valid = prompt_check_chain.invoke({"user_prompt": user_prompt})
    print(f"--Prompt Validated: Is user Prompt Related to writing stories? - {is_user_prompt_valid}--")

    return {
        "user_prompt": user_prompt,
        "is_user_prompt_valid": is_user_prompt_valid
    }
