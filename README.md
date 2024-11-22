# AgentWrite

AgentWrite is a project designed to automate the creation of structured stories using large language models (LLMs). It leverages a planning and execution framework to generate coherent narratives based on predefined characteristics and chapter plans.

## Project Structure

- **`chapter_plan.json`**: Contains the outline of the story, detailing the structure and flow of chapters.
- **`story_characteristics.json`**: Defines the attributes and elements to be included in the story, such as themes, settings, and character traits.
- **`graph.py`**: Manages the workflow, orchestrating the sequence of tasks for story generation.
- **`final_story.md`**: The output file where the generated story is compiled and saved.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/AniruthRamesh/AgentWrite.git
cd AgentWrite
```

### 2. Install Dependencies Using Poetry
Ensure you have Poetry installed. If not, install it first:
```bash
pip install poetry
```

Then, install the dependencies defined in `pyproject.toml`:
```bash
poetry install
```

### 3. Configure API Keys
If the project utilizes external APIs (e.g., OpenAI), set up your API keys as environment variables:
```bash
export OPENAI_API_KEY='your_openai_api_key'
```

### 4. Run the Story Generation Process
Execute the main script to start generating the story:
```bash
poetry run python graph.py
```

### 5. Access the Generated Story
Upon completion, the generated story will be available in the `final_story.md` file.

## Contributing

Contributions are welcome! If you have ideas, bug reports, or feature requests, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or collaboration, please reach out to the repository owner via [GitHub](https://github.com/AniruthRamesh).

---
