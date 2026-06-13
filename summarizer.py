
from openai import OpenAI

class Summarizer:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
    
    def summarize(self, content):
        completition = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Summarize this text in 2-3 phrases: {content}"}
            ]
        )
        return completition.choices[0].message.content.strip()
