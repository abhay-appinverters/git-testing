# activate v-env
>>  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
>> .\.venv\Scripts\activate

# run the backend 
>> uvicorn app.main:app --reload