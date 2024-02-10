from fastapi import FastAPI, HTTPException  #HTTPExceptionはHTTPステータスコードを伴うエラーを返すために使用
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel): #BaseModelを継承することでItemクラスのインスタンスがPydanticによって自動的にバリデーション
    name: str
    nickname: Optional[str] = None

@app.post("/nickname")
def search_nickname(item: Item):
    if item.nickname is not None:
        return {"result": f"「{item.name}」さんのあだ名は「{item.nickname}」です。"}
    else:
        return {"error": f"「{item.name}」さんはまだあだ名が無いのでつけてあげて下さい。"}
