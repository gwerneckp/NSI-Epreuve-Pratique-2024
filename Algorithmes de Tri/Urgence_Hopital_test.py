import Urgence_Hopital as algo;

attente_variable = [(45, 2), (47, 1), (49, 3)]

def test_variable_value():
    assert algo.attente_variable == [(45, 2), (47, 1), (49, 3), (50, 4)]

def test_tri():
    assert algo.tri([(45, 2), (47, 1), (49, 3)]) == [(47, 1), (45, 2), (49, 3)]

def test_quitte():
    assert algo.quitte([(47, 1), (45, 2), (49, 3)]) == [(45, 2), (49, 3)]

def test_maj():
    assert algo.maj([(45, 2), (49, 3)]) == [(45, 1), (49, 2)]

def test_priorite():
    assert algo.priorite([(45, 2), (47, 1), (49, 3)], 49) == 3


def test_revise():
    assert algo.revise([(45, 2), (47, 1), (49, 3)], 49) == [(45, 3), (47, 2), (49, 1)]


