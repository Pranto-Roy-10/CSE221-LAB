input_file=open("input1_2.txt", "r")
output_file=open("output1_2.txt", "w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
adjlst = {i:[] for i in range(n+1)}
for x in range(m):
  u,v,w=input_file.readline().split()
  u,v,w=int(u),int(v),int(w)
  adjlst[u].append([v,w])
s=int(input_file.readline())
print(adjlst)
print(s)
distance={i:float('inf') for i in range(1,n+1)}
visited={i:False for i in range(1,n+1)}
def extract_min(queue, dist):
  min_node=None
  min_dist=float('inf')
  for x in queue:
    if dist[x]<min_dist:
      min_node=x
      min_dist=dist[x]
  return min_node,min_dist
def dijkstra(G, s):
  distance[s]=0
  visited[s]=True
  p_queue=[s]
  while p_queue:
    n,d=extract_min(p_queue, distance)
    p_queue.remove(n)
    for x, wt in G[n]:
      new_distance=d+wt
      if new_distance<distance[x]:
        distance[x]=new_distance
        visited[x]=True
        p_queue.append(x)
  return distance,visited
f_dist,f_visit=dijkstra(adjlst,s)
for x in range(1,n+1):
  if not f_visit[x]:
      f_dist[x]=-1
  output_file.write(f"{f_dist[x]} ")
input_file.close()
output_file.close()