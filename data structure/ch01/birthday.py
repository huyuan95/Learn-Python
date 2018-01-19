import random
birthday = {
    'month': 0,
    'day': 0
}
count = 0
for i in range(5, 105, 5):
    persons=[]
    for j in range(i):
        birthday['month'] = random.randint(1, 12)
        birthday['day'] = random.randint(1, 31)
        persons.append(birthday.copy())
    for person in persons:
        p = person
        for person in persons:
            if p['month'] == person['month'] and p['day'] == person['day']:
                count += 1
    if count > i:
        print('True',i)
    else:
        print('False', i)
    count = 0
