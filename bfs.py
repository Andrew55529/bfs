from collections import deque
import random

def generate_data(vertex=random.randint(5, 100),min_e=2):
    # Создаем множество вершин
    v = []
    for tmp in range(vertex):
        v.append({'id': tmp})
    # Создаем множество ребер
    e = [[] for i in range(len(v))]
    for v_one in v:
        while len(e[v_one['id']]) <min_e:
            v_gen = random.sample(v,1)[0]
            if v_gen['id'] != v_one['id']:
                if (v_gen['id'] not in e[v_one['id']]):
                    e[v_one['id']].append(v_gen['id'])
                    e[v_gen['id']].append(v_one['id'])
    return v, e


def bfs(v, e, id):
    # Создаем очередь
    q = deque()
    # Добавляем первый элемент в очередь
    q.append(id)
    v[id]['count']=0
    # Выполням пока в очереди есть элементы
    while len(q) != 0:
        a = q.popleft()
        # Каждую смежную вершину ранее не помеченную добавляем в очередь и присмаиваем длину
        for vertex in e[a]:
            if 'count' not in v[vertex].keys():
                v[vertex]['count'] = v[a]['count'] + 1
                q.append(vertex)
    return v, e