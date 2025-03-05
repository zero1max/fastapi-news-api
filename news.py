from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from .models import News

router = APIRouter()

class NewsCreateSchema(BaseModel):
    title: str
    content: str

# Faqat adminlar qo‘sha olishi uchun (hozircha oddiy funksiya)
def get_admin():
    return True  # Bu yerda real autentifikatsiya bo‘lishi kerak

@router.post("/admin/news")
async def create_news(news: NewsCreateSchema, admin: bool = Depends(get_admin)):
    if not admin:
        raise HTTPException(status_code=403, detail="Sizga ruxsat yo'q")
    
    news_obj = await News.create(**news.dict())
    return {"message": "News qo'shildi", "id": news_obj.id}

@router.get("/news")
async def get_all_news():
    news_list = await News.all().order_by("-created_at")
    return news_list

@router.get("/news/{news_id}")
async def get_news(news_id: int):
    news = await News.get_or_none(id=news_id)
    if not news:
        raise HTTPException(status_code=404, detail="News topilmadi")
    
    news.views += 1  # Ko‘rishlar sonini oshirish
    await news.save()
    
    return {"title": news.title, "content": news.content, "views": news.views}

@router.delete("/admin/news/{news_id}")
async def delete_news(news_id: int, admin: bool = Depends(get_admin)):
    if not admin:
        raise HTTPException(status_code=403, detail="Sizga ruxsat yo'q")

    news = await News.get_or_none(id=news_id)
    if not news:
        raise HTTPException(status_code=404, detail="News topilmadi")

    await news.delete()
    return {"message": "News o'chirildi"}
