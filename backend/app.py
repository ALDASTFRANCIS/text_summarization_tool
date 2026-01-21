from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
from newspaper import Article
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace specific Extension ID
    allow_methods=["*"],
    allow_headers=["*"],
)


print("Loading model... this takes a minute...")
summarizer = pipeline("summarization", model="t5-small") 


class ArticleRequest(BaseModel):
    url: str


@app.post("/summarize")
async def summarize_article(request: ArticleRequest):
    try:
        
        article = Article(request.url)
        article.download()
        article.parse()
        
        text = article.text
        if len(text) < 100:
            return {"summary": "Article too short to summarize."}


        summary_list = summarizer(text, max_length=60, min_length=10, do_sample=False)
        summary_text = summary_list[0]['summary_text']
        
        return {"summary": summary_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run this: uvicorn server:app --reload