filenames = ['1.doc','2.report','3.presentation']
lst = []
for item in filenames:
    item = item.replace('.','-',1)+'.txt'
    lst.append(item)

print(lst)

