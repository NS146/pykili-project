f=open('input.txt')
res=open('output.txt', 'w')
d={}


N=f.readline()


for stroka in f:
    words=stroka.strip().split(' - ')
    en=words[0]
    lat=words[1].split(', ')
    for key in lat:
        if key in d:
            d[key].append(en)
        else:
            d[key]=[en]
f.close()


for key in d:
    d[key].sort()


res.write(str(len(d)) + '\n')
for lat in sorted(d):
    res.write(lat + ' - ' + ', '.join(d[lat]) + '\n')

res.close()