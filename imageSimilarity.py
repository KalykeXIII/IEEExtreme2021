# Task 2

class ImageSimilarity:
    def __init__(self):
        cases = int(float(input()))
            
        # Iterate through the test cases
        for i in range(cases):
            # For each test case; first get the number of rows and number of columns
            dimensions_1 = list(input().split(' '))
            print(dimensions_1)
            self.rows_1, self.columns_1 = int(float((dimensions_1[0]))), int(float((dimensions_1[1])))
            # Read the grid
            # Start i, end i, start j end j
            self.pos_1 = [[0, self.rows_1], [0, self.columns_1]]
            self.grid_1 = []
            for j in range(self.rows_1):
                self.grid_1.append(list(input()))
                
            # Add this to the big grid    
            
            # For each test case; first get the number of rows and number of columns
            dimensions_2 = list(input().split(' '))
            self.rows_2, self.columns_2 = int(float((dimensions_2[0]))), int(float((dimensions_2[1])))
            # Read the grid
            self.pos_1 = [[0, self.rows_1], [0, self.columns_1]]
            self.grid_2 = []
            for j in range(self.rows_2):
                self.grid_2.append(list(input()))
        
            # Add this to the big grid
        
    # Translate the grid
    # 0 = up
    # 1 = down
    # 2 = right
    # 3 = left
    def translate(self, dir):
        if dir:
            for j in range(self.big_ri):
                pass
        elif(dir): #down
            pass
        elif(dir == 2): #left
            pass
        else:
            return None

            
        
    
    # Rotate the grid 90 degrees clockwise
    def rotate(self):
        return None
    
    # FLip a grid horizonatally or vertically
    # Vertical = 0
    # Horizontal = 1
    def flip(self, dir):
        return None
            
    
    # Get a grid score
    def score(self):
        similarity = 0
        # Create a checking field 
        for i in range(30):
            for j in range(30):
                if self.big_grid1[i][j] == self.big_grid2[i][j] and self.big_grid1[i][j] == 1:
                    similarity += 1
        return similarity
                

if __name__ == "__main__":
    c = ImageSimilarity()
