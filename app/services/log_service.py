from datetime import datetime
from app.db.database import get_connection


def get_all_logs():
    """
    作業ログをすべて取得
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, time, task FROM logs ORDER BY id DESC")
    logs = cur.fetchall()
    conn.close()
    return logs


def add_log(task: str):
    """
    作業ログを追加
    """
    now = datetime.now().strftime("%H:%M:%S")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO logs (time, task) VALUES (?, ?)",
        (now, task)
    )
    conn.commit()
    conn.close()


def delete_log(log_id: int):
    """
    作業ログを削除
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM logs WHERE id = ?", (log_id,))
    conn.commit()
    conn.close()


def get_log_by_id(log_id: int):
    """
    ID指定で作業ログを取得
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, time, task FROM logs WHERE id = ?",
        (log_id,)
    )
    log = cur.fetchone()
    conn.close()
    return log


def update_log(log_id: int, task: str):
    """
    作業ログを更新
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE logs SET task = ? WHERE id = ?",
        (task, log_id)
    )
    conn.commit()
    conn.close()
