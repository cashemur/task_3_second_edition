from random import randint


class TestArray:
    def __init__(self, array):
        self.array = array

    def findMax(self):
        self.array.sort()
        self.max = self.array[-1]
        self.secondMax = 0
        for i in range(len(self.array)-1, -1, -1):
            if self.array[i] != self.array[-1] and self.array[i] > self.secondMax:
                self.secondMax = self.array[i]

        return self.max, self.secondMax
