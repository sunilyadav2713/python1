import sys
import json
filename=sys.argv[1]
fiobj=open(filename)
data=json.load(fiobj)
fiobj.close()
room_type=input('enter the room type like (Small , Phone Booth, Medium, Large ): ')
rooms_info=[]
rooms=[]
for i in data:
    for j in i:
        for k,x in j.items():
            if k=='conference-categories-count':
                for y,z in x.items():
                    if y==room_type:
                        rooms_info.append(z)
                        rooms.append((y,z))
total=0                    
for p in rooms_info:
    total+=p
avg=total/len(rooms_info)
print(rooms)
print(rooms_info)
print(avg)

    

