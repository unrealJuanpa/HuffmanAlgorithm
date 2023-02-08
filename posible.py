import numpy as np

freq = {'E': 16, 'D': 13, 'J': 11, 'M': 10, 'K': 3}

auxf, auxl = [list(freq.values())], [list(freq.keys())]


def sortf():
    global auxf, auxl
    idx = np.array(auxf[-1]).argsort()[::-1]
    auxf[-1] = list(np.array(auxf[-1])[idx])
    auxl[-1] = list(np.array(auxl[-1])[idx])

    for i in range(len(auxf[-1])-1):
        actual, futuro = auxl[-1][i], auxl[-1][i+1]
        if len(actual) > len(futuro) and auxf[-1][i] == auxf[-1][i+1]:
            auxl[-1][i], auxl[-1][i+1] = futuro, actual


while len(auxf[-1]) > 2:
    sortf()
    a1, a2 = auxf[-1][:-2], auxl[-1][:-2]
    a1.append(auxf[-1][-1] + auxf[-1][-2])
    a2.append(f"{auxl[-1][-2]},{auxl[-1][-1]}")
    auxf.append(a1)
    auxl.append(a2)
sortf()

print(auxl)
input(auxf)
