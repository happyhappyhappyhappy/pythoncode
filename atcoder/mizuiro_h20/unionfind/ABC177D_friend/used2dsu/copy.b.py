class dsu():
    n=1
    parent_or_size=[-1 for _ in range(0,n)]
    def __init__(self,N):
        self.n=N
        self.parent_or_size=[-1 for _ in range(0,N)]
    def merge(self,a,b):
        assert 0<=a<self.n,"0<=a<n,a={0},n={1}".format(a,self.n)
        assert 0<=b<self.n,"0<=b<n,b={0},n={1}".format(b,self.n)
        x=self.leader(a)
        y=self.leader(b)
        if x == y:
            return x
        if(-self.parent_or_size[x] < -self.parent_or_size[y]):
            x,y = y,x
        self.parent_or_size[x]=self.parent_or_size[x]+parent_or_size[y]
        self.parent_or_size[y]=x
        return x
    def same(self,a,b):
        assert 0<=a<self.n,"0<=a<n,a={0},n={1}".format(a,N)
        assert 0<=b<self.n,"0<=b<n,b={0},n={N}".format(b,N)
        return self.leader(a)==self.leader(b)
    def leader(self,a):
        assert 0<=a<self.n,"0<=a<n,a={0},n={1}".format(a,N)
        if self.parent_or_size[a]<0:
            return a
        self.parent_or_size[a]=self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]
    def size(self,a):
        assert 0<=a<self.n,"0<=a<n,a={0},n={1}".format(a,self.n)
        return (-1)*self.parent_or_size[self.leader(a)]
    def groups(self):
        leader_buf=[0 for _ in range(0,self.n)]
        group_buf=[0 for _ in range(0,self.n)]
        for j in range(0,self.n):
            leader_buf[j]=self.leader[j]
            group_size[leader_buf[j]]=group_size[leader_buf[j]]+1
        result=[[] for _ in range(0,self.n)]
        for j in range(0,self.n):
            result[leader_buf[j]].append[j]
        result2=[]
        for j in range(0,self.n):
            if 0 < len(result[i]):
                result2.append(result[j])
        return result2
