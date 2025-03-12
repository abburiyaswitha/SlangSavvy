from fastapi import FastAPI
app = FastAPI()
def slang_chatbot(user_input: str) -> str:
    return f"You said: {user_input}. Here's a slang response!"
@app.get("/chat/{user_input}")
def chat(user_input: str):
    response = slang_chatbot(user_input)
    return {"response":response}
