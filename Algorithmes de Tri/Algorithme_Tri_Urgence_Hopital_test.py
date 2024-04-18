import Algorithme_Tri_Urgence_Hopital as algo;

def test_algo():
    assert algo.tri([(45, 2), (47, 1), (49, 3)]) == [(47, 1), (45, 2), (49, 3)]


def test_quitte():
    assert algo.quitte([(47, 1), (45, 2), (49, 3)]) == [(45, 2), (49, 3)]

def test_maj():
    assert algo.maj([(45, 2), (49, 3)]) == [(45, 1), (49, 2)]

def test_priorite():
    assert algo.priorite([(45, 2), (47, 1), (49, 3)], 49) == 3


def test_revise():
    assert algo.revise([(45, 2), (47, 1), (49, 3)], 49) == [(45, 3), (47, 2), (49, 1)]


