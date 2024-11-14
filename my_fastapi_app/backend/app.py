from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
#変更されるか確認

# 静的ファイル (auth.js) を提供する
app.mount("/frontend/static", StaticFiles(directory="../frontend/static"), name="static")

# フォームの表示 (GET)
@app.get("/", response_class=HTMLResponse)
async def get_form():
    # HTML ファイルを直接読み込んで返す
    file_path = os.path.join("..", "frontend", "templates", "index.html")
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# auth.html の表示 (GET)
@app.get("/auth", response_class=HTMLResponse)
async def auth_page():
    # auth.html を返す
    file_path = os.path.join("..", "frontend", "templates", "auth.html")
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


# quiz_add.html の表示 (GET)
@app.get("/add", response_class=HTMLResponse)
async def add_page():
    # quiz_add.html を返す
    file_path = os.path.join("..", "frontend", "templates", "quiz_add.html")
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# フォームデータの送信 (POST)

@app.post("/submit")
async def submit_form(name: str = Form(...), password: str = Form(...)):
    # データを受け取った後に index.html へリダイレクト
    return RedirectResponse(url="/", status_code=302)