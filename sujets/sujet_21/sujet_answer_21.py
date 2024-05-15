from unittest import TestCase, main


def recherche_motif(motif: str, texte: str) -> list[int]:
    res = []
    for i in range(len(texte) - len(motif) + 1):
        if texte[i : i + len(motif)] == motif:
            res.append(i)
    return res


def parcours(adj: list[list[int]], x: int, acc: list[int]) -> None:
    """Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc"""
    if x not in acc:
        acc.append(x)
        for y in adj[x]:
            parcours(adj, y, acc)


def accessibles(adj: list[list[int]], x: int) -> list[int]:
    """Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x."""
    acc: list[int] = []
    parcours(adj, x, acc)
    return acc


# Votre code ici
class TestSujet21(TestCase):
    def test_recherche_motif_empty_text(self) -> None:
        self.assertEqual(recherche_motif("ab", ""), [])

    def test_recherche_motif_no_occurrence(self) -> None:
        self.assertEqual(recherche_motif("ab", "cdcdcdcd"), [])

    def test_recherche_motif_single_occurrence(self) -> None:
        self.assertEqual(recherche_motif("ab", "abracadabra"), [0, 7])

    def test_recherche_motif_multiple_occurrences(self) -> None:
        self.assertEqual(recherche_motif("ab", "abracadabraab"), [0, 7, 11])

    def test_accessibles_start_zero(self) -> None:
        self.assertEqual(
            accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0), [0, 1, 2, 3]
        )

    def test_accessibles_start_four(self) -> None:
        self.assertEqual(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4), [4, 5])


if __name__ == "__main__":
    main()
