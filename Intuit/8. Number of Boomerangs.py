class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        points={(point[0],point[1]) for point in points}
        output=0
        
        for center in points:
            dists=collections.defaultdict(int)
            for other in points:
                dist=self.distance(center,other)
                dists[dist]+=1
            for dist in dists:
                output+=int(dists[dist]*(dists[dist]-1))
        return output
    
    def distance(self, point,other):
        x_point,y_point=point
        x_other,y_other=other
        x_delta=x_other-x_point
        y_delta=y_other-y_point
        return x_delta**2+y_delta**2
