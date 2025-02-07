input_file=open("input1a_1.txt","r")
output_file=open("output1a_1.txt","w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
adjlst={i:[] for i in range(n+1)}
for x in range(m):
  u,v=input_file.readline().split()
  u,v=int(u),int(v)    
  adjlst[u].append(v)
print(adjlst)  
visited=[0]*(n+1)  
stack=[]
def dfs_topo(G,s,visited,stack):
  visited[s]=1
  for x in G[s]:
    if visited[x]==0:
      dfs_topo(G,x,visited,stack)
  stack.append(s)
def isCyclic(n):
  visited=[False]*(n+1)
  helper=[False]*(n+1)
  for x in range(n):
    if visited[x]==False:
      ans=dfs(x,visited,helper)
      if ans==True:
        return True
  return False
def dfs(s,visited,helper):
  visited[s]=True
  helper[s]=True
  neighbour=adjlst[s]
  for x in range(len(neighbour)):
    curr=neighbour[x]
    if helper[curr]==True:
      return True
    if visited[curr]==False:
      ans=dfs(curr,visited,helper)
      if ans==True:
        return True
  helper[s]=False
  return False
if isCyclic(n)==True:
  output_file.write('Impossible')
else:
  for x in range(1,len(adjlst)):
    if visited[x]==0:
      dfs_topo(adjlst,x,visited,stack)
  for x in range(len(stack)-1,-1,-1):
    output_file.write(f"{stack[x]}"" ")
input_file.close()
output_file.close()