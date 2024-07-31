class StackMax:

    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if len(self.items) == 0:
            print('error')
        else:
            del self.items[-1]

    def get_max(self):
        if len(self.items) != 0:
            max_element = max(self.items)
            print(max_element)
        else:
            print('None')


def test():
    stack = StackMax()
    parametr = None
    method_name = ''
    method_names = []
    n = int(input())
    while n > 0:
        method_names.append(input().strip())
        n -= 1
    for i in method_names:
        if ' ' in i:
            method_name, parametr = i.split()
        if parametr == None:
            method = getattr(stack, i)
            method()
        else:
            parametr = int(parametr)
            method = getattr(stack, method_name)
            method(parametr)
            method_name = ''
            parametr = None


if __name__ == '__main__':
    test()
