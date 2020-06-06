a = open('input.txt')
Q = a.readline()
b = {}
for line in a:
    words = line.strip().split(' - ')
    e = words[0]
    la = words[1].split(', ')
    for key in la:
        if key in b:
            b[key].append(e)
        else:
            b[key] = [e]
a.close()
for key in b:
    b[key].sort()
g = open('output.txt', 'w')
g.write(str(len(b)) + '\n')
for la in sorted(b):
    g.write(la + ' - ' + ', '.join(b[la]) + '\n')

g.close()