import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LLMs.llm import LLM
from langchain_core.output_parsers import  JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

with open(os.path.join(os.path.dirname(__file__), 'prompts', 'write.txt'), 'r') as file:
    write_chapter= file.read()

write_chapter_prompt = ChatPromptTemplate({
    ("user", write_chapter)
})

write_chapter_chain = write_chapter_prompt | LLM | StrOutputParser()

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
    chapter_plan = f"""
    {{
    "chapters": [
        {{
        "chapter_number": 1,
        "title": "Humble Beginnings",
        "summary": "Introduce the protagonist, Alex, who is an underdog fighter with a day job in a bustling urban environment. Highlight Alex's daily struggles and his passion for boxing.",
        "characters": {{
            "Alex (The Underdog Fighter)": {{
            "importance": "Central character whose journey of growth and perseverance drives the story.",
            "note": "Alex's humble beginnings and passion for boxing set the stage for the entire narrative."
            }},
            "Supportive Friend (Sam)": {{
            "importance": "Provides emotional support and comic relief.",
            "note": "Sam's presence helps to highlight Alex's humanity and adds depth to his character."
            }}
        }}
        }},
        {{
        "chapter_number": 2,
        "title": "The Opportunity",
        "summary": "Alex receives an unexpected opportunity to train for a championship match after impressing a local trainer, Max, during a street fight.",
        "characters": {{
            "Alex": {{
            "importance": "Faces a pivotal moment that sets his journey into motion.",
            "note": "Alex's determination and raw talent are showcased."
            }},
            "Max (The Mentor)": {{
            "importance": "Introduces the experienced trainer who sees potential in Alex.",
            "note": "Max's character is crucial for guiding Alex through his training."
            }}
        }}
        }},
        {{
        "chapter_number": 3,
        "title": "First Steps",
        "summary": "Alex begins his rigorous training under Max's guidance. Introduce initial challenges and the grueling nature of his training regimen.",
        "characters": {{
            "Alex": {{
            "importance": "Starts his transformation from an underdog to a fighter.",
            "note": "Highlights Alex's resilience and willingness to endure hardship."
            }},
            "Max": {{
            "importance": "Develops a mentor-mentee relationship with Alex.",
            "note": "Max's tough love and wisdom are essential for Alex's growth."
            }}
        }}
        }},
        {{
        "chapter_number": 4,
        "title": "Setbacks and Struggles",
        "summary": "Alex faces personal setbacks, including injuries and self-doubt. Explore his internal conflicts and the pressure to succeed.",
        "characters": {{
            "Alex": {{
            "importance": "Confronts his own fears and limitations.",
            "note": "This chapter deepens Alex's character by showing his vulnerabilities."
            }},
            "Sam": {{
            "importance": "Provides emotional support and encouragement.",
            "note": "Sam's friendship helps Alex push through his darkest moments."
            }}
        }}
        }},
        {{
        "chapter_number": 5,
        "title": "The Rival Appears",
        "summary": "Introduce Alex's main rival, Jake, a seasoned fighter with a reputation for being unbeatable. Tension builds as Alex realizes the magnitude of his challenge.",
        "characters": {{
            "Alex": {{
            "importance": "Begins to understand the true scale of his challenge.",
            "note": "Alex's determination is tested by the appearance of his formidable rival."
            }},
            "Jake (The Rival)": {{
            "importance": "Serves as the main antagonist and a symbol of Alex's ultimate challenge.",
            "note": "Jake's character is essential for creating external conflict and tension."
            }}
        }}
        }},
        {{
        "chapter_number": 6,
        "title": "Training Intensifies",
        "summary": "Alex's training intensifies as the championship match approaches. Include training montages, moments of camaraderie with his friends, and growing respect from Max.",
        "characters": {{
            "Alex": {{
            "importance": "Shows his growth and dedication as a fighter.",
            "note": "Alex's hard work and progress are highlighted."
            }},
            "Max": {{
            "importance": "Continues to guide and motivate Alex.",
            "note": "Max's belief in Alex strengthens their bond."
            }},
            "Sam": {{
            "importance": "Provides comic relief and moral support.",
            "note": "Sam's loyalty and friendship are emphasized."
            }}
        }}
        }},
        {{
        "chapter_number": 7,
        "title": "The Championship Match",
        "summary": "The climax of the story where Alex faces Jake in the championship match. The fight is intense and emotional, showcasing Alex's skills and determination.",
        "characters": {{
            "Alex": {{
            "importance": "Faces his ultimate challenge and tests everything he's learned.",
            "note": "This chapter is crucial for Alex's character arc and the story's climax."
            }},
            "Jake": {{
            "importance": "Acts as the final obstacle Alex must overcome.",
            "note": "Jake's role as the antagonist reaches its peak."
            }},
            "Max": {{
            "importance": "Offers final words of wisdom and support.",
            "note": "Max's mentorship culminates in this chapter."
            }},
            "Sam": {{
            "importance": "Cheering Alex on from the sidelines, providing emotional support.",
            "note": "Sam's unwavering support is a testament to their friendship."
            }}
        }}
        }},
        {{
        "chapter_number": 8,
        "title": "Reflections and Growth",
        "summary": "Reflect on Alex's journey, win or lose, and the lessons learned. Highlight the personal growth of Alex and the impact of his journey on those around him.",
        "characters": {{
            "Alex": {{
            "importance": "Reflects on his journey and personal growth.",
            "note": "This chapter completes Alex's character arc and emphasizes the story's themes."
            }},
            "Max": {{
            "importance": "Reflects on the journey and his role as a mentor.",
            "note": "Max's satisfaction with Alex's progress is highlighted."
            }},
            "Sam": {{
            "importance": "Shares in Alex's reflections and growth.",
            "note": "Sam's friendship and support are celebrated."
            }}
        }}
        }}
    ],
    "character_notes": {{
        "importance": "The characters provided in the JSON are essential for the narrative.",
        "AI_instruction": "Introduce additional characters as needed to enrich the story and enhance character development."
    }}
    }}
    """

    result = write_chapter_chain.invoke({"user_prompt":user_prompt, "story_characteristics": story_characteristics, "chapter_plan": chapter_plan, "previous_chapter": "", "current_chapter": "1"})
    print(result)


