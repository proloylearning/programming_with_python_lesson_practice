gradeDict = {'Kelly': 89, 'David': 65, 'Jack': 95, 'Samantha': 78}

print(gradeDict)
print(gradeDict['David'])

gradeDict['David'] = 56
print(gradeDict)

gradeDict['Jessy'] = 92
print(gradeDict)

del gradeDict['David']
print(gradeDict)

gradeDict = {'Kelly': [89, 88],
             'Jack': [95, 87],
             'Samantha': [78, 89],
             'Jessy': [92, 99]}

print(gradeDict)
print(gradeDict['Jessy'])
print(gradeDict['Jessy'][0])
gradeDict['Jessy'][1] = 95
print(gradeDict['Jessy'])

gradList = [
            {'name': 'Kelly', 'score': [89, 88]},
            {'name': 'Jack', 'score': [95, 87]},
            {'name': 'Samantha', 'score': [78, 89]},
            {'Jessy': 'Samantha', 'score': [92, 99]}
            ]
print(gradList)

for x in gradList:
    print(x)
