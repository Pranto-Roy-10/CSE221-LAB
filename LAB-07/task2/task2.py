input=open('input2_1.txt','r')
output=open('output2_1.txt','w')
red=input.readlines()
n,m= map(int,red[0].split())
edges=[]
cnt=1
for x in range(m):
  u,v,w= map(int,red[cnt].split())
  u-=1 
  v-=1  
  edges.append((w,u,v))
  cnt+=1
edges.sort()
class UnionFind:
  def __init__(self,n):
    self.parent=list(range(n))
    self.rank=[0]*n
  def find(self,a):
    if self.parent[a]!=a:
        self.parent[a]=self.find(self.parent[a]) 
    return self.parent[a]
  def union(self, a, b):
    var1= self.find(a)
    var2= self.find(b)
    if var1!=var2:
      if self.rank[var1]>self.rank[var2]:
        self.parent[var2]=var1
      elif self.rank[var1]<self.rank[var2]:
        self.parent[var1]=var2
      else:
        self.parent[var2]=var1
        self.rank[var1]+=1
      return True
    return False
call=UnionFind(n)
mst_cost=0
edges_in_mst=0
for w,u,v in edges:
    if call.find(u)!=call.find(v) and call.union(u,v):  
      mst_cost+=w
      edges_in_mst+=1
      if edges_in_mst==n- 1:
          break
output.write(f'{mst_cost}')
input.close()
output.close()