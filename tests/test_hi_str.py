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
        # invalid cases
        (1, "प्ेा्र", False),
        (2, "श्ा", False),
        (3, "मूँ्््गा", False),
        (4, "ग्रंा", False),
        (5, "श्च्ा", False),
        (6, "्ज्ञा", False),
        (7, "्अं", False),
        (8, "त्थ्ॉू", False),
        (9, "र्ुि", False),
        (10, "डं़ो", False),
        (11, "मू्गी", False),
        (12, "तेीे", False),
        (13, "त्त्", False),
        (14, "ताू", False),
        (15, "स्सोे", False),
        (16, "न्द्र्र्र्र्र्र्र्र", False),
        (17, "र्इ्श", False),
        (18, "अँ्ग", False),
        (19, "स्र्जा", False),
        (20, "मूैि", False),
        (21, "भैौ", False),
        (22, "न्नँू", False),
        # valid cases
        (101, "च्द्धा", True),
        (102, "स्दा", True),
        (103, "न्द", True),
        (104, "सिं", True),
        (105, "स्दा", True),
        (106, "मूगी", True),
        (107, "ग्रां", True),
        (108, "फ्पु", True),
        (109, "ज्ज़", True),
        (110, "स्कृ", True),
    ],
)
def test_is_valid_cluster(id: int, cluster: str, expected_result: bool):
    assert Shabdansh.is_valid_cluster(cluster) == expected_result
