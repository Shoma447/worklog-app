from fastapi.testclient import TestClient

from app.main import app
import app.routers.logs as logs_router

client = TestClient(app)


def test_get_index_page(monkeypatch):
    """
    GET / が正常に表示されるか
    """

    def fake_get_all_logs():
        return [(1, "12:00:00", "test task")]

    # ★ service ではなく router 側を patch する
    monkeypatch.setattr(logs_router, "get_all_logs", fake_get_all_logs)

    response = client.get("/")

    assert response.status_code == 200
    assert "test task" in response.text


def test_add_log_redirect(monkeypatch):
    """
    POST /add が 303 リダイレクトされるか
    """

    def fake_add_log(task: str):
        assert task == "new task"

    # ★ router 側を patch
    monkeypatch.setattr(logs_router, "add_log", fake_add_log)

    response = client.post(
        "/add",
        data={"task": "new task"},
        follow_redirects=False  # ★ allow_redirects → follow_redirects
    )

    assert response.status_code == 303
    assert response.headers["location"] == "/"


def test_detail_page(monkeypatch):
    """
    GET /detail/{id} が正常に表示されるか
    """

    def fake_get_log_by_id(log_id: int):
        assert log_id == 1
        return (1, "12:00:00", "detail task")

    # ★ router 側を patch
    monkeypatch.setattr(logs_router, "get_log_by_id", fake_get_log_by_id)

    response = client.get("/detail/1")

    assert response.status_code == 200
    assert "detail task" in response.text
