# Returning a Dict

contact_list = []

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    contact_list.append(person)

build_person('jimi', 'hendrix')
build_person('tommy', 'jones')
build_person('denis', 'xie')

for i in contact_list:
    print(i)


# add optional argument for age
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        return person
    else:
        return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
musician2 = build_person('jimi', 'hendrix')
print(musician2)
