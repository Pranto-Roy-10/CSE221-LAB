input_file=open("input3_4.txt","r")
output_file=open("output3_4.txt","w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
adlist={i:[] for i in range(n+1)}
for j in range(m):
  u,v=input_file.readline().split()
  u,v=int(u),int(v)
  adlist[u].append(v)
  adlist[v].append(u)
color={}
for x,y in adlist.items():
    if y!=[]:
        color[x]=0
def DFS(G,x):
  color[x]=1
  output_file.write(f"{x} ")
  for v in G[x]:
    if color[v]==0:
      DFS(G,v)
call=DFS(adlist,1)

input_file.close()
output_file.close()