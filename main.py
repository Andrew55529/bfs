from bfs import generate_data, bfs
import random

if __name__ == '__main__':
    # Генерируем входные данные
    v, e = generate_data(100,2)
    # Выбоор рандомного источника
    source = random.randint(0, len(v)-1)
    # Поиск
    v, e = bfs(v, e, source)
    print(v,e,source)