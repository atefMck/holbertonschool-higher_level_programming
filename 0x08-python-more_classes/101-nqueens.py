#!/usr/bin/python3
import sys


class Grid:
    def __init__(self, size):
        if type(size) is not int:
            print("N must be a number")
            exit(1)
        if size < 4:
            print("N must be at least 4")
            exit(1)
        self.queens = 0
        self.size = size
        self.gridcord = []
        array = []
        for i in range(size):
            for j in range(size):
                array.append([i, j, "."])
            self.gridcord.append(array)
            array = []

    def printGridStr(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.gridcord[i][j][2], end="")
            print()

    def printGridCord(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.gridcord[i][j], end="")
            print()

    def addQueen(self, Queen):
        if self.gridcord[Queen.cord[0]][Queen.cord[1]][2] == ".":
            self.gridcord[Queen.cord[0]][Queen.cord[1]][2] = "Q"
            self.queens += 1
            return (True)
        return (False)

    def delQueen(self, Queen):
        if self.gridcord[Queen.cord[0]][Queen.cord[1]][2] == "Q":
            self.gridcord[Queen.cord[0]][Queen.cord[1]][2] = "."
            self.queens -= 1
            return (True)
        return (False)

    def getAllQueens(self):
        solution = [[]]
        for i in range(self.size):
            for j in range(self.size):
                if self.gridcord[i][j][2] == "Q":
                    solution.append(
                        [self.gridcord[i][j][0], self.gridcord[i][j][1]])
        del solution[0]
        return(solution)


class Queen:
    def __init__(self, cord=[0, 0]):
        self.cord = cord

    def checkAttack(self, grid):

        # Checking first diagonal
        checkx = self.cord[0]
        checky = self.cord[1]
        checkx += 1
        checky += 1
        while checkx != self.cord[0] and checky != self.cord[1]:
            if checkx > 3 or checky > 3:
                checkx -= checky
                checky -= checky
            if checkx == self.cord[0] and checky == self.cord[1]:
                break
            if checkx in range(mygrid.size) and checky in range(mygrid.size):
                if grid.gridcord[checkx][checky][2] == "Q":
                    return (True)
            checkx += 1
            checky += 1

        # Checking second diagonal
        checkx = self.cord[0]
        checky = self.cord[1]
        checkx += 1
        checky -= 1
        while checkx != self.cord[0] and checky != self.cord[1]:
            if checkx > 3 or checky < 0:
                checky += checkx
                checkx -= checkx
            if checkx == self.cord[0] and checky == self.cord[1]:
                break
            if checkx in range(mygrid.size) and checky in range(mygrid.size):
                if grid.gridcord[checkx][checky][2] == "Q":
                    return (True)
            checkx += 1
            checky -= 1

        # Checking horizontal
        checkx = self.cord[0]
        checky = self.cord[1]
        checky += 1
        while checky != self.cord[1]:
            if checky > 3:
                checky = 0
            if checky == self.cord[1]:
                break
            if grid.gridcord[checkx][checky][2] == "Q":
                return (True)
            checky += 1

        # Checking vertical
        checkx = self.cord[0]
        checky = self.cord[1]
        checkx += 1
        while checkx != self.cord[0]:
            if checkx > 3:
                checkx = 0
            if checkx == self.cord[0]:
                break
            if grid.gridcord[checkx][checky][2] == "Q":
                return (True)
            checkx += 1

        return (False)


args = sys.argv
if len(args) != 2:
    print("Usage: nqueens N")
    exit(1)

mygrid = Grid(int(args[1]))
i = j = num = k = l = 0
arr = []
solutions = []

try:
    while l < mygrid.size:
        arr.append(Queen([k, l]))
        mygrid.addQueen(arr[num])
        num += 1
        j = l + 1
        while i < mygrid.size:
            arr.append(Queen([i, j]))
            mygrid.addQueen(arr[num])
            if arr[num].checkAttack(mygrid):
                mygrid.delQueen(arr[num])
                del arr[num]
                num -= 1
            num += 1
            j += 1
            if j >= mygrid.size:
                i += 1
                j = 0
        if mygrid.queens != 4:
            mygrid = Grid(int(args[1]))
            i = 0
            num = 0
            arr = []
        elif mygrid.queens == 4:
            solutions.append(mygrid)
            mygrid = Grid(int(args[1]))
            i = 0
            num = 0
            arr = []
        l += 1
        if l >= mygrid.size:
            k += 1
            l = 0
except IndexError:
    pass
if len(solutions) == 0:
    print("This puzzle solver only works for 4 queens for some reason :x")
    print("We will fix that as soon as possible, thanks for your understanding cx")
for x in range(len(solutions)):
    print(solutions[x].getAllQueens())
