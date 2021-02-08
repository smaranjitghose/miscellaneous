# Python Project Structure

A modified cookie-cutter like project structure I prefer to use for my projects

```python

|- .git/ # Contains Git's files and snapshots
|- .github/
    |- workflows/ # GitHub Actions
        |- black.yml # GitHub action configuration for running black on push and pull requests
|- .gitignore   # Contains the list of files and directories generated locally that should not be staged
|- README.MD # Description of the project
|- LICENSE # Code Distribution LICENSE
|- CODE_OF_CONDUCT.MD # Guidelines for Community Interactions
|- Contributing.MD # Guidelines for Contributing to the project
|- .pre-commit-config.yaml # Contains the configuration setup for pre-commit hooks (Command: pre-commit install)
|- pyproject.toml # Contains the necessary configuration information to setup a modern python project/package (including configs for formatting tools like i-sort and black)
|- requirements.txt # list of all python packages needed to be installed (sorted in alphabetical order)
|- assets/ # All the images, gifs go here
|- src/ # All the scripts go here
|- tests/ # All tests go here
|- notebooks/ # All the Jupyter notebooks go here
|- app.py # Streamlit app script
|- api.py # FastAPI script
|- Dockerfile # Docker Container Configuration
|- .dockerignore # Ignore a list of files and directories while building the docker container
|- Procfile # Setup file for Heroku
|- .slugignore # Ignore a list of files and directories while building the Heroku dyno
```

# Files provided:

#### Heroku

- [.slugignore](./.slugignore)
- [Procfile](./Procfile)
- [setup.sh](./setup.sh)

#### Docker

- [Dockerfile](./Dockerfile)
- [.dockerignore](./.dockerignore)

#### GitHub Actions

- [Black YML](./.git/workflows/black.yml)

#### Python Project Setup

- [pyproject.toml](./pyproject.toml)
- [requirements.txt](./requirements.txt)

#### GitIgnore

- [.gitignore](./.gitignore)
