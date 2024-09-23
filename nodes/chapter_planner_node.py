from chains.plan_chain import story_plan_chain
import json

def chapter_helper(chapter_plan):
    total_chapters = len(chapter_plan['chapters'])
    current_chapter = 1
    return {
        "total_chapters": total_chapters,
        "current_chapter": 1
    }


def chapter_planner_node(state):
    """This node is responsible for creating a detailed plan for each chapters - based on the user prompt & the story characteristics
    this node will create a detailed plan for each chapters and adds more info like chapter summary - characters involved.
    TODO: Add an example"""

    print("--Planning the chapters in the story---")

    user_prompt = state["user_prompt"]
    story_characteristics = state["story_characteristics"]

    chapter_plan = story_plan_chain.invoke({"user_prompt": user_prompt, "story_characteristics": story_characteristics})
    chapter_data = chapter_helper(chapter_plan)

    print("--Chapters Plan is ready--")

    return {
        "chapter_plan": chapter_plan,
        "total_chapters": chapter_data["total_chapters"],
        "current_chapter": chapter_data["current_chapter"],
        "previous_chapter": ""
    }
