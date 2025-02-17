import pytest
from main import count
def test_count_happy_path():
    assert count([]) == {}
    assert count(["aldo", "giovanni", "giacomo","aldo"]) == {"aldo":2, "giovanni":1, "giacomo":1}

def test_count_unhappy_path():
    with pytest.raises(TypeError):
        assert count(None)