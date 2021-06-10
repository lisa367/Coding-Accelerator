fichier1 = \
"""123
323
123"""

fichier2 = \
"""930870
081235
973217
091230
883700"""

rectangle1 = fichier1.split('\n')
rectangle2 = fichier2.split('\n')
coordinates = 0
#print(rectangle1)
#print(rectangle2)

for y in range(len(rectangle2)) :
    if rectangle1[0] in rectangle2[y] :
        x = rectangle2[y].find(rectangle1[0])
        coordinates = (x,y)
        break
for i in range(len(rectangle1)) :
    pass
print('Coordinates :', coordinates)