from stef.base import TestBase, TestType

class Test(TestBase):
    def __init__(self):
        super().__init__("zettel03", TestType.shown)
        self.testgroups = [
            {"name": "nrz", "function": self.test_nrz},
            {"name": "nrzi", "function": self.test_nrzi},
            {"name": "4b5b", "function": self.test_4b5b},
            {"name": "mixed", "function": self.test_mixed}
        ]

    def test_nrz(self):
        self.test(["nrz", "01011000"], [], [["X"]], 1)
        self.test(["nrz", "01001011010010010101011001010011"], [], [["KIVS"]], 2)

    def test_nrzi(self):
        self.test(["differential", "01101110"], [], [["Y"]], 1)
        self.test(["differential", "01110010011100011001101110011101"], [], [["KIVS"]], 2)

    def test_4b5b(self):
        self.test(["4b5b", "0101110110"], [], [["Z"]], 1)
        self.test(["4b5b", "0101010111010101001101011011100101110101"], [], [["KIVS"]], 2)

    def test_mixed(self):
        self.test(["mixed_decode", "01000001011111000111110101000100"], [], [["ABCD"]], 3)
        sahne = "010111010101111110011100000100111001111001011001110111010101011101000110011101111001"
        self.test(["mixed_decode", sahne], [], [["SAHNETORTE"]], 3)
