from pydantic import BaseModel
from typing import Optional


class ArticleModel(BaseModel):
    source: Optional[str] = None
    text: Optional[str] = None
    name: Optional[str] = None
    crawling_time: Optional[int] = None
    translated_text: Optional[str] = None