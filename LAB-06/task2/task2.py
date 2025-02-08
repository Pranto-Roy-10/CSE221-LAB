input_file = open("input2_3.txt", "r")
output_file = open("output2_3.txt", "w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
adjlst={i:[] for i in range(n+1)}
for x in range(m):
  u,v,w=input_file.readline().split()
  u,v,w=int(u),int(v),int(w)    
  adjlst[u].append([v,w])
both_s=input_file.readline().split()
a_s=int(both_s[0])
b_s=int(both_s[1])
print(adjlst)
print(a_s)
print(b_s)
def extract_min(queue, dist):
  min_node=None
  min_dist=float('inf')
  for x in queue:
    if dist[x]<min_dist:
      min_node=x
      min_dist=dist[x]
  return min_node,min_dist
def dijkstra(G,s):
  distance={i:float('inf') for i in range(1,len(G)+1)}
  visited={i:False for i in range(1,len(G)+1)}
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
  return distance
a_dist=dijkstra(adjlst,a_s)
b_dist=dijkstra(adjlst,b_s)
print(a_dist)
print(b_dist)
last_checker_Arr=[]*(n+1)
for x in range(1,n+1):
  if a_dist[x]>b_dist[x]:
    last_checker_Arr.append(a_dist[x])
  else:
    last_checker_Arr.append(b_dist[x])
print(last_checker_Arr)    
min=float('inf')
count=0
for x in range(n):
  if last_checker_Arr[x]<min:
    min=last_checker_Arr[x]
    count=x+1 
if min==float('inf'):
  output_file.write(f"Impossible")
else: 
  output_file.write(f"Time {min}\nNode {count}")
input_file.close()
output_file.close()