from unittest import TestCase, main


def effectif_notes(notes_eval: list[int]) -> list[int]:
    result: list[int] = [0 for _ in range(11)]
    for v in notes_eval:
        result[v] += 1
    return result


def notes_triees(effectif_notes: list[int]) -> list[int]:
    result = []
    for i in range(len(effectif_notes)):
        result += [i] * effectif_notes[i]

    return result


def dec_to_bin(nb_dec: int) -> str:
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)


def bin_to_dec(nb_bin: str) -> int:
    # return (
    #     (2 * bin_to_dec(nb_bin[:-1]) + (nb_bin[-1] != "0"))
    #     if len(nb_bin) != 1
    #     else nb_bin[0] != "0"
    # )

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
    def test_effectif_notes(self) -> None:
        notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
        self.assertListEqual(
            effectif_notes(notes_eval), [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]
        )

    def test_notes_triees(self) -> None:
        self.assertListEqual(
            notes_triees([2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]),
            [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10],
        )

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
