fo = open('sample_files/out.dat', 'wb')
nb = fo.write(b'Single bytes string\n')
s = "Native string as a line\r\n"
nb = fo.write(s.encode())
print(nb)
# best practice - close the file soother processes can read it
fo.close()


for line in open('sample_files/out.dat', 'rb'):
    print(line.decode(), end="")
