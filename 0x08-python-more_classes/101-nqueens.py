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
			if grid.gridcord[checkx][checky][2] == "Q":
				enemy = True
			checkx += 1
			checky += 1

		# Checking second diagonal
		checkx = self.cord[0]
		checky = self.cord[1]
		checkx -= 1
		checky += 1
		while checkx != self.cord[0] and checky != self.cord[1]:
			if checkx < 0 or checky > 3:
				checkx += checky
				checky -= checky
			if checkx == self.cord[0] and checky == self.cord[1]:
				break
			if grid.gridcord[checkx][checky][2] == "Q":
				enemy = True
			print("checking: ", checkx, checky)
			checkx -= 1
			checky += 1

		# # Checking vertical
		# checkx = self.cord[0]
		# checky = self.cord[1]
		# checky += 1
		# while checky != self.cord[1]:
		# 	if checky > 3:
		# 		checky = 0
		# 	if grid.gridcord[checkx][checky][2] == "Q":
		# 		enemy = True
		# 	checky += 1

		# # Checking horizontal
		# checkx = self.cord[0]
		# checky = self.cord[1]
		# checkx += 1
		# while checkx != self.cord[0]:
		# 	if checkx > 3:
		# 		checkx = 0
		# 	if grid.gridcord[checkx][checky][2] == "Q":
		# 		enemy = True
		# 	checkx += 1

		return (enemy)

args = sys.argv
if len(args) != 2:
	print("Usage: nqueens N")
	exit(1)

mygrid = Grid(int(args[1]))
i = j = 0
arr = []
arr.append(Queen([3,3]))
mygrid.addQueen(arr[0])
	

			
mygrid.printGridStr()
mygrid.printGridCord()
print(arr[0].checkAttack(mygrid))

	
