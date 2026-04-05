import time, random

load = 100
loading = 0

while loading <= load:
    progresso = int((loading/load)*100)
    barra = chr(9608) * loading +" " * (load - loading)

    print(f"\r[{barra}] {progresso}%    ", end="")

    loading += 1 