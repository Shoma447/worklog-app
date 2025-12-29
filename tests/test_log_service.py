import app.services.log_service as log_service


class DummyCursor:
    def __init__(self):
        self.executed = []

    def execute(self, query, params=None):
        self.executed.append((query, params))

    def fetchall(self):
        return [(1, "12:00:00", "dummy")]

    def fetchone(self):
        return (1, "12:00:00", "dummy")


class DummyConnection:
    def __init__(self, cursor: DummyCursor):
        self._cursor = cursor
        self.committed = False
        self.closed = False

    def cursor(self):
        return self._cursor

    def commit(self):
        self.committed = True

    def close(self):
        self.closed = True


def test_get_all_logs_executes_select(monkeypatch):
    cursor = DummyCursor()
    conn = DummyConnection(cursor)

    def fake_get_connection():
        return conn

    monkeypatch.setattr(log_service, "get_connection", fake_get_connection)

    logs = log_service.get_all_logs()

    assert logs == [(1, "12:00:00", "dummy")]
    assert cursor.executed[0][0] == "SELECT id, time, task FROM logs ORDER BY id DESC"
    assert conn.closed is True


def test_add_log_executes_insert_and_commit(monkeypatch):
    cursor = DummyCursor()
    conn = DummyConnection(cursor)

    def fake_get_connection():
        return conn

    monkeypatch.setattr(log_service, "get_connection", fake_get_connection)

    log_service.add_log("test task")

    query, params = cursor.executed[0]
    assert query == "INSERT INTO logs (time, task) VALUES (?, ?)"
    assert params[1] == "test task"  # params[0] は時刻なので固定しない
    assert conn.committed is True
    assert conn.closed is True


def test_delete_log_executes_delete(monkeypatch):
    cursor = DummyCursor()
    conn = DummyConnection(cursor)

    def fake_get_connection():
        return conn

    monkeypatch.setattr(log_service, "get_connection", fake_get_connection)

    log_service.delete_log(123)

    query, params = cursor.executed[0]
    assert query == "DELETE FROM logs WHERE id = ?"
    assert params == (123,)
    assert conn.committed is True
    assert conn.closed is True


def test_get_log_by_id_executes_select_where(monkeypatch):
    cursor = DummyCursor()
    conn = DummyConnection(cursor)

    def fake_get_connection():
        return conn

    monkeypatch.setattr(log_service, "get_connection", fake_get_connection)

    log = log_service.get_log_by_id(5)

    assert log == (1, "12:00:00", "dummy")
    query, params = cursor.executed[0]
    assert query == "SELECT id, time, task FROM logs WHERE id = ?"
    assert params == (5,)
    assert conn.closed is True


def test_update_log_executes_update(monkeypatch):
    cursor = DummyCursor()
    conn = DummyConnection(cursor)

    def fake_get_connection():
        return conn

    monkeypatch.setattr(log_service, "get_connection", fake_get_connection)

    log_service.update_log(7, "updated")

    query, params = cursor.executed[0]
    assert query == "UPDATE logs SET task = ? WHERE id = ?"
    assert params == ("updated", 7)
    assert conn.committed is True
    assert conn.closed is True
