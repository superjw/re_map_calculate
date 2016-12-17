outfile = open('r_filter.txt', 'w')
lst = []
with open("author_reported_rs.txt", 'r') as f:
    for line in f:
        line = line.strip().replace('x', '\t').replace(';', '\t').split('\t')
        for k in line:
            lst.append(k.strip().replace(' ', ''))

#         lst.append(line.strip().replace(' ', ''))
# rs_set = set(line.strip() for line in open("author_reported_rs.txt", 'r'))
rs_set = set(lst)
for rs in rs_set:
    outfile.write('\"' + rs + '\"' + ',')
    # remember to remove the last ','
print('job done!')
