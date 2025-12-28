from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import sqlite3

app = FastAPI()
templates = Jinja2Templates(directory="templates")

DB_NAME = "worklog.db"


# ============================
# DB 初期化
# ============================
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT NOT NULL,
            task TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


init_db()


# ============================
# 一覧表示
# ============================
@app.get("/", response_class=HTMLResponse)
def show_page(request: Request):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, time, task FROM logs ORDER BY id DESC")
    logs = cur.fetchall()
    conn.close()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "logs": logs
        }
    )


# ============================
# 追加処理
# ============================
@app.post("/add")
def add_log(task: str = Form(...)):
    now = datetime.now().strftime("%H:%M:%S")

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO logs (time, task) VALUES (?, ?)",
        (now, task)
    )
    conn.commit()
    conn.close()

    return RedirectResponse(url="/", status_code=303)


# ============================
# 削除処理
# ============================
@app.post("/delete")
def delete_log(log_id: int = Form(...)):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM logs WHERE id = ?", (log_id,))
    conn.commit()
    conn.close()

    return RedirectResponse(url="/", status_code=303)


# ============================
# 詳細画面
# ============================
@app.get("/detail/{log_id}", response_class=HTMLResponse)
def show_detail(request: Request, log_id: int):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "SELECT id, time, task FROM logs WHERE id = ?",
        (log_id,)
    )
    log = cur.fetchone()
    conn.close()

    return templates.TemplateResponse(
        "detail.html",
        {
            "request": request,
            "log": log
        }
    )
