# Defining my keys and values in my dictionary
address = {
    'name': 'Jane Doe',
    'address': '555 N Michigan Ave',
    'city': 'Chicago',
    'state': 'IL',
    'zip': '60611'
}

# # Making a variable to format the address in a proper mailing layout
formatted_add = f'''{address['name']}
{address['address']}
{address['city']}, {address['state']} {address['zip']}'''

# Displaying results of formatted_add
print(formatted_add)

# Removing the key:value pair = name
del address['name'] #Alternatively, you can use address.pop('name')

# Creating a new variable full_name as a tuple containing 2 key:value pairs. Then, adding it into the dictionary
full_name = ({'first_name': 'Jane', 'last_name': 'Doe'})
address.update(full_name)

# Updating the address dictionary to add a new key:value
address.update({'honorific': 'Dr.'})

# Created new variable to show new formatted_add layout
new_formatted_add = f'''{address['honorific']} {address['first_name']} {address['last_name']}
{address['address']}
{address['city']}, {address['state']} {address['zip']}'''

# Display results of new_formatted_add
print(new_formatted_add)
