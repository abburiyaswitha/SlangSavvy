def get_slang_response(user_input):
    slang_dict = {
        "bet": "Bet means 'okay' or 'deal'. It's used to confirm something.",
        "sus": "Sus is short for 'suspicious', often used when something seems shady.",
        "cap": "Cap means a lie. Saying 'no cap' means you're telling the truth.",
        "bruh": "Bruh is a casual way of saying 'bro' or 'dude'.",
        "goat": "GOAT stands for 'Greatest Of All Time', used for top athletes and legends.",
        "lit": "Lit means something is exciting, fun, or amazing!",
        "swag":"Swag refers to having a cool , confident and stylish attitude"
    }

    return slang_dict.get(user_input.lower(), "Sorry, I don't know that slang yet!")
