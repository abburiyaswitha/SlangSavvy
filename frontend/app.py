import streamlit as st
import sys
import os
import requests

# Fixing incorrect __file__ usage
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))

from slang_api import get_slang_meaning # type: ignore
from trending_api import get_trending_slang # type: ignore

# Function to handle chatbot responses
def slang_chatbot(user_input):
    slang_dict = {
        "bet": "Bet means 'okay' or 'deal'. It's used to confirm something.","sus": "Sus is short for 'suspicious', often used when something seems shady.","cap": "Cap means a lie. Saying 'no cap' means you're telling the truth.","bruh": "Bruh is a casual way of saying 'bro' or 'dude'.","goat": "GOAT stands for 'Greatest Of All Time', used for top athletes and legends.","lit": "Lit means something is exciting, fun, or amazing!","give me some trending words" : "Rizz,Delulu,Mid,Slay,No Cap,Bet,Skibidi,Gyatt,NPC,GOAT,FOMO,Flex,Yeet","give me few trending words" : "Rizz,Delulu,Mid,Slay,No Cap,Bet,Skibidi,Gyatt,NPC,GOAT,FOMO,Flex,Yeet","what is skibidi with meaning and example" : "A viral phrase from TikTok memes. - Bro, why are you always saying skibidi?","no cap" : "No lie, telling the truth. - That burger was the best I have ever had, no cap!","delulu" : "Short for delusional - Used when someone believes something unlikely. - She thinks she is dating a celebrity? That is so delulu!","rizz" : "Short for charisma refers to someone's flirting skills. - He is got mad rizz with the ladies.","slay" : "To do something amazingly well. - She slayed that outfit today!","mid" : "Something average or overrated. - That movie was mid, nothing special."
    }

    return slang_dict.get(user_input.lower(), "Sorry, I don't know that slang yet!")


# Streamlit UI
st.title("SlangSavvy - AI Slang Decoder")
menu = ["Home", "Slang Decoder", "Chatbot", "Trending Slang"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.write("Welcome to *SlangSavvy*! Decode, chat, and explore trending slang.")

elif choice == "Slang Decoder":
    st.subheader("Decode Slang Words")
    slang_input = st.text_input("Enter a slang word:")
    if st.button("Get Meaning"):
        if slang_input:
            meaning = get_slang_meaning(slang_input)
            st.write(f"**{slang_input}:** {meaning}")  # Fix incorrect formatting
        else:
            st.warning("Please enter a slang word.")

elif choice == "Chatbot":
    st.subheader("AI Slang Chatbot")
    user_input = st.text_input("Chat with AI:")
    if st.button("Send"):
        if user_input:
            response = slang_chatbot(user_input)
            st.write("🤖 AI:", response)
        else:
            st.warning("Please enter a message.")

elif choice == "Trending Slang":
    st.subheader("Trending Slang Words")
    trending = get_trending_slang()
    if trending:
        st.write("🔥 Trending Slang Words:")
        for word in trending:
            st.write(f"- {word}")
    else:
        st.write("No trending slang found.")
