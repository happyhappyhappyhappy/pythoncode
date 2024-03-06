class Levenshtein:
    def initArary(self,str1,str2):
        distance=[]
        for j in range(len(str1)+1):
            distance.append([0]*(len(str2)+1))
            distance[j][0]=1
        for k in range(len(str2)+1):
            distance[0][k]=k
        return distance
    def editDist(self,str1,str2,distance):
        dist=[0]*3
        for i in range(1,len(str1)+1):
            for j in range(1,len(str2)+1):
                dist[0]=distance[i-1][j-1] if str1[i-1]==str2[j-1] else distance[i-1][j-1]+1
                dist[1]=distance[i][j-1]+1
                dist[2]=distance[i-1][j]+1
                distance[i][j]=min(dist)
        return distance[i][j]
    def __init__(self,str1,str2):
        self.str1=str1
        self.str2=str2
        Levenshtein.distance=self.initArary(str1,str2)
        Levenshtein.dist=self.editDist(str1,str2,Levenshtein.distance)
if __name__=="__main__":
    str1 = "やまなか"
    str2 = "やかまか"
    leven=Levenshtein(str1,str2)
    print(leven.dist)
