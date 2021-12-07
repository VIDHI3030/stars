import csv 
data1=[]
data2=[]
with open("bright_stars.csv","r",encoding='utf8') as f:
    r=csv.reader(f)
    for row in r :
        data1.append(row)

headers1=data1[0]
star_data1=data1[1:]

with open("dwarf_stars.csv","r",encoding='utf8') as f:
    r=csv.reader(f)
    for row in r :
        data2.append(row)

headers2=data2[0]
star_data2=data2[1:]
headers=headers1+headers2
star_data=[]
for i in star_data1:
    star_data.append(i)
for j in star_data2:
    star_data.append(j)

with open("totalstars.csv","a+",encoding='utf8') as f:
    writer=csv.writer(f)
    writer.writerow(headers)
    writer.writerows(star_data)


