animals = ['dog', 'cat', 'elephant']

for animal in animals:
    print(animal, len(animal))

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)
# 使用推导式
active_users_1 = {user: status for user, status in users.items() if status == 'active'}
print(active_users_1)
