from langchain.schema import Document
from langgraph.graph import StateGraph, END
from typing_extensions import TypedDict
from typing import List

from nodes.chapter_planner_node import chapter_planner_node
from nodes.prompt_check_node import prompt_check_node
from nodes.saving_node import saving_node
from nodes.story_planner_node import story_planner_node
from nodes.writing_node import writing_node

class GraphState(TypedDict):
    """
    Represents the state of our Graph

    Attributes:

    """
    user_prompt: str
    story_characteristics: dict
    chapter_plan: dict
    is_user_prompt_valid: str ## TODO: Change this to boolen
    total_chapters: int
    current_chapter: int
    previous_chapter: str
    final_story: str
    story_characteristics_written: bool #TODO: change this to something more clean
    chapter_plan_written: bool

def should_continue(state):
    if state["is_user_prompt_valid"] == "yes":
        return "story_planner_node"
    print("--Exiting the workflow -> User prompt is not related to writing stories--")
    return END

def create_workflow(llm):
    workflow = StateGraph(GraphState)

    workflow.add_node("prompt_check_node", prompt_check_node)
    workflow.add_node("story_planner_node", story_planner_node)
    workflow.add_node("chapter_planner_node", chapter_planner_node)
    workflow.add_node("writing_node", writing_node)
    workflow.add_node("saving_node", saving_node)

    # Set entry point to the prompt check node
    workflow.set_entry_point("prompt_check_node")

    workflow.add_conditional_edges(
        # First, we define the start node. We use `agent`.
        # This means these are the edges taken after the `agent` node is called.
        "prompt_check_node",
        # Next, we pass in the function that will determine which node is called next.
        should_continue,
        {
            "story_planner_node": "story_planner_node",  # Continue if prompt is valid
            END: END  # End the workflow if the prompt is invalid
        }
    )

    workflow.add_edge("story_planner_node", "chapter_planner_node")
    workflow.add_edge("chapter_planner_node", "writing_node")

    workflow.add_edge("writing_node", "saving_node")
    workflow.add_edge("saving_node", END)

    return workflow.compile()