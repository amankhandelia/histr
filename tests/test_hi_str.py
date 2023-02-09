from typing import List
from src.histr import Shabdansh
import pytest


@pytest.mark.parametrize(
    "id, text, splits",
    [
        (1, "बिक्रम मेरो नाम हो", ["बि", "क्र", "म", " ", "मे", "रो", " ", "ना", "म", " ", "हो"]),
        (2, "रानीकंुँवर", ["रा", "नी", "कंुँ", "व", "र"]),
        (3, "अंंंंंंंंंंंंंंंंंंंंगद", ["अंंंंंंंंंंंंंंंंंंंं", "ग", "द"]),
        (4, "अंंिकत", ["अंंि", "क", "त"]),
        (5, "अंबंुज", ["अं", "बंु", "ज"]),
        (6, "अंिहवरनसिं", ["अंि", "ह", "व", "र", "न", "सिं"]),
        (7, "अंोंकारचन्द", ["अंों", "का", "र", "च", "न्द"]),
        (8, "लीलावतेीे", ["ली", "ला", "व", "तेीे"]),
        (9, "लुख्ुड", ["लु", "ख्ु", "ड"]),
        (10, "लीलांिसह", ["ली", "लांि", "स", "ह"]),
        (11, "राजदत्त्", ["रा", "ज", "द", "त्त्"]),
        (12, "मू्गी", ["मू्गी"]),
        (13, "पू्जी", ["पू्जी"]),
    ],
)
def test_cluster_splitting(id: int, text: str, splits: List[str]):
    text = Shabdansh(text)
    assert text.str_ls == splits


@pytest.mark.parametrize(
    "id, cluster, expected_result",
    [
        (1, "प्ेा्र", True),
        (2, "श्ा", True),
        (3, "मूँ्््गा", True),
        (4, "ग्रंा", True),
        (5, "श्च्ा", True),
        (6, "्ज्ञा", True),
        (7, "्अं", True),
        (8, "त्थ्ॉू", True),
        (9, "र्ुि", True),
        (10, "डं़ो", True),
        (11, "च्द्धा", False),
        (12, "स्दा", False),
    ],
)
def test_contains_hanging_matra(id: int, cluster: str, expected_result: bool):
    assert False
