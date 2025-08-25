responses = {
    "hii": "Hello! 👋 How can I help you with farming today?",
    "hello": "Hi there! 🌱 You can ask me about crops, soil, or fertilizers.",
    "best crop in summer": "🌞 In summer, maize, rice, and millet are good options.",
    "fertilizer for wheat": "🌾 Nitrogen-rich fertilizers like Urea are best for wheat.",
    "improve soil": "🌍 Try crop rotation, organic manure, and vermicomposting.",
    "bye": "Goodbye! 👋 Happy farming!"   
}

def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "🤔 I'm still learning. Please consult an expert farmer for detailed advice.")
