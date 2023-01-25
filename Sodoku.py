class Sodoku:
    def __init__(self, sodoku):
        self.sodoku = sodoku
        self.counter = 0

    def solve(self):
        self.counter += 1
        geloest = False
        if self.isSolved():
            print(self.sodoku)
            return True
        else:
            x, y = self.getFirstUnsolved()
            posibilities = self.getPosibilities(x, y)
            for i in posibilities:
                self.sodoku[x][y] = i
                if self.solve() is True:
                    geloest = True
                self.sodoku[x][y] = 0
            return geloest

    def isSolved(self):
        contains = [False for i in range(9)]
        for i in range(9):
            for j in range(9):
                if self.sodoku[i][j] == 0:
                    return False
                else:
                    contains[self.sodoku[i][j] - 1] = True
            for q in contains:
                if q == False:
                    return False
            contains = [False for s in range(9)]
        for i in range(9):
            for j in range(9):
                if self.sodoku[j][i] == 0:
                    return False
                else:
                    contains[self.sodoku[j][i] - 1] = True
            for q in contains:
                if q == False:
                    return False
            contains = [False for s in range(9)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        if self.sodoku[(3 * i) + k][(3 * j) + l] == 0:
                            return False
                        else:
                            contains[self.sodoku[(3 * i) + k][(3 * j) + l] - 1] = True
                for q in contains:
                    if q == False:
                        return False
                contains = [False for s in range(9)]
        return True

    def getFirstUnsolved(self):
        for i in range(9):
            for j in range(9):
                if self.sodoku[i][j] == 0:
                    return i, j

    def getPosibilities(self, x, y):
        contains = [True for i in range(9)]
        for i in range(9):
            if self.sodoku[x][i] != 0:
                contains[self.sodoku[x][i] - 1] = False
            if self.sodoku[i][y] != 0:
                contains[self.sodoku[i][y] - 1] = False
        x = int(x / 3)
        y = int(y / 3)
        for i in range(3):
            for j in range(3):
                if self.sodoku[(3 * x) + i][(3 * y) + j] != 0:
                    contains[self.sodoku[(3 * x) + i][(3 * y) + j] - 1] = False
        list = []
        for i in range(9):
            if contains[i] is True:
                list = list + [i + 1]

        return list

    def initSodoku(self):
        self.sodoku = sodoku


if __name__ == "__main__":
    sodoku = [
        [0, 5, 0, 0, 7, 0, 1, 0, 6],
        [6, 9, 2, 1, 4, 0, 0, 7, 8],
        [1, 8, 0, 6, 5, 9, 4, 0, 3],
        [0, 0, 0, 0, 1, 0, 2, 0, 4],
        [4, 0, 6, 8, 0, 2, 0, 0, 0],
        [5, 0, 0, 3, 0, 4, 0, 8, 9],
        [0, 0, 9, 0, 3, 5, 0, 0, 2],
        [0, 4, 0, 0, 0, 0, 8, 0, 1],
        [2, 0, 0, 0, 0, 1, 0, 3, 7],
    ]
    meinSodoku = Sodoku(sodoku)
    meinSodoku.solve()
