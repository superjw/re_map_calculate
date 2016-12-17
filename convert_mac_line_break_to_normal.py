# with open('r_filter_trunks.txt', 'r') as f:
#     for line in f:
#         print(len(line.split(',')))
outfile = open('GWAS_snp_positions_on_grch37_autosome_remove_patch.tsv', 'w')
with open('2.tsv', 'r') as f:
     for line in f:
         outfile.write(line.strip() + '\n')
         print(line)
print('job done')
# this is for the ^M in less display