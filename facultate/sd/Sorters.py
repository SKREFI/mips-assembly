from math import log
from random import randint as r
import time


def quick(inp, low=0, high=-1):
    def partition(inp, low, high):
        i = low-1
        pivot = inp[high]

        for j in range(low, high):
            if inp[j] < pivot:
                i = i+1
                inp[i], inp[j] = inp[j], inp[i]

        inp[i+1], inp[high] = inp[high], inp[i+1]
        return i+1

    if high == -1:
        high += len(inp)
    if low < high:
        pi = partition(inp, low, high)
        quick(inp, low, pi-1)
        quick(inp, pi+1, high)
    return inp


def bubble(inp):
    n = len(inp)
    for i in range(n):
        for j in range(n - i - 1):
            if inp[j] > inp[j+1]:
                inp[j], inp[j+1] = inp[j+1], inp[j]
    return inp


def radix(inp, BASE=256):
    if len(inp) == 0:
        return []
    digits = (int(log(max(inp), BASE)) + 1)

    def setup():
        d = {}
        for i in range(BASE):
            d[i] = []
        return d

    def dicToList(d):
        l = []
        for values in d.values():
            for value in values:
                l.append(value)
        return l

    key = 1  # adica cifra unitatilor (abcd // key = d)
    for _ in range(digits):
        d = setup()
        for i in inp:
            d[(i//key) % BASE].append(i)
        inp = dicToList(d)
        key *= BASE
    return inp


def count(inp):
    l = [0 for _ in range(max(inp) + 1)]
    for i in inp:
        l[i] += 1
    ret = []
    index = 0
    for i in l:
        for _ in range(i):
            ret.append(index)
        index += 1
    return ret


def systemSort(inp):
    return sorted(inp)


def merge(inp):
    def merge_helper(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L, R = arr[:mid], arr[mid:]
            merge_helper(L)
            merge_helper(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    merge_helper(inp)
    return inp


def test(function, name, debugger=False, no_tests=10, lists_length=1000, min_num=0, max_num=10**10):
    def getms():
        return int(round(time.time() * 1000))

    def getRandomList(length, min, max):
        l = []
        for _ in range(length):
            l.append(r(min, max))
        return l

    times = []
    for i in range(no_tests):
        inp = getRandomList(lists_length, min_num, max_num)
        start = getms()
        result = function(inp)
        stop = getms()
        if result != sorted(inp):
            # raise Exception(Log.fail('Function did a bad job!'))
            Log.fail('Function did a bad job!')
        if debugger:
            Log.debug(f'Test {i+1}/{no_tests} time: {stop-start}')
            Log.debug(f'List: {result}')
        times.append(stop - start)
    print(Log.succes(f'{name} function\'s time: {sum(times)/len(times)} ms'))


class Log():
    end = '\033[0m'

    @classmethod
    def warning(cls, inp):
        print('\033[93m' + inp + cls.end)

    @classmethod
    def fail(cls, inp):
        print('\033[91m' + inp + cls.end)

    @classmethod
    def succes(cls, inp):
        print('\033[92m' + inp + cls.end)

    @classmethod
    def debug(cls, inp):
        print('\033[94m' + inp + cls.end)

    @classmethod
    def getAllStyles(cls):
        for i in range(100):
            print(f'\033[{i}mNumber{i}\033[0m')
