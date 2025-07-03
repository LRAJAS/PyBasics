class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def move (self):
        print("move")
        
    def draw (self):
        print("draw")
        
    
point1 = Point(10,20)
point1.x = 5
point1.y = 10
point1.z = 20
print(point1)        
        