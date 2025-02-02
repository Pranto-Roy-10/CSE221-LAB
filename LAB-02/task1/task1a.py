input_file=open("input1a.txt","r")
output_file=open("output1a.txt","w")
red=input_file.readline().split()
total_input=int(red[0])
sum=int(red[1])
next_red=input_file.readline().split()
checker1=0
checker2=0
for x in range(total_input):
  for y in range(x+1,total_input):
    if int(next_red[x])+int(next_red[y])==sum:
      checker1=x+1
      checker2=y+1
if checker1!=0:
  output_file.write(f"{checker1} {checker2}")
else:
  output_file.write("IMPOSSIBLE")
input_file.close()  
output_file.close()