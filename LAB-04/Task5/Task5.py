from collections import deque
input_file=open("input5_2.txt","r")
output_file=open("output5_2.txt","w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
d=int(red[2])
adlist={i:[] for i in range(n+1)}
for j in range(m):
  u,v=input_file.readline().split()
  u,v=int(u),int(v)
  adlist[u].append(v)
  adlist[v].append(u)
def bfs(G,s,d):
  if s==d:
    return [s], 0
  queue=[(s,[s],0)]
  visited=[]
  while queue:
    a,b,c=queue.pop(0)
    if a==d:
      return b,c
    visited.append(a)
    for x in G[a]:
      if x not in visited:
        queue.append((x,b+[x],c+1))
        visited.append(x)
path,s_time=bfs(adlist,1,d)
output_file.write(f"Time: {s_time}\n")
output_file.write(f"Shortest path: ")
for x in path:
  output_file.write(f"{x} ")
input_file.close()
output_file.close()