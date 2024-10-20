'''
# Name: Dylan Phan
# Date: 9/19/2024
# File Purpose: contacts program main
'''

from contacts import *

contacts_list = {}
in_index_phone = None
in_index_first = None
in_index_last = None
search = None

while True:
    inp1 = input('''
      *** TUFFY TITAN CONTACT MAIN MENU

1. Add contact
2. Modify contact
3. Delete contact
4. Print contact list
5. Find contact
6. Exit the program

Enter menu choice: ''')
    if (inp1 == '1') :
        in_index_phone = input('Enter phone number: ')
        in_index_first = input('Enter first name: ')
        in_index_last = input('Enter last name: ')
        add_contact(contacts=contacts_list, id=in_index_phone, first_name=in_index_first, last_name=in_index_last)
    if (inp1 == '2') :
        in_index_phone = input('Enter phone number: ')
        in_index_first = input('Enter first name: ')
        in_index_last = input('Enter last name: ')
        modify_contact(contacts=contacts_list, id=in_index_phone, first_name=in_index_first, last_name=in_index_last)
    if (inp1 == '3'):
        in_index_phone = input('Enter phone number: ')
        delete_contact(contacts=contacts_list, id=in_index_phone)
    if (inp1 == '4') :
        sort_contacts(contacts=contacts_list)
    if (inp1 == '5') :
        search = input('Enter search string: ')
        find_contact(contacts=contacts_list, find=search)
    if (inp1 == '6') :
        break