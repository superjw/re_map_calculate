# this is used for mapping GWAS-Catlog snps to GRCh37 assembly
# it works (19-Dec-2016)
import sys
import os


def mapping(p, fl, infile_name):
    """
    check the belonging of gene and snp
    :param p: position of snp
    :param fl: up/downstream range
    :param infile_name: file name of gene START END position file
    :return:string of gene_ids and gene_names
    """
    # inf = open('./gene_location/pos.chr' + ch + '.gene.tsv', 'r')
    inf = open(infile_name, 'r')
    g_id_lst = [] # use list here just want to include any other potential mapping position
    g_name_lst = []
    for line in inf:
        l = line.strip().split('\t')
        start = int(l[1]) - int(fl)
        end = int(l[2]) + int(fl)
        if (len(str(p)) - len(str(start)) < 2) and (len(str(end)) - len(str(p)) < 2):
            # check the length of the position, to reduce the loop
            if start < int(p) < end:
                g_id_lst.append(l[0])
                g_name_lst.append(l[4])
        else:
            continue
    inf.close()
    g_id_lst = ','.join(g_id_lst)
    g_name_lst = ','.join(g_name_lst)
    # print(g_id_lst)
    return g_id_lst, g_name_lst


# def main():
#     chro = sys.argv[1]
#     infile, outfile = generate_file_names(chro)
#     outf = open(outfile, 'w')
#     # with open('19', 'r') as f:
#     for line in sys.stdin:
#         if not line.startswith('#'):
#             # info = line.strip().split('\t')[7]
#             maf, snp_pos = retrive_info(line)
#             # if maf:
#             g_id, g_name = mapping(snp_pos, 1000, infile)
#             # print(snp_pos, end = '\t')
#             # print(maf, end='\t')
#             # print(g_id, end='\t')
#             # print(g_name)
#             outf.write(maf + '\t' + g_id + '\t' + g_name + '\n')
#     outf.close()
#
#
# main()
for i in range(1, 23):
    gene_location_infile_name = '../gene_location/pos.chr' + str(i) + '.gene.tsv'
    outfile_name = './batch_file/gwascatalog_chr' + str(i) + '_snp_mapping_1000_flank_grch37.tsv'
    snp_location_file_name = './batch_file/chr' + str(i) + '.tsv'
    outf = open(outfile_name, 'w')
    with open(snp_location_file_name, 'r') as f:
        next(f)
        for line in f:
            line = line.strip().split('\t')
            rs, pos = line[1], line[2]
            g_id, g_name = mapping(pos, 1000, gene_location_infile_name)
            outf.write(rs + '\t' + pos + '\t'+ g_id + '\t' + g_name + '\n')
    outf.close()
    print('mapping done for chr ' + str(i) + '!')
