input_file=open("input4_5.txt","r")
output_file=open("output4_5.txt","w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
adlist={i:[] for i in range(n+1)}
for j in range(m):
  u,v=input_file.readline().split()
  u,v=int(u),int(v)
  adlist[u].append(v)
Red=[0]*(n+2)
Blue=[0]*(n+2)
result=["NO"]
stack=[]
def DFS(x):
  Red[x] = 1
  stack.append(x)
  for i in adlist[x]:
    if Red[i] != 1:
      DFS(i)
      stack.pop()
      Blue[i] = x
    elif Red[i] == 1 and Blue[i] != x and i in stack:
      result[0] = "YES"
DFS(1)
output_file.write(f"{result[0]}")
input_file.close()
output_file.close()