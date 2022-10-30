bajtocja = {}


def dodaj_wioske(graf, wierzcholek):
    """Do mapy Bajtocji zostanie wstawiony wierzcholek"""
    if wierzcholek not in graf:
        graf[wierzcholek] = {}


def dodaj_droge(graf, krawedz):
    """Dodaje droge do mapy Bajtocji."""
    zrodlo = int(krawedz[0])
    cel = int(krawedz[1])

    dodaj_wioske(graf, zrodlo)
    dodaj_wioske(graf, cel)
    if zrodlo == cel:
        raise ValueError("Loops are not allowed in graph structures!!")

    if cel not in graf[cel]:
        graf[zrodlo].update({cel: int(krawedz[2])})

    if zrodlo not in graf[cel]:
        graf[cel].update({zrodlo: int(krawedz[2])})


file = open("./poslancy/test.txt", "r")
lines = file.readlines()
wejscie = []
for line in lines:
    wejscie.append(line.strip().split())
n = int(wejscie[0][0])
k = int(wejscie[0][1])
wejscie = wejscie[1::]
drogi = wejscie[0:n - 1]
krolewicze = []
for i in range(-1, k - 1):
    krolewicze.append(int(wejscie[n + i][0]))

for droga in drogi:
    dodaj_droge(bajtocja, droga)
print(bajtocja)
# ================================
trasa = []
suma = 0
def znajdz_droge(graph, start, cel,):
    global suma
    while 1:
        print(suma, end=" ")
        if start == cel:
            return suma
        elif start in trasa:
            break
        else:
            targets = list(graph[start].keys())
            for target in targets:
                print(target, graph[start][target], trasa)
                trasa.append(start)
                suma += graph[start][target]
                znajdz_droge(graph, target, cel)
print(znajdz_droge(bajtocja, 5, 1))
"""def poslancy(graf):
    cele = [1]
    suma = 0
    trasa = []
    for i in range(len(krolewicze)):
        start = krolewicze[i]
        for cel in cele:
            while start != cel:


poslancy(graph)"""
