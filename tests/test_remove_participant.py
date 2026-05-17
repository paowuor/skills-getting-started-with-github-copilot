from src.app import activities


def test_remove_existing_participant_success(client):
    # Arrange
    activity = "Chess Club"
    existing = "michael@mergington.edu"
    assert existing in activities[activity]["participants"]

    # Act
    response = client.delete(f"/activities/{activity}/participants", params={"email": existing})

    # Assert
    assert response.status_code == 200
    assert existing not in activities[activity]["participants"]


def test_remove_nonexistent_participant_returns_404(client):
    # Arrange
    activity = "Chess Club"
    missing = "notfound@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants", params={"email": missing})

    # Assert
    assert response.status_code == 404


def test_remove_from_nonexistent_activity_returns_404(client):
    # Arrange
    activity = "NoSuchActivity"
    email = "someone@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert response.status_code == 404
