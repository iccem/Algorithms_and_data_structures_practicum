import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class DoubleConnectedNode:
        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev


def solution(node):
    temp = node.next
    node.next = node.prev
    node.prev = temp
    node = temp
    while node.next is not None:
        temp = node.next
        node.prev, node.next = node.next, node.prev
        node = temp
    temp = node.prev
    node.next = temp
    node.prev = None
    return node
    # print()


def print_list(node):
    current = node
    n = 5000
    values = []
    while current is not None or n < 1:
        values.append(current.value)
        n -= 1
        current = current.next
    print("\n".join(map(str, values)))


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)

    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.prev is node1

    print_list(new_head)


if __name__ == '__main__':
    test()