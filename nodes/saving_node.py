from tools import write_content_to_file
import json

def saving_node(state):
    """This node saves the current state to a file before proceeding."""

    write_content_to_file(json.dumps(state["story_characteristics"], indent=4), "story_characteristics", "json")
    write_content_to_file(json.dumps(state["chapter_plan"], indent=4), "chapter_plan", "json")
    write_content_to_file(state["final_story"], "final_story", "md")
    
    # # If story characteristics haven't been written, write them to a JSON file
    # if "story_characteristics" in state and not state.get("story_characteristics_written", False):
    #     write_content_to_file(json.dumps(state["story_characteristics"], indent=4), "story_characteristics", "json")
    #     return {
    #         "story_characteristics_written": True
    #     }

    # # If chapter plan hasn't been written, write it to a JSON file
    # if "chapter_plan" in state and not state.get("chapter_plan_written", False):
    #     write_content_to_file(json.dumps(state["chapter_plan"], indent=4), "chapter_plan", "json")
    #     return {
    #         "chapter_plan_written": True
    #     }

    # # Write the final story if available, in Markdown format
    # if "final_story" in state and state["final_story"]:
    #     write_content_to_file(state["final_story"], "final_story", "md")
    #     return {

    #     }
