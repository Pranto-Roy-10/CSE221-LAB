input_file=open("input1a_2.txt","r")
output_file=open("output1a_2.txt","w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
edges=[]
for x in range(m):
  edge = list(map(int, input_file.readline().split()))
  edges.append(edge)

def Adj_matrix(N,m,edge):
  arr1=[]
  for a in range(N+1):
    row=[0]*(N+1)
    arr1.append(row)
  for x in edge:
    a,b,c=x
    arr1[a][b]=c

  return arr1
mat=Adj_matrix(n,m,edges)
for row in mat:
  for element in row:
      output_file.write(str(element) + " ")
  output_file.write("\n")
input_file.close()
output_file.close()

