import math
from typing import Literal
from tools import *
from random import shuffle


def selection_sort(nums: list[int]) -> list[int]:
    """选择排序， 平均时间复杂度O(n^2), 空间复杂度O(1)， 不稳定
    进行n次“找最小的数”， 从下标0开始到n-1

    Args:
        nums (list[int]): 数组

    Returns:
        list[int]: 排序后数组
    """
    for i in range(len(nums)):
        minPos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minPos]:
                minPos = j

        nums = swap(nums, i, minPos)
    return nums


def bubble_sort(nums: list[int], optimized=False) -> list[int]:
    """冒泡排序，平均时间复杂度O(n^2)，空间复杂度O(1)，稳定
    进行n次两数检查大小(互换)

    Args:
        nums (list[int]): 数组
        optimized (bool, optional): 选择要不要每一轮开始前检查上一轮有没有变化. Defaults to False.

    Returns:
        list[int]: 排序数组
    """
    if not optimized:
        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums = swap(nums=nums, idx1=j, idx2=j+1)
        return nums
    else:
        length = len(nums)
        swapped = True
        while swapped:
            swapped = False
            for i in range(length - 1):
                if nums[i] > nums[i+1]:
                    nums = swap(nums, i, i+1)
                    swapped = True
            length -= 1
        return nums


def insertion_sort(nums: list[int], h=1) -> list[int]:
    """插入排序，平均时间复杂度O(n^2)，空间复杂度O(1)，稳定
    每个数和前面对比，直到插入到正确位置

    Args:
        nums (list[int]): 数组
        h (int, optional): gap(留着给希尔排序). Defaults to 1.

    Returns:
        list[int]: 排序数组
    """
    for i in range(h, len(nums)):
        for j in range(i, h-1, -h):
            if nums[j] < nums[j-h]:
                nums = swap(nums, j, j-h)
            else:
                break
    return nums


def shell_sort(nums: list[int], h=None, gapping: Literal['shell', 'knuth'] = 'shell') -> list[int]:
    """希尔排序，平均时间复杂度O(n^1.3)，空间复杂度O(1)，不稳定


    Args:
        nums (list[int]): _description_
        h (_type_, optional): _description_. Defaults to None.
        gapping (Literal[&#39;shell&#39;, &#39;knuth&#39;], optional): _description_. Defaults to 'shell'.

    Returns:
        list[int]: _description_
    """
    gapping_types = ['shell', 'knuth']
    assert gapping in gapping_types, f'gapping must in {gapping_types}'
    if h is None:
        h = len(nums) // 2

    if gapping == 'knuth':
        h = 1
        while h < len(nums):
            h = 3*h+1

    while h > 0:
        nums = insertion_sort(nums=nums, h=h)
        if gapping == 'shell':
            h //= 2
        elif gapping == 'knuth':
            h -= 1
            h //= 3
    return nums


def merge_sort(nums: list[int], left: int, right: int) -> list[int]:
    """_summary_

    Args:
        nums (list[int]): _description_
        left (int): left pointer of array
        right (int): right pointer of array

    Returns:
        _type_: _description_
    """
    if left == right:
        # print(f'-> return merge_sort({nums[left:right+1]})')
        return nums

    # use right - left prevent int overflow
    mid = int(left + (right - left) / 2)
    nums = merge_sort(nums, left=left, right=mid)
    nums = merge_sort(nums, left=mid+1, right=right)
    return merge(nums=nums, leftPtr=left, rightPtr=mid+1, rightBound=right)


def quick_sort(nums: list[int], leftBound: int, rightBound: int) -> list[int]:
    if leftBound >= rightBound:
        return nums
    pivot = nums[rightBound]
    left, right = leftBound, rightBound-1
    while left <= right:
        while nums[left] <= pivot and left <= right:
            left += 1
        while nums[right] > pivot and left <= right:
            right -= 1
        if left < right:
            nums = swap(nums=nums, idx1=left, idx2=right)
    nums = swap(nums=nums, idx1=left, idx2=rightBound)
    nums = quick_sort(nums=nums, leftBound=leftBound, rightBound=left-1)
    nums = quick_sort(nums=nums, leftBound=left+1, rightBound=rightBound)
    return nums


if __name__ == '__main__':
    # nums = list(range(10000))
    # shuffle(nums)

    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # nums = [1, 3, 6, 2, 5, 4, 7]
    # nums = [1, 3, 2]
    # nums = [9, 6, 11, 3, 5, 12, 8, 7, 10, 15, 14, 4, 1, 13, 2]

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~            Algorithm Selection                 ~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # nums = selection_sort(nums=nums)

    # For 10000 shuffled data, optimized ~ 4.5s , Not optimized ~ 4.7s
    # For 10000 sorted data, optimized ~ 0.004s , Not optimized ~ 2.2s
    # nums = bubble_sort(nums=nums, optimized=False)

    # nums = insertion_sort(nums=nums)
    # nums = shell_sort(nums=nums, h=4, gapping='shell')
    # nums = shell_sort(nums=nums, gapping='knuth')

    # nums = merge_sort(nums=nums, left=0, right=len(nums)-1)

    # nums = quick_sort(nums=nums, leftBound=0, rightBound=len(nums)-1)
    print(checking(quick_sort))

    # print(nums)
