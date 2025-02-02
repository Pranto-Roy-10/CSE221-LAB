input_file=open("input3.txt","r")
output_file=open("output3.txt","w")
red=int(input_file.readline())
lst=[]
for x in range(red):
  lst.append(input_file.readline().split())
for x in range(red):
  for y in range(red-1):
    if int(lst[y][1])>int(lst[y+1][1]):
      lst[y],lst[y+1]=lst[y+1],lst[y]
print(lst)      
start_time=int(lst[0][0])
end_time=int(lst[0][1])
count=1
lst1=[]
lst1.append(str(start_time)+" "+str(end_time))
for x in range(1,red):
  if int(lst[x][0])>=end_time:
    count+=1
    start_time=int(lst[x][0])
    end_time=int(lst[x][1])
    lst1.append(str(start_time)+" "+str(end_time))
output_file.write(str(count)+"\n")
for x in lst1:
  output_file.write(x+"\n")
output_file.close() 