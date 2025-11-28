Activate virtual environment:
>> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
>> .\.venv\Scripts\activate

Deactivate virtual environment:
>> deactivate

Install all dependencies:
>> uv sync

Set up pre-commit hooks:
>> pre-commit clean
>> pre-commit install

Run the backend:
>> uvicorn app.main:app --reload

Note: If "black" fails, your code needs formatting:
>> uv run black app
