from unittest import TestCase, main


def exponent_factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n ** exponent_factorial(n - 1)


class Tests(TestCase):
    def test_exponent_0(self) -> None:
        self.assertEqual(exponent_factorial(0), 1)

    def test_exponent_1(self) -> None:
        self.assertEqual(exponent_factorial(1), 1)

    def test_exponent_2(self) -> None:
        self.assertEqual(exponent_factorial(2), 2)

    def test_exponent_3(self) -> None:
        self.assertEqual(exponent_factorial(3), 9)

    def test_exponent_4(self) -> None:
        self.assertEqual(exponent_factorial(4), 262144)


if __name__ == "__main__":
    main()
