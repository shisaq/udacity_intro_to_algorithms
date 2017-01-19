def edge(x, y):
    return (x, y) if x < y else (y, x)

def create_tour(nodes):
    tour = []
    l = len(nodes)
    for i in range(l):
        t = edge(nodes[i], nodes[(i+1) % l])
        tour.append(t)
    return tour

arr = [1,2,3,4,5]
print create_tour(arr)
