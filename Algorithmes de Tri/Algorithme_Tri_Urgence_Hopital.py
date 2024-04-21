# Fonction tri selection
attente = [(45, 2), (47, 1), (49, 3)]

def tri(attente):
    for i in range(len(attente)):
        pos = i
        mini = attente[i][1]
        for j in range(i, len(attente)):
            if attente[j][1] < mini:
                pos = j
                mini = attente[j][1]
        temp = attente[i]
        attente[i] = attente[pos]
        attente[pos] = temp
        return attente


def quitte(attente):
    return [...]

def maj(attente):
    ...
    return ...

def priorite(attente, p):
    ...
    return ...


def revise(attente, p):
    nouvelle = []
    n = priorite(attente, p)
    for (patient, prio) in attente:
        if patient == p:
            nouvelle.append(...)
        elif ...:
            nouvelle.append((patient, prio + 1))
        else:
            nouvelle.append((patient, prio))
    return nouvelle
