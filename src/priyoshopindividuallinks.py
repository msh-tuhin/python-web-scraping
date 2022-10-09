file = open("C:\\Users\\Tuhin\\Desktop\\priyoshop\\priyoshopfinallinks2.txt", "r")
file2 = open("C:\\Users\\Tuhin\\Desktop\\priyoshop\\priyoshopshirtlinks.txt", "w")
lines = []
while(True):
    line = file.readline()
    if line is '':
        break
    lines.append(line)
    if 'shirt' in line:
        file2.write(line)

print(len(lines))
print(len(set(lines)))
file.close()
file.close()