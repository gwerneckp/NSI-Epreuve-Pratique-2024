from Epreuve_Pratique import sujet_06;


def test_Exo_1():
    assert sujet_06.verifie([0, 5, 8, 8, 9]) == True
    assert sujet_06.verifie([8, 12, 4]) == False
    assert sujet_06.verifie([-1, 4]) == True
    assert sujet_06.verifie([5]) == True
    assert sujet_06.verifie([]) == True


def test_Exo_2():
    assert sujet_06.depouille([ 'A', 'B', 'A' ]) == {'A': 2, 'B': 1}
    assert sujet_06.depouille([]) == {}
    assert sujet_06.vainqueurs({'A': 3, 'B': 4, 'C': 3}) == ['B']
    assert sujet_06.vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1}) == ['A', 'B']
    
    

