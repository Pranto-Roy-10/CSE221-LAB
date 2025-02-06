input_file=open("input1b_3.txt","r")
output_file=open("output1b_3.txt","w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
edges=[]
for x in range(m):
  edge = list(map(int, input_file.readline().split()))
  edges.append(edge)
def Adj_list(N,edge):
  a_lst={}
  for x in range(N+1):
    a_lst[x]=[]
  for x in edge:
    a,b,c=x
    a_lst[a].append((b,c))
  return a_lst
Adj_lst=Adj_list(n,edges)  
for x in range(n+1):
  output_file.write(f"{x} : ")
  if x in Adj_lst:
      for v, w in Adj_lst[x]:
        output_file.write(f"({v},{w}) ")
  output_file.write('\n')
input_file.close()
output_file.close()