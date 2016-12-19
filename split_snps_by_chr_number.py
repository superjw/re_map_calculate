# this script is used for grouping snps by chr number
# for i in range(1, 23):
#     print(i)
#     outfile = open('chr' + str(i) + 'tsv', 'w')
import sys
# def build_dict_for_chr(chr_number):
#     """
#     used for building a dictionary of gene location on chromosome "chr_number"
#     :param chr_number: chormosome number
#     :return:
#     """
#     gene_location_file_name = 'pos.chr' + chr_number + '.gene.tsv'
#     with open("'../gene_location/' + gene_location_file_name", 'r') as f:


# sys.argv[1] used to determin chromosome number
out_file_name = './batchfile/chr' + str(sys.argv[1]) + '.tsv'
outfile = open(out_file_name, 'w')
with open('GWAS_snp_positions_on_grch37_autosome_remove_patch.tsv', 'r') as f:
    header = next(f)
    outfile.write(header)
    for line in f:
        line_split = line.strip().split('\t')
        chr = line_split[0]
        rs = line_split[1]
        pos = line_split[2]
        if int(chr) == int(sys.argv[1]):
            print(line)
            outfile.write(line)


print('split snps by chromosome number done for chromosome ' + str(sys.argv[1]) + '!')

