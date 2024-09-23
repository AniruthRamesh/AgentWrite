import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LLMs.llm import LLM
from langchain_core.output_parsers import  JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

with open(os.path.join(os.path.dirname(__file__), 'prompts', 'plan.txt'), 'r') as file:
    story_plan = file.read()

story_plan_prompt = ChatPromptTemplate({
    ("user", story_plan)
})

story_plan_chain = story_plan_prompt | LLM | JsonOutputParser()


if __name__ == "__main__":

    user_prompt = f"""I want to create an anime inspired by the Rocky movie style, 
    focusing on an underdog fighter who trains hard to overcome obstacles and compete in a championship match."""
    story_characteristics = f"""
    {{
        "category": "anime",
        "characteristics": {{
            "narrative_style": "Inspirational storytelling with a focus on character growth",
            "themes": [
            "Overcoming adversity",
            "Determination and perseverance",
            "Friendship and mentorship"
            ],
            "plot_structure": {{
            "beginning": "Introduce the protagonist and their humble beginnings",
            "inciting_incident": "Protagonist receives an opportunity to train for a championship",
            "rising_action": "Training montages, challenges, and personal setbacks",
            "climax": "The protagonist faces their main rival in the championship match",
            "resolution": "Reflect on personal growth and lessons learned, win or lose"
            }},
            "setting": "Urban environment with gritty gyms and vibrant street life",
            "character_archetypes": [
            "The Underdog Fighter (Protagonist)",
            "The Mentor (Experienced Trainer)",
            "The Rival (Main Antagonist)",
            "The Supportive Friend"
            ],
            "conflict_types": [
            "Man vs. Self (internal struggles)",
            "Man vs. Man (fighting rival)",
            "Man vs. Society (overcoming societal expectations)"
            ],
            "story_tone": "Motivational and emotional, with moments of humor and camaraderie"
        }}
    }}
    """

    result = story_plan_chain.invoke({"user_prompt":user_prompt, "story_characteristics": story_characteristics})
    print(result)