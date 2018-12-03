class Matrix(object):
    def __init__(self, row_size, col_size):
        self.cols = col_size
        self.rows = row_size
        self.matrix = Matrix.__createMatrix(self.rows, self.cols)

    def __createMatrix(rows, cols):
        matrix = []
        for row in range(rows):
            matrix.append([])
            for col in range(cols):
                matrix[row].append(0)
        return matrix

    def display(self):
        for row in range(self.rows):
            print("|", end=" ")
            for col in range(self.cols):
                print(self.matrix[row][col], end=" ")
            print("|")
        print()

    def reset(self):
        for rindex, row in enumerate(self.matrix):
            for cindex, col in enumerate(row):
                self.matrix[rindex][cindex] = 0

    def fillSubMatrix(self, dist_from_left, dist_from_top, sub_mat_cols, sub_mat_rows):
        for row in range(sub_mat_rows):
            row_in_parent_mat = row + dist_from_top
            for col in range(sub_mat_cols):
                col_in_parent_mat = col + dist_from_left
                self.matrix[row_in_parent_mat][col_in_parent_mat] += 1

    def fillSubMatrixByClaimId(self, cid, dist_from_left, dist_from_top, sub_cols, sub_rows):
        for row in range(sub_rows):
            row_in_parent = row + dist_from_top
            for col in range(sub_cols):
                col_in_parent = col + dist_from_left
                element = self.matrix[row_in_parent][col_in_parent]
                if type(element) is list:
                    self.matrix[row_in_parent][col_in_parent] = element + [cid]
                elif not element:
                    self.matrix[row_in_parent][col_in_parent] = cid
                elif element:
                    self.matrix[row_in_parent][col_in_parent] = [element] + [cid]

    def findCommonClaims(self):
        common_claims = set()
        for row in range(self.rows):
            for col in range(self.cols):
                if type(self.matrix[row][col]) is list:
                    [common_claims.add(e) for e in self.matrix[row][col]]
        return common_claims

    def findOverlapsInMatrix(self):
        no_of_overlaps = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.matrix[row][col] > 1:
                    no_of_overlaps += 1
        return no_of_overlaps


if __name__ == '__main__':
    # Initial Setup

    matrix = Matrix(8, 8)
    matrix.display()

    # Test code for puzzle 5th

    matrix.fillSubMatrix(1, 3, 4, 4)
    matrix.fillSubMatrix(3, 1, 4, 4)
    matrix.fillSubMatrix(5, 5, 2, 2)
    matrix.display()
    print("No. of overlaps in matrix:", matrix.findOverlapsInMatrix())

    # Test code for puzzle 6th

    matrix.reset()
    matrix.display()
    matrix.fillSubMatrixByClaimId(1, 1, 3, 4, 4)
    matrix.fillSubMatrixByClaimId(2, 3, 1, 4, 4)
    matrix.fillSubMatrixByClaimId(3, 1, 3, 6, 1)
    matrix.fillSubMatrixByClaimId(4, 5, 5, 2, 2)
    matrix.display()
    print("IDs of overlapped claims:", matrix.findCommonClaims())
