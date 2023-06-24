class Aligners:
    
    def __init__(self) -> None:
        pass
    
    def align_left(self, vector = [], width = 0, height = 0):
        '''
        align the left point of the vector to the first column
        '''
        old = vector 
        left_point = 0
        
        for y in range(height - 1):
            if left_point > 0:
                break
            for x in range(width - 1):
                if vector[x + y * width] > 0:
                    left_point = x
                    break
        
        if left_point > 0:
            for y in range(height - 1):
                slice = vector[y * width : width + y * width]
                for x in range(left_point):
                    slice.pop(0)
                    slice.append(0)
                    vector[y * width : width + y * width] = slice

        return vector

    def align_top(self, vector = [], width = 0, height = 0):
        '''
        align the top point of the vector to the first row
        '''
        highest_point = 0
        
        for x in range(width - 1):
            if highest_point > 0:
                break
            for y in range(height - 1):
                if vector[x + y * width] > 0:
                    highest_point = y
                    break
        
        if highest_point > 0:
            for x in range(width):
                for y in range(highest_point):
                    vector.pop(0)
                    vector.append(0)
                    
        return vector