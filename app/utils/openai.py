import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def get_openai(prompt):
#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     messages  = [ {"role": "system", "content": prompt } ]
#     chat = openai.ChatCompletion.create(
#             model="gpt-4o-mini", messages=messages
#     ) 
#     return chat.choices[0].message.content
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def get_gemini(prompt):
    # Set up the API key
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    
    # Create the model
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    # Generate content
    response = model.generate_content(prompt)
    
    # Return the response text
    return response.text
