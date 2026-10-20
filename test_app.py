import app as notes


def setup_function():
    notes.init_db()


def test_index():
    client = notes.app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_user_found():
    client = notes.app.test_client()
    response = client.get("/user?name=admin")
    assert response.status_code == 200
    assert response.get_json()["users"][0]["name"] == "admin"


def test_hello_escapes_html():
    client = notes.app.test_client()
    response = client.get("/hello?name=<script>")
    assert b"<script>" not in response.data
    assert b"&lt;script&gt;" in response.data