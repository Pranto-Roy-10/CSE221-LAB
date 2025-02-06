input_file=open("input2_1.txt","r")
output_file=open("output2_1.txt","w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
adlist={i:[] for i in range(n+1)}
for j in range(m):
  u,v=input_file.readline().split()
  u,v=int(u),int(v)
  adlist[u].append(v)
  adlist[v].append(u)
def BFS(G,s):
  visited=[]
  queue=[]
  visited.append(s)
  queue.append(s)
  while queue:
    var=queue.pop(0)
    output_file.write(f"{var} " "")
    for x in G[var]:
      if x not in visited:
        visited.append(x)
        queue.append(x)  
call=BFS(adlist,1)

input_file.close()
output_file.close()