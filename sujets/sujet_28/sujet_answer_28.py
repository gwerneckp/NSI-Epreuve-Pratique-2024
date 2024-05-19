from unittest import TestCase, main


def fibonacci(n: int) -> int:
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b

    return b


def eleves_du_mois(eleves: list[str], notes: list[int]) -> tuple[int, list[str]]:
    note_maxi = 0
    meilleurs_eleves: list[str] = []

    for i in range(len(eleves)):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi, meilleurs_eleves)


class TestSujet28(TestCase):
    def test_fibonacci_case_1(self) -> None:
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_case_2(self) -> None:
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_case_3(self) -> None:
        self.assertEqual(fibonacci(25), 75025)

    def test_eleves_du_mois_case_1(self) -> None:
        eleves_nsi = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
        self.assertTupleEqual(
            eleves_du_mois(eleves_nsi, notes_nsi), (80, ["c", "f", "h"])
        )

    def test_eleves_du_mois_case_empty(self) -> None:
        self.assertTupleEqual(eleves_du_mois([], []), (0, []))


if __name__ == "__main__":
    main()
