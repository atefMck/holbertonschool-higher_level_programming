#!/usr/bin/python3
import sys

class Grid:
	queens = 0
	def __init__(self, size):
		if type(size) is not int:
			print("N must be a number")
			exit(1)
		if size < 4:
			print("N must be at least 4")
			exit(1)
		self.size = size
		self.gridcord = []
		array = []
		for i in range(size):
			for j in range(size):
				array.append([i , j, "."])
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
			Grid.queens += 1
			return (True)
		return (False)

	def delQueen(self, Queen):
		if self.gridcord[Queen.cord[0]][Queen.cord[1]][2] == "Q":
			self.gridcord[Queen.cord[0]][Queen.cord[1]][2] = "."
			Grid.queens -= 1
			return (True)
		return (False)
			

class Queen:
	def __init__(self, cord=[0,0]):
		self.cord = cord

	def checkAttack(self, grid):
		enemy = False;

		checkx = self.cord[0]
		checky = self.cord[1]
		checkx += 1
		checky += 1
		while checkx != self.cord[0] and checky != self.cord[1]:
			if grid.gridcord[checkx][checky][2] == "Q":
				enemy = True
			checkx += 1
			checky += 1
			if checkx > 3 or checky > 3:
				checky -= checkx
				checkx -= checkx

		checkx = self.cord[0]
		checky = self.cord[1]
		checkx -= 1
		checky += 1
		while checkx != self.cord[0] and checky != self.cord[1]:
			if grid.gridcord[checkx][checky][2] == "Q":
				enemy = True
			checkx -= 1
			checky += 1
			if checkx < 0 or checky < 0:
				checkx += checky
				checky -= checky

		checkx = self.cord[0]
		checky = self.cord[1]
		checky += 1
		while checky != self.cord[1]:
			if grid.gridcord[checkx][checky][2] == "Q":
				enemy = True
			checky += 1
			if checky > 3:
				checky = 0

		checkx = self.cord[0]
		checky = self.cord[1]
		checkx += 1
		while checkx != self.cord[0]:
			if grid.gridcord[checkx][checky][2] == "Q":
				enemy = True
			checkx += 1
			if checkx > 3:
				checkx = 0

		return (enemy)

args = sys.argv
if len(args) != 2:
	print("Usage: nqueens N")
	exit(1)

mygrid = Grid(int(args[1]))
i = j = 0
arr = []
arr.append(Queen([0,0]))
mygrid.addQueen(arr[0])

v = True
arr.append(Queen([0,1]))
mygrid.addQueen(arr[1])
num = 1
while arr[num].checkAttack(mygrid) or v == False:
	v = False
	j += 1
	if j >= mygrid.size:
		i += 1
		j = 0
	arr.append(Queen([i, j]))
	mygrid.addQueen(arr[num])
	print(arr[num].cord)
	num += 1
	if arr[1].checkAttack(mygrid):
		del arr[1]
		num -= 1
	

			

mygrid.printGridStr()
mygrid.printGridCord()


	
