import math
# Creates a node object with a few properties which will come in handy.
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.previousNode = None
        self.distance = math.inf
        self.pathL = 0

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getPrerviousNode(self):
        return self.previousNode
    
    def getDistance(self):
        return self.distance
    
    def setPreviousNode(self, n):
        self.previousNode = n
        
    def setDistance(self,d):
        self.distance = d

    def getPathLen(self):
        return self.pathL
    def setPathLen(self, d):
        self.pathL = d

# Use this to print a pretty board
def gridPrint(grid, start, end):
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            if grid[i][j] == end:
                print("3", end=" ")
            elif grid[i][j] == start:
                print("2", end=" ")
            elif isinstance(grid[i][j],Node):
                print("0",end = " ")
            else:
                print(grid[i][j],end=" ")
        print()
    print()
# Make the board however you want
# The start and end nodes are declared in the main method so pick your location for your start and end there
# In the board generation, assign
# 1 = wall
# 2 = start
# 3 = end
# * = path
# currently the board is 11 x 11 but you can change it and it should probably work still
def boardGeneration(start, end):
    board = []
    for i in range(0, 11):
        temp = []
        for j in range(0, 11):
            temp.append(0)
        board.append(temp)

    for i in range(1, len(board)):
        board[len(board)-1 - i][i] = 1
    board[start.getRow()][start.getCol()] = start
    board[end.getRow()][end.getCol()] = end

    for i in range(0,len(board)-4):
        board[len(board)-i-1][i+3] = 1

    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            if board[i][j] == 0:
                n = Node(i,j)
                board[i][j] = n
    return board

# just returns the surrounding nodes. In the future I might extend to doing diagonals so the majority of changes
# will occurr here.
# I know this method looks ugly but It just took 15 minutes to brute force and seems to work fine enough. 
def getNeighbours(n, board, prev):
    retValue = []
    row = n.getRow()
    col = n.getCol()

    if row > 0 and row < len(board)-1 and col > 0 and col < len(board)-1:
        if(not(board[row+1][col] in prev)):
            retValue.append(board[row + 1][col])
        if (not (board[row][col+1] in prev)):
            retValue.append(board[row][col+1])
        if (not (board[row - 1][col] in prev)):
            retValue.append(board[row-1][col])
        if (not (board[row][col - 1] in prev)):
            retValue.append(board[row][col - 1])
    elif row == 0 and col == 0:
        if (not (board[row + 1][col] in prev)):
            retValue.append(board[row+1][col])
        if (not (board[row][col + 1] in prev)):
            retValue.append(board[row][col+1])
    elif row == len(board)-1 and col == 0:
        if (not (board[row - 1][col] in prev)):
            retValue.append(board[row-1][col])
        if (not (board[row][col + 1] in prev)):
            retValue.append(board[row][col+1])
    elif row == len(board) - 1 and col == len(board)-1:
        if (not (board[row - 1][col] in prev)):
            retValue.append(board[row-1][col])
        if (not (board[row][col - 1] in prev)):
            retValue.append(board[row][col - 1])
    elif row == 0 and col == len(board)-1:
        retValue.append(board[row + 1][col])
        if (not (board[row][col - 1] in prev)):
            retValue.append(board[row][col - 1])
    elif row == 0:
        if (not (board[row + 1][col] in prev)):
            retValue.append(board[row+1][col])
        if (not (board[row][col + 1] in prev)):
            retValue.append(board[row][col+1])
        if (not (board[row][col - 1] in prev)):
            retValue.append(board[row][col - 1])
    elif row == len(board)-1:
        if (not (board[row - 1][col] in prev)):
            retValue.append(board[row-1][col])
        if (not (board[row][col + 1] in prev)):
            retValue.append(board[row][col+1])
        if (not (board[row][col - 1] in prev)):
            retValue.append(board[row][col - 1])
    elif col == 0:
        if (not (board[row + 1][col] in prev)):
            retValue.append(board[row+1][col])
        if (not (board[row - 1][col] in prev)):
            retValue.append(board[row-1][col])
        if (not (board[row][col + 1] in prev)):
            retValue.append(board[row][col+1])
    elif col == len(board)-1:
        if (not (board[row + 1][col] in prev)):
            retValue.append(board[row+1][col])
        if (not (board[row - 1][col] in prev)):
            retValue.append(board[row-1][col])
        if (not (board[row][col - 1] in prev)):
            retValue.append(board[row][col - 1])

    return retValue

# assigns a "distance" value which is used in the priority queue
def distance(c, e):
    distance = math.sqrt( (c.getRow()  - e.getRow()) * (c.getRow()  - e.getRow()) + (c.getCol()  - e.getCol()) * (c.getCol()  - e.getCol()))
    c.setDistance(distance + c.getPathLen())


# pick your start and end node points here
start = Node(0,0)
end = Node(9,9)

# create the board as specified in the boardGeneration method
board = boardGeneration(start, end)

# just to print the inital grid
gridPrint(board, start, end)

# prev is the list of all previously visited nodes. To make the walls not count as nodes, I just added it to prev so
# 1 will not be considered a node.
prev = []
prev.append(1)

# pQ is the priority queue which in this case is just a list but it works well enough
pQ = []

# gets a list of neighbours
n = getNeighbours(start,board,prev)

# each neighbour gets their distance calculated and added to the priority queue and have their links for previous nodes
# set
for i in range(0,len(n)):
    n[i].setPathLen(start.getPathLen() + 1)
    distance(n[i],end)
    pQ.append(n[len(n)-1-i])
    n[i].setPreviousNode(start)

# added to the list of previously visited nodes
prev.append(start)

#sorts the list based on the distances = euclidean distance + path length
pQ.sort(key=lambda x:x.distance)


# repeats the above process until we find the end node. In the case that a path to end does not exist, you will get an
# empty priority queue
while(len(pQ) > 0 and pQ[0]!=end):
    cN = pQ[0]
    del pQ[0]
    n = getNeighbours(cN,board,prev)
    for i in range(0,len(n)):
        n[i].setPathLen(cN.getPathLen()+1)
        distance(n[i],end)
        pQ.append(n[len(n)-1-i])
        n[i].setPreviousNode(cN)
    pQ.sort(key=lambda x: x.distance)
    prev.append(cN)

# prints either no path availaible or prints the path out.
if len(pQ) == 0:
    print("No Path availaible")
else:
    cN = end
    while(cN != start):
        if cN != end:
            board[cN.getRow()][cN.getCol()] = "*"
        cN = cN.getPrerviousNode()

    gridPrint(board, start, end)