from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slang_api import get_slang_meaning
from chatbot_api import slang_chatbot
from trending_api import get_trending_slang
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message": "Welcome to SlangSavvy Backend!"}

@app.get("/decode")
def decode_slang(word: str):
    """Fetch meaning of a slang word."""
    meaning = get_slang_meaning(word)
    return {"word": word, "meaning": meaning}

@app.get("/chat")
def chat_slang(message: str):
    """AI chatbot to explain slang terms."""
    response = slang_chatbot(message)
    return {"response": response}

@app.get("/trending")
def trending_slang():
    """Fetch trending slang terms."""
    return {"trending": get_trending_slang()}
