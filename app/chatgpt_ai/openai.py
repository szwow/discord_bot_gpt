from dotenv import load_dotenv
import openai
import os
import time

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')
model = "text-davinci-003"
temperature = 1
max_tokens = 1050
cache = {}

def chatgpt_response(prompt):
    if prompt in cache:
        return cache[prompt]
    
    try:
        start_time = time.time()
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        response_text = response.choices[0].text.strip()
        cache[prompt] = response_text
        end_time = time.time()
        print(f'Response time: {end_time - start_time:.2f}s')
        return response_text
    except Exception as e:
        print(f'Error: {str(e)}')
        return 'Sorry, I couldn\'t understand your message. Please try again.'