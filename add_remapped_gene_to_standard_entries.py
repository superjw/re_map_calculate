# this script is used for adding remapped GWAS-Catalog SNPs to those standard rs id entries


def build_dict():
    """
    used for building a dictionary of rs_id:mapped_gene
    :return:
    """
    d = {}
    for i in range(1, 23):
        file_name = './batch_file/gwascatalog_chr' + str(i) + '_snp_mapping_1000_flank_grch37.tsv'
        with open(file_name, 'r') as f:
            for line in f:
                line_split = line.strip().split('\t')
                if len(line_split) > 2:
                    d[line_split[0]] = line_split[2]
    return d


def xstr(s):
    return '' if s is None else str(s)


def get_mapped_gene_based_on_rs(one_or_multi_rs_id, rs_gene_dictionary):
    """

    :param rs_gene_dictionary:
    :return: mapped gene for single rs id OR 'string of mapped gene' separated by ',' for multiple rs ids
    """
    multiple_rs = one_or_multi_rs_id.strip().replace('x', '\t').replace(';', '\t').split('\t')
    if len(multiple_rs) == 1:
        mapped_gene_string = rs_gene_dictionary.get(multiple_rs[0])
    elif len(multiple_rs) > 1:
        mapped_gene_list = []
        for k in multiple_rs:
            if rs_gene_dictionary.get(k):
                mapped_gene_list.append(rs_gene_dictionary.get(k))
            else:
                print('no value found!')
                pass
            # print(mapped_gene_list)
            # if not mapped_gene_list:
            mapped_gene_string = ','.join(mapped_gene_list)
            #     print(mapped_gene_string)
    else:
        print('error detected!')
    return mapped_gene_string


outfile = open('GWAS_entries_grch37_remapping.tsv', 'w')
with open('./entries_standard_rs_id.tsv', 'r', encoding='utf8') as f:
    header = next(f)
    outfile.write(header.strip() + '\t' + 'remapped_gene' + '\n')
    dictionary = build_dict()
    for line in f:
        rs = line.strip().split('\t')[7]
        mapped_gene = get_mapped_gene_based_on_rs(rs, dictionary)
        mapped_gene = xstr(mapped_gene)
        outfile.write(line.strip() + '\t' + mapped_gene + '\n')
outfile.close()
print('remapping done!')
