input_file=open("input2_3.txt","r")
output_file=open("output2_3.txt","w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
adjlst={i:[] for i in range(n+1)}
for x in range(m):
  u,v=input_file.readline().split()
  u,v=int(u),int(v)    
  adjlst[u].append(v)
print(adjlst)  
def bfs_topo(G):
  n=len(G)
  indegree=[0]*(n)
  for x in range(0,len(G)):
    for t in G[x]:
      indegree[t]+=1
  queue=[]
  for x in range(len(G)):
    if indegree[x]==0:
      queue.append(x)
  idx=0    
  order=[]
  while len(queue)>0:
    min_val=min(queue)
    queue.remove(min_val)
    order.append(min_val)
    idx+=1
    for x in G[min_val]:
      indegree[x]-=1
      if indegree[x]==0:
        queue.append(x)
  if idx!=n:
    return "IMPOSSIBLE"
  return order 
topo=bfs_topo(adjlst)
if topo=="IMPOSSIBLE":
  output_file.write("Impossible")
else:
  for x in range(1,len(topo)):
    output_file.write(f"{topo[x]}"" ")
input_file.close()
output_file.close()