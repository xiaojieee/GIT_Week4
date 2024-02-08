# can be opened for overwrite or append

output = open('sample_files/myfile.txt', 'w')
append = open('sample_files/logfile.txt', 'a')

# append a \n to make it a line
chars_written = output.write("Hello\n")
print(chars_written)

chars_written = output.write("Is it me you're looking for?\n")
print(chars_written)

list_of_lyrics = ['I can see it in your eyes\n', 'I can see it in your smile\n']

# append \n to make it lines
# does not return a count of char or bytes written
output.writelines(list_of_lyrics)


