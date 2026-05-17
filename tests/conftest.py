from fastapi.testclient import TestClient
from src.app import app, activities
import copy
import pytest

# Keep an original deep copy of activities to restore between tests
_original_activities = copy.deepcopy(activities)

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture(autouse=True)
def reset_state():
    # Arrange: reset in-memory activities before each test
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))
