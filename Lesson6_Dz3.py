import json
import sys

hobby_list = []
user_list = []
user_dict = {}

with open('users.csv', 'r', encoding='utf-8') as f1:
    line = f1.readline()
    f1.seek(0)
    for line in f1:
        el = line.strip('\n').split(',')
        user_list.append(','.join(el))

with open('hobby.csv', 'r', encoding='utf-8') as f2:
    line = f2.readline()
    f2.seek(0)
    for line in f2:
        el = line.strip('\n').split(',')
        hobby_list.append(','.join(el))

if len(hobby_list) > len(user_list):
    sys.exit(1)
elif len(hobby_list) < len(user_list):
    delta = abs(len(hobby_list) - len(user_list))
    while delta > 0:
        hobby_list.append('None')
        delta -= 1

delta = len(hobby_list) - len(user_list)
users_dict = {key: val for key, val in zip(user_list, hobby_list)}
print(users_dict)

with open('users_hobby.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(users_dict))

with open('users_hobby.json', 'r', encoding='utf-8') as f:
    print(json.loads(f.read()))
