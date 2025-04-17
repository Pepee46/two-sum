from typing import List

def twosum(numeros: List[int], objetivo: int):
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] + numeros[j] == objetivo:
                return [i, j]