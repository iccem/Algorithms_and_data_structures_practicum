"""
https://contest.yandex.ru/contest/22781/run-report/115387752/


-- ПРИНЦИП РАБОТЫ --
Реализована хеш-таблица с использованием метода цепочек для разрешения коллизий.
Хеш-таблица представлена списком заранее заданного размера,
в ячейках которого хранятся списки (цепочки) элементов.
По условиям задачи, поддерживать рехеширование и масштабирование хеш-таблицы не требуется, поэтому следует тщательно подойти к выбору размера массива хеш-таблицы.
Для решения текущей задачи было выбрано число 100003 по следующим соображениям:
по условию, количество ключей не может превышать 10ˆ5, выбор размера 100003 позволяет хранить все ключи, обеспечивая при этом низкую плотность заполнения таблицы. Низкая плотность (или коэффициент заполнения) таблицы приводит к уменьшению числа коллизий и повышает производительность операций поиска, вставки и удаления.
при коэффициенте заполнения таблицы, близком к 1, время выполнения операций остается в среднем близким к O(1). При размере таблицы 100003 и максимальном количестве ключей 10ˆ5, коэффициент заполнения составляет примерно 1.05, что позволяет поддерживать высокую производительность.
выбранный размер предоставляет гибкость для небольшого увеличения количества элементов, не требуя немедленного изменения размера таблицы.
Думается, также отметить недостаток сделанного выбора:
выбранный размер может оказаться избыточным для хранения менее 100000 ключей; будет создано много пустых ячеек, а это неэффективно с точки зрения использования памяти

Таблица поддерживает основные операции:
добавление (put), получение (get) и удаление (delete) элементов.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Корректность работы алгоритма обеспечивается использованием хеш-функции
для определения индекса ячейки, в которой должен храниться элемент.
Для разрешения коллизий применяется метод цепочек:
если несколько элементов имеют один и тот же хеш-индекс,
они сохраняются в связанный список в соответствующей ячейке.
При добавлении элемента алгоритм проверяет наличие ключа в списке и обновляет значение, если ключ уже существует.
При получении и удалении элемента
алгоритм последовательно просматривает элементы списка в соответствующей ячейке, что гарантирует корректность выполнения операций.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Операции добавления (put), получения (get) и удаления (delete) элемента
в среднем выполняются за O(1) благодаря равномерному распределению хеш-функции и небольшому размеру цепочек.
В худшем случае, при возникновении большого количества коллизий, временная сложность операций может увеличиться до O(n), где n — количество элементов в таблице.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Пространственная сложность хеш-таблицы составляет O(n + m),
где n — размер массива таблицы, m — количество элементов в таблице.
Дополнительно используется память для хранения списков (цепочек) и элементов в них.



"""


class Deque:

    def __init__(self, n):
        self.deque = [None] * n
        self.head = 0
        self.tail = 0
        self.size = 0
        self.maximum_number_of_items = n

    def push_back(self, x):
        if self.size == self.maximum_number_of_items:
            raise OverflowError()
        self.deque[self.tail] = x
        self.tail = (self.tail + 1) % self.maximum_number_of_items
        self.size += 1

    def push_front(self, x):
        if self.size == self.maximum_number_of_items:
            raise OverflowError()
        self.head = (self.head - 1) % self.maximum_number_of_items
        self.deque[self.head] = x
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError()
        else:
            self.tail = (self.tail - 1) % self.maximum_number_of_items
            x = self.deque[self.tail]
            self.deque[self.tail] = None
            self.size -= 1
            return x

    def pop_front(self):
        if self.size == 0:
            raise IndexError()
        else:
            x = self.deque[self.head]
            self.deque[self.head] = None
            self.head = (self.head + 1) % self.maximum_number_of_items
            self.size -= 1
            return x


def read_input():
    n = int(input().strip())
    m = int(input().strip())
    method_names = []
    deque = Deque(m)

    while n > 0:
        method_names.append(input().strip())
        n -= 1

    for i in method_names:
        try:
            if ' ' in i:
                method_name, parameter = i.split()
                parameter = int(parameter)
                method = getattr(deque, method_name)
                method(parameter)
            else:
                method = getattr(deque, i)
                print(method())
        except (IndexError, OverflowError):
            print('error')


if __name__ == '__main__':
    read_input()
