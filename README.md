# LangGraph CLI Chatbot

A CLI chatbot built using LangGraph with OpenAI GPT-4.1-nano and Tavily search integration.

## Features

- **LangGraph State Management**: Uses StateGraph for conversation flow
- **Tool Integration**: Tavily search for real-time information retrieval
- **OpenAI Integration**: Powered by GPT-4.1-nano model
- **Interactive CLI**: Simple command-line interface for chatting

## Prerequisites

- Python 3.8+
- Conda package manager
- OpenAI API key
- Tavily API key

## Quick Start

1. **Clone the repository**:

   - **with https:**

   ```bash
   git clone https://github.com/maxitect/lg-chatbot.git
   cd lg-chatbot
   ```

   - **with ssh:**

   ```bash
   git clone git@github.com:maxitect/lg-chatbot.git
   cd lg-chatbot
   ```

2. **Setup environment**

   ```bash
   conda env create -f environment.yml
   conda activate lg-chatbot
   ```

3. **Configure API keys**

   Create a `.env` file in the root directory:

   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

4. **Run the chatbot**

   ```bash
   python src/main.py
   ```

   Type your messages and press Enter. Use `quit`, `exit`, or `q` to stop.

## Project Structure

```
├── src/
│   ├── __init__.py       # Package initialisation
│   ├── main.py          # CLI entry point
│   ├── graph.py         # LangGraph state graph definition
│   ├── models.py        # State models and type definitions
│   ├── nodes.py         # Graph nodes (chatbot, tool integration)
│   └── tools.py         # Tool definitions (Tavily search)
├── environment.yml      # Conda environment
├── setup.cfg           # Tool configurations
├── pyproject.toml      # Build configuration
└── .env                # API keys (create this file)
```

## Architecture

The chatbot uses a **StateGraph** with two main nodes:

- **Chatbot Node**: Processes messages using OpenAI's GPT-4.1-nano
- **Tools Node**: Handles tool calls (currently Tavily search)

The graph automatically routes between nodes based on whether the LLM decides to use tools.

## Development

- **Code formatting**: `autopep8 --in-place --recursive src/`
- **Linting**: `flake8 src/`
- **View graph structure**: The ASCII representation prints when running the application

## Configuration

### Model Configuration

- Current model: `openai:gpt-4.1-nano`
- Tools: Tavily search (max 2 results)

### Code Standards

- Line length: 160 characters
- PEP 8 compliance with autopep8
- Flake8 linting enabled

## Git Branch Naming

Follow these conventions:

- `feature/feature-name` - New features
- `bugfix/bug-description` - Bug fixes
- `hotfix/critical-fix` - Critical fixes
- `chore/task-description` - Maintenance tasks
- `docs/documentation-update` - Documentation changes

## Commit Messages

Use conventional commits:

- `feat: add new feature`
- `fix: resolve bug`
- `docs: update documentation`
- `style: format code`
- `refactor: restructure code`
- `test: add tests`
- `chore: update dependencies`

## Author

[**maxitect**](https://github.com/maxitect) - maxime.downe@gmail.com
