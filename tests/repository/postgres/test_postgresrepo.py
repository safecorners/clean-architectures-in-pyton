import pytest
from rentomatic.repository.postgres_objects import Room

pytestmark = pytest.mark.integration

def test_connection(pg_session):
    assert len(pg_session.query(Room).all()) == 4