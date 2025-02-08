input_file = open("input3_1.txt", "r")
output_file = open("output3_1.txt", "w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
adjlst={i:[] for i in range(n+1)}
for x in range(m):
  u,v,w=input_file.readline().split()
  u,v,w=int(u),int(v),int(w)    
  adjlst[u].append([v,w])
print(adjlst)
def extract_min(queue, dist):
  min_node=None
  min_dist=float('inf')
  for x in queue:
    if dist[x]<min_dist:
      min_node=x
      min_dist=dist[x]
  return min_node,min_dist
def dijkstra(G,s,var):
  distance={i:float('inf') for i in range(1,len(G)+1)}
  visited={i:False for i in range(1,len(G)+1)}
  distance[s]=0
  visited[s]=True
  p_queue=[s]
  while p_queue:
    n,d=extract_min(p_queue, distance)
    p_queue.remove(n)
    if n==var:
      return d,distance
    for x, wt in G[n]:
      new_distance=max(d,wt)
      if new_distance<distance[x]:
        distance[x]=new_distance
        visited[x]=True
        p_queue.append(x)
  return "Impossible" 
result,dist=dijkstra(adjlst,1,n)
print(dist)
output_file.write(str(result))
input_file.close()
output_file.close()
