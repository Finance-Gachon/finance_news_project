from sqlalchemy.orm import Session

from . import models, schemas


def get_news(db: Session):
    return db.query(models.News_crawl).all()

print()