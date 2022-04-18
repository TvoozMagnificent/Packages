# we attempt to make a matrix class
# WE WILL NOT USE ANY OTHER PACKAGES
# define MatrixError

class MatrixError(Exception):
    """An error class for PythonMatrixClass"""
    pass

class Matrix(object): # for compatibility
    def __init__(self, values):
        # the input values should look like
        # [[1,2,3],[4,5,6]]
        # and we will store them as a list of lists
        self.values = values

    def get_row(self, row):
        # return the specified row
        # the row is a number
        # the first row is row 0
        # the second row is row 1
        # and so on
        # we will return a list of numbers
        # for instance, the following matrix
        # [[1,2,3],[4,5,6]]
        # will return
        # [1,2,3]
        # for row 0
        # [4,5,6]
        # for row 1
        # if the row does not exist, raise a MatrixError
        if row < 0 or row >= len(self.values):
            raise MatrixError("Row {} does not exist. "
                              "Valid rows are 0 to {}, "
                              "as your matrix is {}".format(row, len(self.values)-1, self.values))
        return self.values[row]

    def flip_diag(self):
        # flip diagonally
        # for instance, the following matrix
        # [[1,2,3],[4,5,6]]
        # will return
        # [[1,4],[2,5],[3,6]]

        # we will return a new matrix
        # we will use the list of lists constructor

        return Matrix([[self.values[i][j] for i in range(len(self.values))] for j in range(len(self.values))])

    def transpose(self):
        # same as flip diag
        return self.flip_diag()

    def flip_hor(self):
        # flip horizontally
        # for instance, the following matrix
        # [[1,2,3],[4,5,6]]
        # will return
        # [[3,2,1],[6,5,4]]
        return Matrix([[self.values[i][j] for i in range(len(self.values))] for j in range(len(self.values))[::-1]])

    def flip_ver(self):
        # flip vertically
        # for instance, the following matrix
        # [[1,2,3],[4,5,6]]
        # will return
        # [[4,5,6],[1,2,3]]
        return Matrix([[self.values[i][j] for i in range(len(self.values))[::-1]] for j in range(len(self.values))])

    def flip_both(self):
        # flip both horizontally and vertically
        # for instance, the following matrix
        # [[1,2,3],[4,5,6]]
        # will return
        # [[6,5,4],[3,2,1]]
        return self.flip_ver().flip_hor()

    def get_col(self, col):
        # return the specified column
        # use the get_row function and transpose

        return self.transpose().get_row(col)

    def get_val(self, row, col):
        # return the value at the specified row and column
        # use the get_row and get_col functions
        return self.get_row(row)[col]

    def duplicate(self):
        # duplicate the matrix
        # return a new matrix
        # beware of the deep copy
        return Matrix([[x for x in row] for row in self.values])

    def __str__(self):
        # return a string representation of the matrix
        # for instance, the following matrix
        # [[1,2,3],[4,5,6]]
        # should return the string
        # 1 2 3
        # 4 5 6
        # we will use a new line for each row
        # and we will use a space for each element

        return "\n".join([" ".join([str(x) for x in row]) for row in self.values])

    def __add__(self, other):
        # add two matrices
        # return a new matrix
        # we will assume that the matrices are the same size
        # and that they are both matrices
        # else, we will raise a MatrixError

        # check if both are matrices
        if not isinstance(other, Matrix):
            raise MatrixError("Cannot add matrix to non-matrix. "
                              "Consider changing your input format to matrix. "
                              "For Debug: Input is {}, class {}".format(other, type(other)))
        # check if both are the same size
        if len(self.values) != len(other.values):
            raise MatrixError("Cannot add matrices of different sizes. "
                              "Consider using get_rows or get_cols to get the correct size. "
                              "For Debug: Input is {}, Row number is {}".format(other, len(other.values)))
        # check if both are the same size
        if len(self.values[0]) != len(other.values[0]):
            raise MatrixError("Cannot add matrices of different sizes. "
                              "Consider using get_rows or get_cols to get the correct size. "
                              "For Debug: Input is {}, Column number is {}".format(other, len(other.values[0])))
        # check if all elements are numbers. Int and Float are all acceptable
        for row in self.values:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise MatrixError("Cannot add matrices with non-numeric elements. "
                                      "Consider changing your input format to numbers. "
                                      "For Debug: Input is {}, class {}".format(element, type(element)))
        for row in other.values:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise MatrixError("Cannot add matrices with non-numeric elements. "
                                      "Consider changing your input format to numbers. "
                                      "For Debug: Input is {}, class {}".format(element, type(element)))
        # add the matrices
        return Matrix([[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(self.values, other.values)])

    def __sub__(self, other):
        # subtract two matrices
        # return a new matrix
        # do the same as __add__

        # check if both are matrices
        if not isinstance(other, Matrix):
            raise MatrixError("Cannot subtract matrix from non-matrix. "
                              "Consider changing your input format to matrix. "
                              "For Debug: Input is {}, class {}".format(other, type(other)))
        # check if both are the same size
        if len(self.values) != len(other.values):
            raise MatrixError("Cannot subtract matrices of different sizes. "
                              "Consider using get_rows or get_cols to get the correct size. "
                              "For Debug: Input is {}, Row number is {}".format(other, len(other.values)))
        # check if both are the same size
        if len(self.values[0]) != len(other.values[0]):
            raise MatrixError("Cannot subtract matrices of different sizes. "
                              "Consider using get_rows or get_cols to get the correct size. "
                              "For Debug: Input is {}, Column number is {}".format(other, len(other.values[0])))
        # check if all elements are numbers. Int and Float are all acceptable
        for row in self.values:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise MatrixError("Cannot subtract matrices with non-numeric elements. "
                                      "Consider changing your input format to numbers. "
                                      "For Debug: Input is {}, class {}".format(element, type(element)))
        for row in other.values:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise MatrixError("Cannot subtract matrices with non-numeric elements. "
                                      "Consider changing your input format to numbers. "
                                      "For Debug: Input is {}, class {}".format(element, type(element)))
        # subtract the matrices
        return Matrix([[x - y for x, y in zip(row1, row2)] for row1, row2 in zip(self.values, other.values)])

    def __mul__(self, other):
        # multiply two matrices
        # return a new matrix

        # multiplication is a little different
        # check if both are matrices
        if not isinstance(other, Matrix):
            try: return self.__rmul__(other)
            except: raise MatrixError("Cannot multiply matrix with non-matrix. "
                                      "Consider changing your input format to matrix. "
                                      "For Debug: Input is {}, class {}".format(other, type(other)))
        # check if all elements are numbers. Int and Float are all acceptable
        for row in self.values:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise MatrixError("Cannot multiply matrices with non-numeric elements. "
                                      "Consider changing your input format to numbers. "
                                      "For Debug: Input is {}, class {}".format(element, type(element)))
        for row in other.values:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise MatrixError("Cannot multiply matrices with non-numeric elements. "
                                      "Consider changing your input format to numbers. "
                                      "For Debug: Input is {}, class {}".format(element, type(element)))
        # check if the number of columns in the first matrix is equal to the number of rows in the second matrix
        if len(self.values[0]) != len(other.values):
            raise MatrixError("Cannot multiply matrices of 'strange' sizes. "
                              "Consider using get_rows or get_cols to get the correct size. "
                              "For Debug: Input is {}, Column number is {}".format(other, len(other.values[0])))

        # multiply the matrices
        # beware the 80-character line length
        # iterate through each row of the first matrix, for each row, iterate through elements
        # and multiply them with the corresponding element in the second matrix

        # for instance, if the first matrix is [[1, 2], [3, 4]]
        # and the second matrix is [[5, 6], [7, 8]]
        # then the result is [[17, 27], [39, 33]] because:
        # 1 * 5 + 2 * 6 = 5 + 12 = 17
        # 1 * 7 + 2 * 8 = 3 + 24 = 27
        # 3 * 5 + 4 * 6 = 15 + 24 = 39
        # 3 * 7 + 4 * 8 = 9 + 32 = 33
        return Matrix([[sum(x * y for x, y in zip(row1, row2)) for row2 in other.values] for row1 in self.values])

    def __rmul__(self, other):
        # multiply a matrix with a number
        # return a new matrix

        # check if the number is a number
        if not isinstance(other, (int, float)):
            raise MatrixError("Cannot multiply matrix with non-numeric elements. "
                              "Consider changing your input format to numbers. "
                              "For Debug: Input is {}, class {}".format(other, type(other)))
        # check if all elements are numbers. Int and Float are all acceptable
        for row in self.values:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise MatrixError("Cannot multiply matrices with non-numeric elements. "
                                      "Consider changing your input format to numbers. "
                                      "For Debug: Input is {}, class {}".format(element, type(element)))
        # multiply the matrix with the number
        return Matrix([[element * other for element in row] for row in self.values])

    def determinant(self):
        # calculate the determinant of a matrix
        # return the determinant
        # raise an error if the matrix is not square
        if len(self.values) != len(self.values[0]):
            raise MatrixError("Cannot calculate the determinant of a non-square matrix. "
                              "For Debug: Input is {}".format(self))
        # check if all elements are numbers. Int and Float are all acceptable
        for row in self.values:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise MatrixError("Cannot calculate the determinant of a matrix with non-numeric elements. "
                                      "Consider changing your input format to numbers. "
                                      "For Debug: Input is {}, class {}".format(element, type(element)))
        # calculate the determinant
        # if the matrix is a 2x2 matrix, then the determinant is the product of the diagonal elements
        # if the matrix is a 3x3 matrix, then the determinant is the sum of the products of the diagonal elements
        # and the products of the elements in the first column and the elements in the first row
        # if the matrix is a 4x4 matrix, then the determinant is the sum of the products of the diagonal elements
        # and the products of the elements in the first column and the elements in the first row
        # and the products of the elements in the first row and the elements in the second column
        # and the products of the elements in the second row and the elements in the third column
        # and the products of the elements in the third row and the elements in the fourth column
        # and the products of the elements in the fourth row and the elements in the second column
        if len(self.values) == 2:
            return self.values[0][0] * self.values[1][1] - self.values[0][1] * self.values[1][0]
        elif len(self.values) == 3:
            return self.values[0][0] * self.values[1][1] * self.values[2][2] + \
                   self.values[0][1] * self.values[1][2] * self.values[2][0] + \
                   self.values[0][2] * self.values[1][0] * self.values[2][1] - \
                   self.values[0][2] * self.values[1][1] * self.values[2][0] - \
                   self.values[0][1] * self.values[1][0] * self.values[2][2] - \
                   self.values[0][0] * self.values[1][2] * self.values[2][1]
        else:
            # use recursion to calculate the determinant

            # for instance, the determinant of [[a,b,c,d],[e,f,g,h],[i,j,k,l],[m,n,o,p]] is
            # a*det([[f,g,h],[j,k,l],[n,o,p]])-
            # b*det([[e,g,h],[i,k,l],[m,o,p]])+
            # c*det([[e,f,h],[i,j,l],[m,n,p]])-
            # d*det([[e,f,g],[i,j,k],[m,n,o]])

            return sum([self.values[0][i] * (-1) ** i * self.submatrix(0, i).determinant() for i in range(len(self.values))])

    def submatrix(self, row, column):
        # return a new matrix with the specified row and column removed
        # raise an error if the row or column is out of range
        if row < 0 or row >= len(self.values):
            raise MatrixError("Row {} is out of range. For Debug: Input is {}".format(row, self))
        if column < 0 or column >= len(self.values):
            raise MatrixError("Column {} is out of range. For Debug: Input is {}".format(column, self))
        # create a new matrix with the specified row and column removed
        # if the matrix is a 2x2 matrix, then the new matrix is a 1x1 matrix
        # if the matrix is a 3x3 matrix, then the new matrix is a 2x2 matrix
        # if the matrix is a 4x4 matrix, then the new matrix is a 3x3 matrix
        new_values = []
        for i in range(len(self.values)):
            if i == row:
                continue
            new_values.append([])
            for j in range(len(self.values)):
                if j == column:
                    continue
                new_values[-1].append(self.values[i][j])
        return Matrix(new_values)

    def cofactor_item(self, row, column):
        # return the cofactor of the element at the specified row and column
        # raise an error if the row or column is out of range
        if row < 0 or row >= len(self.values):
            raise MatrixError("Row {} is out of range. For Debug: Input is {}".format(row, self))
        if column < 0 or column >= len(self.values):
            raise MatrixError("Column {} is out of range. For Debug: Input is {}".format(column, self))
        # use recursion to calculate the cofactor
        # if the matrix is a 2x2 matrix, then the cofactor is the determinant of the submatrix
        # if the matrix is a 3x3 matrix, then the cofactor is the determinant of the submatrix
        # if the matrix is a 4x4 matrix, then the cofactor is the determinant of the submatrix
        return (-1) ** (row + column) * self.submatrix(row, column).determinant()

    def cofactor(self):
        # return the cofactor matrix of the current matrix
        # raise an error if the matrix is not square
        if len(self.values) != len(self.values[0]):
            raise MatrixError("Cofactor matrix is only defined for square matrices. "
                              "For Debug: Input is {}".format(self))
        # create a new matrix with the cofactor of each element

        return Matrix([[self.cofactor_item(i, j) for j in range(len(self.values))] for i in range(len(self.values))])

    def adjugate(self):
        # return the adjugate matrix of the current matrix
        # raise an error if the matrix is not square
        if len(self.values) != len(self.values[0]):
            raise MatrixError("Adjugate matrix is only defined for square matrices. "
                              "For Debug: Input is {}".format(self))
        # use the cofactor matrix to calculate the adjugate matrix
        return self.cofactor().transpose()

    def det(self):
        # shortcut for the determinant
        return self.determinant()

    def adj(self):
        # shortcut for the adjugate
        return self.adjugate()

    def inverse(self):
        # return the inverse matrix of the current matrix
        # raise an error if the matrix is not square or not invertible
        if len(self.values) != len(self.values[0]):
            raise MatrixError("Inverse matrix is only defined for square matrices. "
                              "For Debug: Input is {}".format(self))
        if self.determinant() == 0:
            raise MatrixError("Inverse matrix is not defined for matrices with determinant 0. "
                              "For Debug: Input is {}".format(self))
        # use the adjugate matrix to calculate the inverse matrix
        return self.adjugate() / self.determinant()

    def __truediv__(self, other):
        # multiply the current matrix by the inverse of the other matrix
        try: return self * other.inverse()
        except AttributeError:
            try: return self * Matrix(other).inverse()
            except TypeError: return self.__rtruediv__(other)


    def __rtruediv__(self, other):
        # multiply the matrix by the reciprocal of the given number
        return self * (1 / other)

    def __div__(self, other): # for compatibility
        return self.__truediv__(other)

    def __rdiv__(self, other): # for compatibility
        return self.__rtruediv__(other)

class IdentityMatrix(Matrix):
    def __init__(self, n):
        super().__init__([[1 if i == j else 0 for j in range(n)] for i in range(n)])

class ZeroMatrix(Matrix):
    def __init__(self, n):
        super().__init__([[0 for j in range(n)] for i in range(n)])
