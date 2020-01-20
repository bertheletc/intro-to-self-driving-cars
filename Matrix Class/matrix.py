import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

#Adding dot product function for use in multiplication method    
def dot_product(vector_one, vector_two):
    
    dot = 0
    
    for i in range(len(vector_one)):
        s = vector_one[i] * vector_two[i]
        dot += s
    
    return dot    

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            det = self.g[0][0]
        else:
            
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            
            det = a*d - b*c
         
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        n = self.h
        trace = 0
        
        for i in range(n):
            trace += self.g[i][i]
            
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse = []
        
        if self.h == 1:
            inverse = [[(1 / self.g[0][0])]]
        else:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1] 
        
            det = self.determinant()
        
            inverse = [[d, -b],
                      [-c, a]]
        
            for i in range(len(inverse)):
                for j in range(len(inverse[0])):
                    inverse[i][j] *= (1 / det)
                    
        return Matrix(inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = []
        
        for j in range(self.w):
            new_row = []
            for i in range(self.h):
                new_row.append(self.g[i][j])
            transpose.append(new_row)
        
        return Matrix(transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        added = []
        
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                s = self.g[i][j] + other.g[i][j]
                new_row.append(s)
            added.append(new_row)
    
        return Matrix(added)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        neg = []
        
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                new_row.append(self.g[i][j]* -1)
            neg.append(new_row)
                
        return Matrix(neg)

       
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        
        subtracted = []
        
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                s = self.g[i][j] - other.g[i][j]
                new_row.append(s)
            subtracted.append(new_row)
    
        return Matrix(subtracted)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        if self.w != other.h:
            raise(ValueError, "Matrices can only be multiplied if the inside dimensions are the same (m x n * n x p)") 
        
        product = []
    
        transposeOther = other.T()
    
        rows_A = self.h
        rows_Bt = transposeOther.h
    
        for i in range(rows_A):
            new_row = []
            for j in range(rows_Bt):
                new_row.append(dot_product(self.g[i],transposeOther.g[j]))
            product.append(new_row)
              
        return Matrix(product)
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #pass
            #   
            # TODO - your code here
            #
            multiplier = other
            new = self.g
        
            for i in range(self.h):
                for j in range(self.w):
                    new[i][j] *= multiplier
                
            return Matrix(new)
    
    
    
    
            