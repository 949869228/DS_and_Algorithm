"""
常见的查找算法
"""


# 线性查找
def linear_search(arr, target):
    """从头到尾去查找某个元素，若元素不存在，返回-1

    Parameters:
    -----------
    arr : list

    target : int or float
    """
    if not arr:
        return -1
    for index, elem in enumerate(arr):
        if elem == target:
            return index
    return -1


# 二分查找
def binary_search(arr, target):
    """二分查找，若元素不存在，返回-1
    注：假设arr已经有序

    Parameters:
    -----------
    arr : list

    target : int or float
    """
    if not arr:
        return -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search2(arr, target):
    """二分查找，若元素不存在，返回-1
    这次我们要求返回target第一次出现的index

    Parameters:
    -----------
    arr : list

    target : int or float
    """
    if not arr:
        return -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def test_search():
    print("test linear search")
    arr1 = [1, 65, 2, 45, 9, 0, 111]
    assert linear_search(arr1, 65) == 1

    print("test binary search")
    arr2 = [1, 1, 2, 2, 2, 2, 2, 2, 2, 3]
    assert binary_search(arr2, 2) == 4
    assert binary_search([], 2) == -1

    print("test binary search2")
    assert binary_search2(arr2, 2) == 2


if __name__ == "__main__":
    test_search()