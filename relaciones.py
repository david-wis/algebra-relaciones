import networkx as nx
import matplotlib.pyplot as plt

#   -----------------------------------------------------
#   Graficador clasificador de relaciones entre conjuntos 
#   -----------------------------------------------------  
#   
#   - Matplotlib no grafica relaciones del tipo (x,x) pero el programa las reconoce igual
#   - Las busquedas no están optimizadas ya que los datos se llenan siempre a mano
#   

def findItems(R, x = None, y = None):
    items = []
    for (x1, y1) in R:
        if (x != None and y != None):
            if ((x1, y1) == (x, y)):
                items.append((x1,y1))
        elif (x != None):
            if (x1 == x):
                items.append((x1,y1))
        elif (y != None):
            if (y1 == y):
              items.append((x1,y1))
        else:
            return []
    return items

def checkIfInDictionary(dic, el):
    for array in dic.values():
        for n in array:
            if n == el:
                return True    
    return False

def IsReflexive(A, R):
    reflexDic = {}
    for x in A:
        reflexDic[x] = False
    
    for (x,y) in R:
        if x == y: 
            reflexDic[x] = True
    return all(x for x in reflexDic.values())

def IsSymmetric(A, R):
    return all(R.count((y,x)) > 0 for (x,y) in R)

def IsTransitive(A, R):
    for (x, y) in R:
        secondElements = findItems(R, x=y)
        if len(secondElements) > 0:
            for (_, z) in secondElements:
                thirdElements = findItems(R, x, z)
                if len(thirdElements) == 0:
                    return False
    return True

def IsAntisymmetric(A, R):
    for (x, y) in R:
        secondElements = findItems(R, y, x)
        if len(secondElements) > 0:
            (x0, y0) = secondElements[0]
            if not (x == x0 and y == y0):
                return False
    return True
        
def TotalOrder(A, R):
    for x in A:
        for y in A:
            if len(findItems(R, x, y)) == 0 and len(findItems(R, y, x)) == 0:
                return False
    return True


def GetEquivClasses(A, R):
    equivDic = {}
    for i in A:
        if equivDic.get(i) is None and not checkIfInDictionary(equivDic, i):
            items = findItems(R, x=i)
            equivDic[i] = [y for (_, y) in items]
    return equivDic


# Conjunto universo
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Relacion en A
R = [
    (1, 1), (2, 2), (3, 3), (4, 4),
    (1, 2), (2, 1),
    (1, 3), (3, 1),
    (1, 4), (4, 1),
    (2, 3), (3, 2),
    (2, 4), (4, 2),
    (3, 4), (4, 3),
    
    (5, 5), (6, 6),
    (5, 6), (6, 5),
    
    (7, 7), (8, 8), (9, 9),
    (7, 8), (8, 7),
    (7, 9), (9, 7),
    (8, 9), (9, 8)
]
    
    
# Ejemplos

""" Relacion de orden total """

"""
A = [1, 2, 3]

R = [
     (1, 1), (2, 2), (3, 3),
     (3, 2), (2, 1), (3, 1)
]
"""

""" Relacion de equivalencia y orden """

"""
A = [1, 2, 3, 4, 5]
R = [(1,1), (2,2), (3,3), (4,4), (5,5)]
"""

def main():
    ref = IsReflexive(A, R)
    sim = IsSymmetric(A, R)
    trans = IsTransitive(A, R)
    anti = IsAntisymmetric(A, R)
    
    equiv = ref and sim and trans
    order = ref and anti and trans
    total = (ref and anti and trans and TotalOrder(A, R))
    
    print(f"Reflexiva: {'Si' if ref else 'No'}")
    print(f"Simetrica: {'Si' if sim else 'No'}")
    print(f"Antisimetrica: {'Si' if anti else 'No'}")
    print(f"Transitiva: {'Si' if trans else 'No'}")
    print(f"\nEquivalencia: {'Si' if equiv else 'No'}")
    if equiv:
        classDic = GetEquivClasses(A, R)
        print("Las clases de equivalencia son")
        for i in classDic:
            formattedDic = "{" + ', '.join([f"{str(x)}" for x in classDic[i]]) + "}"
            print(f"[{i}]: {formattedDic}")
    
    print(f"\nOrden: {'Si' if order else 'No'} - Total: {'Si' if total else 'No'}")
    
    graph = nx.DiGraph()
    graph.add_nodes_from(A)
    graph.add_edges_from(R)
    nx.draw(graph, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()
