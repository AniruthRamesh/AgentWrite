from langchain.schema import Document
from chains.story_characterizer_chain import story_category_chain

def story_planner_node(state):
    """Based on the user-prompt, this node generates a JSON output containing the categories that goes into creating the story that user
    wants to create. TODO: Add an example prompts so users can see what is happening"""

    print("--Planning the Story--")
    print("--Identifying the characteristics of user requested story--")
    user_prompt = state["user_prompt"]
    story_characteristics = story_category_chain.invoke({"user_prompt":user_prompt})

    print("--Story plan is ready--")

    return {
        "story_characteristics": story_characteristics
    }
