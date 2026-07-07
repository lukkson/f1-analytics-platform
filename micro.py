mytekst = "hello"
result = {}
for i in mytekst:
    result[i] = result.get(i, 0) + 1
print(result)

numes = [1, 2, 3, 2, 4, 5, 4]
dublication = []
numes2 = set()
for i in numes:
    if i in numes2:
        dublication.append(i)
    else:
        numes2.add(i)
print(dublication)

data = {
    "users": [
        {"id": 1, "name": "John", "active": True, "roles": ["admin", "user"]},
        {"id": 2, "name": "Kate", "active": False, "roles": ["user"]},
        {"id": 3, "name": "Tom", "active": True, "roles": ["user"]},
    ]
}

for user in data["users"]:
    if user["active"] == True and "admin" in user["roles"]:
        print(user["name"])

name = [
    user["name"]
    for user in data["users"]
    if user["active"] == True and "admin" in user["roles"]
]
print("AAAA")
print(name)

name = next(
    (
        user["name"]
        for user in data["users"]
        if user["active"] == True and "admin" in user["roles"]
    ),
    None,
)
print(name)
