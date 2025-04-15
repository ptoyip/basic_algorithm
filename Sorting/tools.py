import random
from typing import Callable, Tuple


def checking(fun: Callable, **args):
    for i in range(10):
        nums = [random.randint(1, 1000) for _ in range(10)]
        nums_cp = nums.copy()
        nums_cp = sorted(nums_cp)
        nums = fun(nums, leftBound=0, rightBound=len(nums)-1)
        if nums != nums_cp:
            print(nums)
            print(nums_cp)
            return False
    return True


def swap(nums: list[int], idx1: int, idx2: int) -> list[int]:
    temp = nums[idx1]
    nums[idx1] = nums[idx2]
    nums[idx2] = temp
    return nums


def merge(nums: list[int], leftPtr: int, rightPtr: int, rightBound: int) -> list[int]:
    if leftPtr == rightBound:
        return nums

    nums_cp = [0] * (rightBound - leftPtr + 1)
    i, j, k = leftPtr, rightPtr, 0

    while i < rightPtr and j <= rightBound:
        nums_cp[k] = nums[i] if nums[i] <= nums[j] else nums[j]
        k += 1
        if nums[i] <= nums[j]:
            i += 1
        else:
            j += 1

    while i < rightPtr:
        nums_cp[k] = nums[i]
        k += 1
        i += 1
    while j <= rightBound:
        nums_cp[k] = nums[j]
        k += 1
        j += 1
    for _ in range(len(nums_cp)):
        nums[leftPtr+_] = nums_cp[_]
    return nums
