from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services.log_service import (
    get_all_logs,
    add_log,
    delete_log,
    get_log_by_id,
    update_log
)

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# ============================
# 一覧表示
# ============================
@router.get("/", response_class=HTMLResponse)
def show_page(request: Request):
    logs = get_all_logs()

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
@router.post("/add")
def add_log_route(task: str = Form(...)):
    add_log(task)
    return RedirectResponse(url="/", status_code=303)


# ============================
# 削除処理
# ============================
@router.post("/delete")
def delete_log_route(log_id: int = Form(...)):
    delete_log(log_id)
    return RedirectResponse(url="/", status_code=303)


# ============================
# 詳細画面
# ============================
@router.get("/detail/{log_id}", response_class=HTMLResponse)
def show_detail(request: Request, log_id: int):
    log = get_log_by_id(log_id)

    return templates.TemplateResponse(
        "detail.html",
        {
            "request": request,
            "log": log
        }
    )


# ============================
# 編集画面表示
# ============================
@router.get("/edit/{log_id}", response_class=HTMLResponse)
def show_edit(request: Request, log_id: int):
    log = get_log_by_id(log_id)

    return templates.TemplateResponse(
        "edit.html",
        {
            "request": request,
            "log": log
        }
    )


# ============================
# 更新処理
# ============================
@router.post("/edit")
def update_log_route(log_id: int = Form(...), task: str = Form(...)):
    update_log(log_id, task)
    return RedirectResponse(url="/", status_code=303)
