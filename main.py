import os
from fastapi import FastAPI, Request
import uvicorn
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from dotenv import load_dotenv

# Load the API key from .env file, if available
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

class SimpleSummarizer:
    def __init__(self):
        # Initialize the language model using OpenAI
        self.llm = ChatOpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo")
    
    def summarize(self, text: str) -> str:
        # Creating summarize promts
        messages = [
            SystemMessage(content="You are an expert assistant with expertise in summarizing speeches"),
            HumanMessage(content=f"Please provide a short and concise summary of the following speech:\n TEXT: {text}")
        ]
        # Generating annotation
        response = self.llm(messages)
        return response.content

app = FastAPI()

@app.post("/summarize")
async def summarize(request: Request):
    # Get the text from the request
    data = await request.json()
    text = data.get("text", "")
    # Initialize the summarizer and generate the summary
    summarizer = SimpleSummarizer()
    summary = summarizer.summarize(text)
    return {"summary": summary}

if __name__ == "__main__":
    # Run app at the localhost 
    uvicorn.run(app, host="127.0.0.1", port=8000)
