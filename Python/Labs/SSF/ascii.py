list1 = []     # List 1
list2 = []     # List 2

for num in range(65,91):
    c1 = (num,chr(num))     # convert to ASCII
    # print(c1)               # print c1 list
    list1.append(c1)       # Adding items to List 1

for num in range(97,123):
    c2 = (num,chr(num))     # convert to ASCII
    # print(c2)
    list2.append(c2)       # Adding items to List 2

allcolumns = list1, list2    #creating allcolumns = listc1 + listc2

# newlist12 = ()
# newlist34 = ()

for column1 in allcolumns[0]:
    set1 = column1[0]
    set2 = column1[1]
    sets12 = (set1, set2)
    # print(sets12)
    # newlist12.append(sets12)       # Adding items to List 1

for column2 in allcolumns[1]:
    set3 = column2[0]
    set4 = column2[1]
    sets34 = (set3, set4)
    # print(sets34)
    # newlist34.append(sets34)       # Adding items to List 1

    print(sets12, sets34)
# print(newlist12, newlist34)


# print(newlist12)
    # print(sets12)


        # print(column1, column2)

#     stuff1 = (column1[0])
#     print(stuff1)
# #
# for column2 in list2:
#     stuff2 = (column2[0], column2[1])
#     item2 = (stuff2[0], stuff2[1])
#     # print(item2)
#
# while(integer < 10):
#     square = integer ** 2
#     cube = integer ** 3
#     print(integer,square,cube)
#     integer += 1






# for i, (item1, item2) in (list1, list2):
#     print(i, item1, item2)




# print(item1[0], item2)





# stuff2 = listc2
# print(stuff1, stuff2)

# print(listc1[0], listc2[0])
# allcolumns = listc1,listc2    #creating allcolumns = listc1 + listc2
# # print(allcolumns)
#
# for item1 in allcolumns:
#     print(item1[0], item1[1])
# #
# for column in allcolumns:           # for each column in all allcolumns
#     for item in column:             # for each iten in each column
#         print(item[0])              # show item
#         #listc2[27])
