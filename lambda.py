people = [
    {'name':'mansoor','address':'kotha'},
    {'name':'osama','address':'top'},
    {'name':'shahroom','address':'swabi'},
    {'name':'hasan','address':'zaida'}
]

people.sort(key=lambda person:person['name'])
print(people)