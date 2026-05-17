def test_root_serves_index(client):
    # Arrange: `client` fixture provides a TestClient

    # Act
    response = client.get("/")

    # Assert: redirect followed and index served
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")
