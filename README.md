# Lg Chatbot

A basic chatbotngGraph

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

## Project Structure

```
├── src/             # Code
├── environment.yml  # Conda environment
├── setup.cfg        # Tool configurations
└── pyproject.toml   # Build configuration
```

## Development

- **Code formatting**: `autopep8 --in-place --recursive src/`
- **Linting**: `flake8 src/`

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
