input_file=open("input1b.txt","r")
output_file=open("output1b.txt","w")
red=input_file.readline().split(" ")
total_input=int(red[0])
sum=int(red[1])
next_red=input_file.readline().split()
checker1=0
checker2=0
left=0
right=len(next_red)-1
while left<total_input and right>0:
  if int(next_red[left])+int(next_red[right])==sum:
    if next_red[left]!=next_red[right]:
      checker1=left+1
      checker2=right+1
      break
    else:
      break
  elif int(next_red[left])+int(next_red[right])<sum:
    left+=1
  elif int(next_red[left])+int(next_red[right])>sum:
    right-=1

if checker1!=0:
  output_file.write(f"{checker1} {checker2}")
else:
  output_file.write("IMPOSSIBLE")
input_file.close()
output_file.close()