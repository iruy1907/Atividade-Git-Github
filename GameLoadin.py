import time, random

load = 100
loading = 0
print("\033[?25l")

while loading <= load:
    progresso = int((loading/load)*100)
    barra = chr(9608) * loading +" " * (load - loading)

    print(f"\r[{barra}] {progresso}%   ", end="")

    time.sleep(0.5)
    loading += random.randint(1,6) 

barra = chr(9608) * load
print(f"\r[{barra}] 100%{' ' * 10}")

print("\n Loading Concluido")
print("\033[?25h")