from typing import List
from histr import Shabdansh
import pytest


@pytest.mark.parametrize(
    "text, splits", [("बिक्रम मेरो नाम हो", ["बि", "क्र", "म", " ", "मे", "रो", " ", "ना", "म", " ", "हो"])]
)
def test_cluster_splitting(text: str, splits: List[str]):
    text = Shabdansh(text)
    assert len(text) == len(splits)
    for char, expected_char in zip(text, splits):
        assert char == expected_char
