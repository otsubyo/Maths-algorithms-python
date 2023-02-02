from queue import PriorityQueue
from math import *
import random as rd
import networkx as nx
import matplotlib.pyplot as plt

def genererGraphe(taille,a=1,b=100) :
    graphe = []
    for i in range(taille) :
        liste = []
        graphe.append(liste)
        for y in range(taille):
            graphe[i].append(inf)
    for i in range(taille) :
        for y in range(taille) :
            if (i != y) :#on manipule la chance pour qu'il y ai un peut plus de 0
                if (rd.randint(0,1) == 0) :
                    graphe[i][y] = inf
                else :
                    graphe[i][y] = rd.randint(a,b)
    return graphe
def djikstra1(graph, S , A): 
    file = [(0, S, [S])]
    while file: #on teste si le file est vide
        (poid, a, chemin) = sorted(file)[0]  #on prend le premier sommet du file
        for next in graph[a] - set(chemin):  #on parcours les voisins de a
            if next == A: #si le voisin est A
                yield (poid, chemin + [next]) #on retourne le chemin
            else: #sinon
                file.append((poid + 1, next, chemin + [next])) #on ajoute le voisin a la file
        file.pop(0) #on supprime le premier element du file
    return file #on retourne le file

def dijkstra(graph, debut, taille):
    D = {v:float('inf') for v in range(taille)}
    D[debut] = 0
    visite = []
    pq = PriorityQueue()
    pq.put((0, debut))

    while not pq.empty():
        (dist, point) = pq.get()
        visite.append(point)

        for voisin in range(taille):
            if graph[point][voisin] != inf:
                distance = graph[point][voisin]
                if voisin not in visite:
                    ancien_poids = D[voisin]
                    nv_poids = D[point] + distance
                    if nv_poids < ancien_poids:
                        pq.put((nv_poids, voisin))
                        D[voisin] = nv_poids

    for i in range(taille) :
        if D[i] == inf :
            D[i] = 'sommet non joignable'

    return D

def BelmanFord(graph, debut, taille) :
    D = {v:float('inf') for v in range(taille)}
    D[debut] = 0
    for i in range(taille) :
        for y in range(taille) :
            if (graph[i][y] != inf) :
                if (D[i] + graph[i][y] < D[y]) :
                    D[y] = D[i] + graph[i][y]
    for i in range(taille) :
        if D[i] == inf :
            D[i] = 'sommet non joignable'
    return D


taille = 8
point = 0
g = genererGraphe(taille,1,100)

print("Notre Graphe :")
print(g)
print('')
print("liste des distance entre le sommet ", point, " et tout les autres sommet :")
print(dijkstra(g, point, taille))

print('')
print('')


taille = 3
point = 0
g = [[inf,1,inf],[1,inf,inf],[2,3,inf]]

print("Notre Graphe :")
print(g)
print('')
print("liste des distance entre le sommet ", point, " et tout les autres sommet :")
print(dijkstra(g, point, taille))
print(BelmanFord(g,point,taille))
print(djikstra1(g, point, taille))  


def bellmanford2 (graph,poids,s):
    d=[]
    pred = []
    for u in range (graph) :
        d[u] = inf
        pred[u] = None
    d[s] = 0
    for k in range (len(graph)-1):
        for u in range (graph) :
            for v in range (graph) :
                if d[v] > d[u] + poids[u][v] :
                    d[v] = d[u] + poids[u][v]
                    pred[v] = u
    return d,pred
