def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves =  ...

    for i in range(...) :
        if notes[i] == ... :
            meilleurs_eleves.append(...)
        elif notes[i] > note_maxi:
            note_maxi = ...
            meilleurs_eleves = [...]

    return (note_maxi,meilleurs_eleves)

>>> eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
>>> notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
>>> eleves_du_mois(eleves_nsi, notes_nsi)
(80, ['c', 'f', 'h'])
>>> eleves_du_mois([],[])
(0, [])

