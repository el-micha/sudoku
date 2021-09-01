
class Board:
    all = {1,2,3,4,5,6,7,8,9}

    def __init__(self):
        self.cells = list(range(81))
        self.row_cons = [{1,2,3,4,5,6,7,8,9} for i in range(9)]
        self.col_cons = [{1,2,3,4,5,6,7,8,9} for i in range(9)]
        self.block_cons = [{1,2,3,4,5,6,7,8,9} for i in range(9)]
        self.cnt = 0

    def step(self):
        print("step", str(self.cnt), "---------------------------------------------")
        self.cnt += 1
        print(self)
        self.place_singles()
        print(self)
        print("step done", "=========================================")

    def place_singles(self):
        xs = [(i, j, b.get_poss(i, j)) for j in range(9) for i in range(9) if len(b.get_poss(i, j)) > 0]
        ys = sorted(xs, key=lambda tup: len(tup[2]))
        print("constraints, sorted:", ys)
        if len(ys) == 0:
            print("board is full")
            return
        singles = list(filter(lambda tup: len(tup[2]) == 1, ys))
        print("singles:            ", singles)
        if len(singles) == 0:
            print("cannot find any singles")
            return
        for i, j, sgt in singles:
            self.set(sgt.pop(), i, j)
            print("set ", self.get(i, j), "at", i, j)

    def reduce_double_constraints(self):
        """if a digit in a block must occur on a col or row, all other cols/rows cannot have that digit"""
        for n, block in self.get_blocks():
            block_cons = self.block_cons[n]
            block_rows = [self.row_cons[x] for x in self.get_row_indices_for_block(n)]
            block_cols = [self.col_cons[x] for x in self.get_col_indices_for_block(n)]
            # if possible digit is only possible in one row, all other rows can be ruled out.
            for digit in block_cons:
                if digit in ...:
                    pass

    def get_row_indices_for_block(self, n):
        x, y = int(n/3), n%3
        return [x, x+1, x+2]

    def get_col_indices_for_block(self, n):
        x, y = int(n/3), n%3
        return [y, y+1, y+2]

    def setup_linear(self, xs):
        assert(len(xs) == 81)
        for i in range(9):
            for j in range(9):
                self.set(xs[i*9+j], i, j)

    def setup_from_tups(self, xs):
        for n, i, j in xs:
            self.set(n, i, j)

    def set(self, n, i, j):
        self.cells[i*9+j] = n
        self.row_cons[i].discard(n)
        self.col_cons[j].discard(n)
        self.block_cons[self.coords_to_block_index(i,j)].discard(n)

    def get(self, i, j):
        return self.cells[i*9+j]

    def get_poss(self, i, j):
        if self.get(i,j) > 0:
            return set()
        # print("poss at", i, j)
        # print(self.row_cons[i])
        # print(self.col_cons[j])
        # print(self.block_cons[self.coords_to_block_index(i,j)])
        res =  Board.all & self.row_cons[i] & self.col_cons[j] & self.block_cons[self.coords_to_block_index(i,j)]
        # print(res)
        # print("=====")
        return res

    def get_row(self, i):
        return self.cells[9*i:9*i+9]

    def get_col(self, i):
        return [self.cells[j*9+i] for j in range(9)]

    def get_rows(self):
        return [self.get_row(i) for i in range(9)]

    def get_cols(self):
        return [self.get_col(i) for i in range(9)]

    def get_block_by_coords(self, i, j):
        return self.get_block(int(i/3)*3 + int(j/3))

    def get_block(self, i):
        return [self.cells[x*9 + y] for (x,y) in self._nhood(*self._midpoints()[i])]

    def get_blocks(self):
        return [self.get_block(i) for i in range(9)]

    def _midpoints(self):
        return [(1,1), (1,4), (1,7), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7)]

    def _nhood(self, i, j):
        return [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]

    def coords_to_block_index(self, i, j):
        return int(i/3)*3 + int(j/3)

    def __repr__(self):
        s = ""
        for x in self.get_rows():
            s += str(x) + "\n"
        return s

s1 = [5,3,0,0,7,0,0,0,0,6,0,0,1,9,5,0,0,0,0,9,8,0,0,0,0,6,0,8,0,0,0,6,0,0,0,3,4,0,0,8,0,3,0,0,1,7,0,0,0,2,0,0,0,6,0,6,0,0,0,0,2,8,0,0,0,0,4,1,9,0,0,5,0,0,0,0,8,0,0,7,9]
s2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,8,5,0,0,1,0,2,0,0,0,0,0,0,0,5,0,7,0,0,0,0,0,4,0,0,0,1,0,0,0,9,0,0,0,0,0,0,0,5,0,0,0,0,0,0,7,3,0,0,2,0,1,0,0,0,0,0,0,0,0,4,0,0,0,9]
s3 = [0,7,0,1,0,6,0,0,0,0,0,4,0,0,0,7,0,0,8,0,0,0,0,0,5,3,0,2,0,1,0,9,4,0,0,0,0,8,0,0,0,0,0,9,0,0,0,0,6,8,0,2,0,5,0,1,5,0,0,0,0,0,3,0,0,7,0,0,0,6,0,0,0,0,0,9,0,3,0,7,0]
b = Board()
b.setup_linear(s3)
b.step()

