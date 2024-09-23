from langchain.schema import Document
from chains.write_chain import write_chapter_chain

def writing_node(state):
    """This node is responsible for writing each chapters - and update the state of the graph according to the chapters already
    written. TODO: Insert example"""

    print("--Writing the Chapters--")
    user_prompt = state["user_prompt"]
    story_characteristics = state["story_characteristics"]
    chapter_plan = state["chapter_plan"]
    current_chapter = state["current_chapter"]

    total_chapters = state["total_chapters"]
    chapters = []

    for chapter_num in range (current_chapter, total_chapters+1):
        previous_chapter = state["previous_chapter"]
        print(f"--Working on chapter: {chapter_num}")

        result = write_chapter_chain.invoke({
            "user_prompt": user_prompt,
            "story_characteristics": story_characteristics,
            "chapter_plan": chapter_plan,
            "previous_chapter": previous_chapter,
            "current_chapter": chapter_num
        })

        state["previous_chapter"] = result
        state["current_chapter"] = chapter_num
        chapters.append(result)

        print(f"--Concluded the chapter: {chapter_num}")
        
        ### need to check if we just need previous chapter or the whole story?
    final_story = '\n\n'.join(chapters)

    print("--Final story is created--")

    return {
        "final_story": final_story
    }


    

