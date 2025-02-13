# Backend

## One Time Setup

- Ensure you are using Python 3.12, as 3.13 is not supported on certain ML platforms. You can use a tool like [pyenv](https://github.com/pyenv/pyenv) to switch your python version. 
- Create a virtual environment with `python3 -m venv .env`, and activate it. If you use a different name for your env, add it to `.gitignore`
  - MacOS: `source .env/bin/activate`
  - Windows: `.\venv\Scripts\activate`
- Install dependencies with `pip install -r requirements.txt`
- Run the backend with `flask -A app run`

## Development

- If you add another package, be sure to perform `pip freeze > requirements.txt` to update dependencies