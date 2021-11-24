import json
siteList = []
for i in range(1,20):
    siteList.append(input(f'Enter site {i}: '))
print(siteList)


#print(siteList)


with open('host_list.json', 'w', encoding='utf-8') as f:
    json.dump(siteList, f, ensure_ascii=False, indent=4)