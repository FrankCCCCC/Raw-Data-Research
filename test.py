import json
with open("json.json") as f:
    j1 = json.load(f)

print(type(j1))
print(j1)
print(j1[0]['name'])

# with open("user_vp_from_highest.json",encoding='utf-8',errors='ignore') as fp:
#     j2 = json.load(fp)


# print(j2)
# print(type(j2))