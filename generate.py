import google.generativeai as genai
import os

def generate_answer(prompt):
    # Access the Google API key from the loaded environment variables
    API_KEY = os.getenv("GOOGLE_API_KEY")

    # Configure the generative AI client with the API key
    genai.configure(api_key=API_KEY)

    # define the google gemini model
    model = genai.GenerativeModel('gemini-pro')

    answer = model.generate_content(prompt)
    return answer.text