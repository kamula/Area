class RectangleArea:
    '''
    Class that calculates the area of a Rectangle
    '''    
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def rectangle_area(self):
        '''method that calculates the area of a rectangle'''
        area = self.length * self.width
        return f'area of the Rectangle is {area}'

rectangle1 = RectangleArea(7,4)
print(rectangle1.rectangle_area())
    