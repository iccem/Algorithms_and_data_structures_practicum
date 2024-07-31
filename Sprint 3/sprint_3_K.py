def merge(arr, lf, mid, rg):
    c = [0] * (rg - lf)

    a = arr[lf:mid]
    len_a = mid - lf

    b = arr[mid:rg]
    len_b = rg - mid

    i, k, n = 0, 0, 0
    while i < len_a and k < len_b:
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len_a:
        c[n] = a[i]
        i += 1
        n += 1
    while k < len_b:
        c[n] = b[k]
        k += 1
        n += 1
    return c


def merge_sort(arr, lf, rg):
    c = [0] * (rg - lf)
    if rg - lf <= 1:
        return
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    c = merge(arr, lf, mid, rg)

    m = 0
    s = lf
    while m < len(c) and s < rg:
        arr[s] = c[m]
        m += 1
        s += 1


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
