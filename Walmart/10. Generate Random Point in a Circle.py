class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center
        self.xmin = -self.r+self.x
        self.xmax = self.r+self.x
        self.ymin = -self.r+self.y
        self.ymax = self.r+self.y

    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(self.xmin,self.xmax)
            y = random.uniform(self.ymin,self.ymax)
            if (x-self.x)**2 + (y-self.y)**2 <= self.r**2:
                return [x,y]
