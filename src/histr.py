import unicodedata

"Class to split devnagri text in shabdansh"


class Shabdansh(str):
    VIRAMA = "\N{DEVANAGARI SIGN VIRAMA}"
    HALLANK = "्"
    LEFT_MATRA = ["ि"]
    RIGHT_MATRA = ["ॉ", "ो", "ौ", "ा", "ी", "ः"]
    TOP_MATRA = ["ँ", "ं", "ॅ", "े", "ै"]
    BOTTOM_MATRA = ["़", "ु", "ू", "ृ"]

    def __init__(self, devnagari_text: str):
        self.str = devnagari_text
        self.str_ls = list(self.splitclusters(self.str))

    @staticmethod
    def splitclusters(devnagari_text: str):
        """Generate the grapheme clusters for the strings.

        E.g.

        "बिक्रम मेरो नाम हो" => ['बि', 'क्र', 'म', ' ', 'मे', 'रो', ' ', 'ना', 'म', ' ', 'हो']

        ref: https://stackoverflow.com/questions/6805311/combining-devanagari-characters
        """

        cluster = ""
        last = None
        for char in devnagari_text:
            category = unicodedata.category(char)[0]
            if category == "M" or category == "L" and last == Shabdansh.VIRAMA:
                cluster += char
            else:
                if cluster:
                    yield cluster
                cluster = char
            last = char
        if cluster:
            yield cluster

    @staticmethod
    def is_valid_cluster(cluster: str) -> bool:
        left_matra_count, right_matra_count, top_matra_count, bottom_matra_count = 0, 0, 0, 0
        for char in cluster:
            if char in Shabdansh.LEFT_MATRA:
                left_matra_count += 1
            elif char in Shabdansh.RIGHT_MATRA:
                right_matra_count += 1
            elif char in Shabdansh.TOP_MATRA:
                top_matra_count += 1
            elif char in Shabdansh.BOTTOM_MATRA:
                bottom_matra_count += 1
        if left_matra_count and right_matra_count:
            return False
        if left_matra_count > 1:
            return False
        if right_matra_count > 1:
            return False
        if top_matra_count > 1:
            return False
        if bottom_matra_count > 1:
            return False

        return True

    def __getitem__(self, index):
        return self.str_ls[index]

    def __len__(self):
        return len(self.str_ls)

    def __iter__(self):
        return iter(self.str_ls)
