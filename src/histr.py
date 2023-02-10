import unicodedata


"Class to split devnagri text in shabdansh"
# for more details refer to https://www.unicode.org/versions/Unicode11.0.0/ch12.pdf
# and https://learn.microsoft.com/en-us/typography/script-development/devanagari


class Shabdansh(str):
    VIRAMA = "\N{DEVANAGARI SIGN VIRAMA}"
    HALANT = "्"
    LEFT_MATRA = ["ि"]
    RIGHT_MATRA = ["ॉ", "ो", "ौ", "ा", "ी", "ः"]
    TOP_MATRA = ["ँ", "ं", "ॅ", "े", "ै"]
    BOTTOM_MATRA = ["़", "ु", "ू", "ृ"]
    MATRA = LEFT_MATRA + RIGHT_MATRA + TOP_MATRA + BOTTOM_MATRA
    INVALID_COMBO_RIGHT_TOP = [
        ("ॉ", "ँ"),
        ("ॉ", "ं"),
        ("ॉ", "ॅ"),
        ("ॉ", "े"),
        ("ॉ", "ै"),
        ("ो", "ँ"),
        ("ो", "ॅ"),
        ("ो", "े"),
        ("ो", "ै"),
        ("ौ", "ँ"),
        ("ौ", "ॅ"),
        ("ौ", "े"),
        ("ौ", "ै"),
        ("ा", "े"),
        ("ा", "ै"),
        ("ी", "ँ"),
        ("ी", "ॅ"),
        ("ी", "े"),
        ("ी", "ै"),
    ]
    INVALID_COMBOS = [("ं", "़"), ("ा", "ू"), ("ै", "ि")] + INVALID_COMBO_RIGHT_TOP
    HALANT_THRESHOLD_VALUE = 3

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
        """Identify if a grapheme cluster is valid or not

        Following are the rules:
            1. Cluster cannot contain both left and right matra
            2. Cluster cannot have multiple matra from in the same position, i.e. there
               can't be more than >1 matra in top, bottom, left, right position
            3. Cluster can contain top and bottom matra at the same time
            4. There has to be consonant, i.e. unicode category Mn after a halant
            5. If a halant is immediately followed by bottom matra
            6. Number of halant should always be N-1, where is the number of consonants
            7. If present ANUSVARA has to be last code point in a cluster


        Parameters
        ----------
        cluster : str
            grapheme cluster for evaluation

        Returns
        -------
        bool
            whether the grapheme cluster is valid or not
        """

        # check if the cluster invalid combo
        for matra_1, matra_2 in Shabdansh.INVALID_COMBOS:
            if matra_1 in cluster and matra_2 in cluster:
                return False

        # check if the anuswara is last code point
        if "ं" in cluster and cluster[-1] != "ं":
            return False

        # check for count based validation
        left_matra_count, right_matra_count, top_matra_count, bottom_matra_count = 0, 0, 0, 0
        halant_count = 0
        consonant_count = 0
        for idx, char in enumerate(cluster):
            if unicodedata.category(char)[0] == "L":
                consonant_count += 1
            elif char in Shabdansh.LEFT_MATRA:
                left_matra_count += 1
            elif char in Shabdansh.RIGHT_MATRA:
                right_matra_count += 1
            elif char in Shabdansh.TOP_MATRA:
                top_matra_count += 1
            elif char in Shabdansh.BOTTOM_MATRA:
                bottom_matra_count += 1
            elif char == Shabdansh.HALANT:
                halant_count += 1
                # invalid if the preceding code point was not a consonant
                if (idx > 0 and unicodedata.category(cluster[idx - 1])[0] != "L") or idx == 0:
                    return False

        # invalidated because of invalid combination of matra categories
        if left_matra_count and right_matra_count:
            return False

        # invalidated because of more than one matra from the same category
        if left_matra_count > 1:
            return False
        if right_matra_count > 1:
            return False
        if top_matra_count > 1:
            return False
        if bottom_matra_count > 1:
            return False

        if halant_count >= consonant_count or halant_count > Shabdansh.HALANT_THRESHOLD_VALUE:
            return False

        return True

    @staticmethod
    def contains_hanging_matras(cluster: str) -> bool:
        return False

    def __getitem__(self, index):
        return self.str_ls[index]

    def __len__(self):
        return len(self.str_ls)

    def __iter__(self):
        return iter(self.str_ls)
