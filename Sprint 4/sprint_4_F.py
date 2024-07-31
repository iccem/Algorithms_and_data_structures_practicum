'''
Этот алгоритм называется Полиномиальное хеширование с префиксными хешами.
Он используется для быстрого вычисления хешей подстрок в строке, что позволяет отвечать на запросы о подстроках за
O(1) после предварительной обработки строки за O(n).

Основная идея алгоритма:
Префиксные хеши: Предварительно вычисляются хеши всех префиксов строки. Хеш префикса длиной
i включает все символы от начала строки до i-го символа.
Вычисление хеша подстроки: Хеш подстроки можно получить за O(1)
с использованием префиксных хешей и заранее вычисленных степеней основания.
Алгоритм:
Вычисление префиксных хешей:
prefix_hashes[i]=(prefix_hashes[i−1]×base+ord(line[i−1]))%mod
Вычисление степеней основания:
power[i]=(power[i−1]×base)%mod
Хеш подстроки с помощью префиксных хешей:
hash_value=(prefix_hashes[r]−(prefix_hashes[l−1]×power[r−l+1])%mod+mod)%mod
История и авторство:
Полиномиальное хеширование является широко используемой техникой
в алгоритмах строковой обработки и восходит к фундаментальным работам по хешированию.
Концепция префиксных хешей в контексте полиномиального хеширования
и использования этих хешей для эффективного вычисления хешей подстрок
была разработана и популяризована в сообществе компьютерной науки и алгоритмов.

Один из ранних описаний использования полиномиального хеширования
для работы со строками можно найти в учебниках и научных статьях
по алгоритмам и структурам данных. Однако конкретное имя автора или дата изобретения
не всегда явно указаны, так как этот метод представляет собой
обобщение идей из хеширования и динамического программирования,
которые развивались в течение нескольких десятилетий.

Применение:
Полиномиальное хеширование с префиксными хешами активно используется
в алгоритмах поиска подстрок (например, в алгоритме Рабина-Карпа)
и для решения задач, связанных с проверкой эквивалентности подстрок,
задачами поиска дубликатов и многими другими.
'''

def compute_prefix_hashes_and_powers(string, q, m):
    n = len(string)
    prefix_hashes = [0] * (n + 1)
    powers = [1] * (n + 1)
    for i in range(1, n + 1):
        prefix_hashes[i] = (prefix_hashes[i - 1] * q + ord(string[i - 1])) % m
        powers[i] = (powers[i - 1] * q) % m
    return prefix_hashes, powers


def get_substring_hash(prefixes, powers, start, end, m):
    hash_value = (prefixes[end] - prefixes[start - 1] * powers[end - start + 1]) % m
    if hash_value < 0:
        hash_value += m
    return hash_value


def get_substring_hashes(string, slices, q, m):
    prefix_hashes, powers = compute_prefix_hashes_and_powers(string, q, m)
    results = []
    for start, end in slices:
        hash_value = get_substring_hash(prefix_hashes, powers, start, end, m)
        results.append(hash_value)
    return results


def read_input():
    q = int(input().strip())
    m = int(input().strip())
    string = input().strip()
    slices = []
    n = int(input().strip())
    while n > 0:
        temp = list(map(int, (input().strip().split())))
        slices.append(temp)
        n -= 1
    return string, q, m, slices


string, q, m, slices = read_input()
hashes = get_substring_hashes(string, slices, q, m)
print('\n'.join(map(str, (i for i in hashes))))
