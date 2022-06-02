from os import lseek


anthony = {
    'name': 'anthony',
    'number': '555-111-1111'
}
viviana = {
    'name': 'viviana',
    'number': '555-222-2222'
}
mommy = {
    'name': 'mommy',
    'number': '555-333-3333'
}
daddy = {
    'name': 'daddy',
    'number': '555-444-4444'
}
tawon = {
    'name': 'tawon',
    'number': '555-555-5555'
}
rebecca = {
    'name': 'rebecca',
    'number': '555-777-7777'
}

class ContactList():

    def __init__(self, list_name, contacts):
        self.list_name = list_name
        self.contacts = contacts
        

    def add_contact(self, name):
        (self.contacts).append(name)

    def remove(self, name):
        if name in self.contacts:
            (self.contacts).remove(name)
    
    def match(self, other):
        matches = []
        for contact in self.contacts:
                if contact in other.contacts:
                    matches.append(contact)
        return(f"Matches from {self.list_name} and {other.list_name} are {matches}")
    


friends = ContactList('Friends',[])
family = ContactList('Family',[])
work = ContactList('Work',[])
friends.add_contact(anthony)
friends.add_contact(viviana)
family.add_contact(anthony)
family.add_contact(mommy)
family.add_contact(daddy)
work.add_contact(rebecca)
work.add_contact(tawon)
keys = friends.__dict__.keys()
values = friends.__dict__.values()
# print(keys)

print(f"Friends list {friends.contacts}")
# print(f"Family list {family.contacts}")
# print(f"Work list {work.contacts}")
friends.remove(viviana)
friends.remove(mommy)
print(f"Friends list {friends.contacts}")
print(friends.match(family))
print(friends.match(work))

