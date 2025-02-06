input_file=open("input6_2.txt","r")
output_file=open("output6_2.txt","w")
red=input_file.readline().split()
n=int(red[0])
m=int(red[1])
arr=[list(input_file.readline().strip())]
for x in range(n-1):
  arr.append(list(input_file.readline().strip())) 
def bfs(arr,a,b,c="#"):
  row_cnt=len(arr)
  col_cnt=len(arr[0])
  cnt=0
  if arr[a][b]==c:
    return cnt
  queue=[]
  queue.append((a,b))
  while len(queue)>0:
    a,b=queue.pop(0)
    if a<0 or a>=row_cnt or b<0 or b>=col_cnt or arr[a][b]==c:
      continue
    else:
      if arr[a][b]=="D":
        cnt+=1
      arr[a][b]=c
      queue.append((a+1,b))
      queue.append((a-1,b))
      queue.append((a,b+1))
      queue.append((a,b-1))
  return cnt
def flood_fill(arr):
  max_D=[0]
  row_cnt=len(arr)
  col_cnt=len(arr[0])
  for i in range(row_cnt):
    for j in range(col_cnt):
      total=0
      if arr[i][j]==".":
        total+=bfs(arr,i,j)
        max_D.append(total)
  return max(max_D)
Max_D=flood_fill(arr)
output_file.write(str(Max_D))
input_file.close()
output_file.close()