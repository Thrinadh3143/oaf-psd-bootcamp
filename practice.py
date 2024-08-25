list = [1,2,2,3,3,4,4,4]


def remove_duplicates(l1):
    new_lst = []
    for items in l1:
        if items not in new_lst:
            new_lst.append(items)
    global list= new_lst

            
remove_duplicates(list)

print(list)
