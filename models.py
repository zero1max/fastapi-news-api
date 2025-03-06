from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class News(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    views = fields.IntField(default=0)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "news"

    def __str__(self):
        return self.title
    

News_Pydantic = pydantic_model_creator(News, name="News")

# DATABASE_CONFIG qo‘shish
DATABASE_CONFIG = {
    "connections": {
        "default": "sqlite://db.sqlite3",  # Yoki PostgreSQL/Mysql bog‘lanish ma’lumotlari
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],  # `aerich.models` bo‘lishi kerak!
            "default_connection": "default",
        },
    },
}
