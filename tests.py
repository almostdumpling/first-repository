import pytest
from main import greeting

def test_greeting():
    result = greeting('alex')
    assert result == "Hello alex"