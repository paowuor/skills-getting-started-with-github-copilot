from src.app import activities


def test_signup_success_and_duplicate(client):
    # Arrange
    activity = "Chess Club"
    new_email = "newstudent@mergington.edu"

    # Act: first signup should succeed
    response = client.post(f"/activities/{activity}/signup", params={"email": new_email})

    # Assert
    assert response.status_code == 200
    assert new_email in activities[activity]["participants"]

    # Act: duplicate signup should fail
    dup_resp = client.post(f"/activities/{activity}/signup", params={"email": new_email})

    # Assert duplicate rejected
    assert dup_resp.status_code == 400


def test_signup_nonexistent_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent"
    email = "someone@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
