def dec_to_bin(nb_dec: int) -> str:
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)


def bin_to_dec(nb_bin: str) -> int:
    if len(nb_bin) == 1:
        if nb_bin[0] == "0":
            return 0
        else:
            return 1
    else:
        if nb_bin[-1] == "0":
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit


class TestSujet09(TestCase):
    def test_dec_to_bin(self) -> None:
        self.assertEqual(dec_to_bin(25), "11001")

    def test_dec_to_bin_one(self) -> None:
        self.assertEqual(dec_to_bin(1), "1")

    def test_dec_to_bin_byte(self) -> None:
        self.assertEqual(dec_to_bin(255), "11111111")

    def test_bin_to_dec(self) -> None:
        self.assertEqual(bin_to_dec("101010"), 42)

    def test_bin_to_dec_one(self) -> None:
        self.assertEqual(bin_to_dec("1"), 1)

    def test_bin_to_dec_byte(self) -> None:
        self.assertEqual(bin_to_dec("11111111"), 255)


if __name__ == "__main__":
    main()
