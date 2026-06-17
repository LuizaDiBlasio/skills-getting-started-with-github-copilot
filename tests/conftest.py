import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_store

original_activities = copy.deepcopy(activities_store)


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activity_data():
    activities_store.clear()
    activities_store.update(copy.deepcopy(original_activities))
    yield
    activities_store.clear()
    activities_store.update(copy.deepcopy(original_activities))
