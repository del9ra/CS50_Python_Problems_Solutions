dict={}
name_list=[]
numbers_list=[]
while True:
    try:
        item = input("").upper()
        name_list.append(item)
    except EOFError:
        break
name_list.sort()
for i in name_list:
    n=name_list.count(i)
    numbers_list.append(n)

for j in range(0,len(name_list)):
    dict[name_list[j]] = numbers_list[j]


for name, number in dict.items():
    print(number, name)
