'''
Name: Dylan Phan
Date: 9/19/2024
File Purpose: putting contacts in a list and making it a program
'''
contacts = {}

def add_contact(contacts, id=None, first_name=None, last_name=None) :
    #This function adds a contact to the dictionary of contacts
    if id in contacts:
        print('Phone number already exists.')
        return "error"
    contacts.update({id:[first_name,last_name]})
    print(f'Added: {first_name} {last_name}')
    return {id: [first_name,last_name]}

def modify_contact(contacts, id=None, first_name=None, last_name=None,) :
    #this function modifies the contacts dictionary and changes it to the user's request
    if id in contacts :
        contacts[id] = [first_name, last_name]
        print('Modified: ' + first_name +' ' + last_name)
        return {id : [first_name,last_name]}
    print('Phone number does not exist.')
    return 'error'

def delete_contact(contacts, id=None) :
    #this function deletes a contact from the contact dictionary
    if id in contacts :
        first_name, last_name = contacts[id]
        print('Deleted: ' + str(first_name) + ' ' + str(last_name) +'.')            
        del contacts[id]
        return {id: [first_name, last_name]}
    print('Invalid phone number.')
    return 'error'


def sort_contacts(contacts) :
    #this function prints out every contact in the list contacts
    print('''
==================== CONTACT LIST ====================
Last Name             First Name            Phone
====================  ====================  ==========''')
    sorted_contacts = dict(sorted(contacts.items(), key=lambda item: (item[1][1], item[1][0])))
    for phone, (first_name, last_name) in sorted_contacts.items():
        print(f'{last_name:21} {first_name:20}  {phone}')
    return sorted_contacts

def find_contact(contacts, find = None) :
    #this function searches for a query that the user inputs and makes a list to similar results
    found_contacts = {}
    #for phone, (first_name, last_name) in contacts.items():
    if find.isdigit() and int(find) in contacts:
        found_contacts[int(find)] = contacts[int(find)]

    for phone, (first_name, last_name) in contacts.items():
        if find.lower() in first_name.lower() or find.lower() in last_name.lower():
            found_contacts[phone] = [first_name, last_name]
    sorted_contacts = dict(sorted(found_contacts.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))
    print('''
================== FOUND CONTACT(S) ==================
Last Name             First Name            Phone
====================  ====================  ==========''')
    for phone, (first_name, last_name) in sorted_contacts.items():
        print(f'{last_name:21} {first_name:20}  {phone}')
    return sorted_contacts