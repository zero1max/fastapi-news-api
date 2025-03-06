from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from news import router as news_router

app = FastAPI()

# News Router'ni kiritish
app.include_router(news_router)

# Database ulashish
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=False,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
