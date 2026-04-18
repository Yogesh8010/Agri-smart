import re

responses = {
    r'\b(hi|hello|hey|hii)\b': "Hello! 👋 How can I help you with farming today?",
    r'\b(best|good)\s*(crop|crops|seed)\s*(summer)\b': "🌞 In summer, maize, rice, cotton, and millet are excellent options.",
    r'\b(best|good)\s*(crop|crops|seed)\s*(winter)\b': "❄️ In winter, wheat, barley, mustard, and peas are great choices.",
    r'\b(fertilizer| खाद )\s*(wheat|gehu)\b': "🌾 Nitrogen-rich fertilizers like Urea are best for wheat.",
    r'\b(improve|better)\s*(soil|mitti)\b': "🌍 Try crop rotation, organic manure, and vermicomposting to improve soil quality.",
    r'\b(disease|pest|sick)\b': "🐛 If your plants are sick, you can use our Disease Scanner to identify the issue and get solutions!",
    r'\b(weather|rain)\b': "🌧️ Always check local weather forecasts. Adequate watering is crucial, but avoid waterlogging.",
    r'\b(bye|goodbye|cya)\b': "Goodbye! 👋 Happy farming!"
}

def get_response(user_input):
    user_input = user_input.lower()
    
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
            
    return "🤔 I'm still learning. Try asking about 'crops for summer', 'fertilizer for wheat', or 'improving soil'."
