import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item

def solution(node, elem):
    counter = 0
    while node.next_item is not None:
        if node.value == elem:
            break
        node = node.next_item
        counter += 1
    if node.next_item is None:
        return -1
    else:
        node.next_item = node.next_item.next_item
    return counter

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2

if __name__ == '__main__':
    test()