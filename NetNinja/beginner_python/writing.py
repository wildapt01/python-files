with open('NetNinja/files/write.txt', 'w') as write_file:
    write_file.write('I love Python 3.')


with open('NetNinja/files/write.txt', 'a') as write_file:
    write_file.write('\nI even dream in python')


quotes = [
    '\nThis the 1st quote',
    '\nI have a lot of quotes',
    '\nAlea jacta est'
]

with open('NetNinja/files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)
