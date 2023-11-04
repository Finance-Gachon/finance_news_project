from datetime import datetime
from typing import Union

from pydantic import BaseModel

class News_crwalBase(BaseModel):
    search_word: str
    title: str


class PerfCreate(News_crwalBase):
    pass


class News_crwal(News_crwalBase):
    class Config:
        orm_mode = True
