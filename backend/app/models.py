from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base

class News_crawl(Base):
    __tablename__ = "news_crawl"

    search_word = Column(String)
    title = Column(String)
    originallink = Column(String, primary_key=True)
    link = Column(String)
    description = Column(String)
    pub_date = Column(Date)
    context = Column(String)
    