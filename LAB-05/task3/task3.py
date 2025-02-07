input_file=open("input3_1.txt","r")
output_file=open("output3_1.txt","w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
adjlst={i:[] for i in range(n+1)}
for x in range(m):
  u,v=input_file.readline().split()
  u,v=int(u),int(v)    
  adjlst[u].append(v)
def kosaraju(G):
  visited=[0]*(n+1)  
  stack=[]
  def dfs_topo(G,s,visited,stack):
    visited.append(s)
    for x in G[s]:
      if x not in visited:
        dfs_topo(G,x,visited,stack)
    stack.append(s)   
  def transpose_DFS(G,s,visited,strgly_c_c):
    visited.append(s)
    strgly_c_c.append(s)
    for x in G[s]:
      if x not in visited:
        transpose_DFS(G,x,visited,strgly_c_c)
  for x in G:
    if x!=0 and x not in visited:
      dfs_topo(G,x,visited,stack)
  transpose_graph={}
  for x in G:
    if x!=0:
      transpose_graph[x]=[]
  for x in G:
    if x!=0:
      for y in G[x]:
        if y!=0:
          transpose_graph[y].append(x)  
  visited.clear()
  scc_arr=[]
  while len(stack)>0:
    var=stack.pop()
    if var not in  visited:
      strgly_c_c=[]
      transpose_DFS(transpose_graph,var,visited,strgly_c_c)
      scc_arr.append(strgly_c_c)
  return scc_arr
call=kosaraju(adjlst)
for x in call:
  for y in x:
    output_file.write(f"{y} ")
  output_file.write("\n")
input_file.close()
output_file.close()
