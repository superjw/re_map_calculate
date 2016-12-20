# this script is used for counting the mapped traits for each gene in the 'GWAS_entries_grch37_remapping.tsv'


def generate_ensg_set(the_file_name_to_be_count_from):
    """
    used to construct a set of ensg ids for following count
    :return:
    """
    with open(the_file_name_to_be_count_from, 'r') as f:
        header = next(f)
        ensg_list = []
        for line in f:
            l = line.strip().split('\t')
            if len(l) > 13:
                # print(l)
                ensg = l[13]
                # print(ensg)
                if ',' in ensg:
                    multi_ensg = ensg.split(',')
                    for k in multi_ensg:
                        # print(k.replace('\"', ''))
                        ensg_list.append(k.replace('\"', ''))
                else:
                    ensg_list.append(ensg)
            else:
                pass
        return set(list(filter(None, ensg_list)))


def mapped_trait_counter(ensg_id, the_file_name_to_be_count_from):
    i = 0
    with open(the_file_name_to_be_count_from, 'r') as f:
        next(f)
        m_traits_lst = []
        for line in f:
            l = line.strip().split('\t')
            # print(len(l))
            if len(l) > 13:
                m_genes, m_traits = l[13], l[10]
                # print(m_genes, end='\t')
                # print(m_traits)
                if ensg_id in m_genes:
                    if ',' in m_traits:
                        for k in m_traits.split(','):
                            m_traits_lst.append(k.replace('\"', ''))
                    else:
                        m_traits_lst.append(m_traits.replace('\"', ''))
            else:
                pass
        return len(set(list(filter(None, m_traits_lst)))), ','.join(set(list(filter(None, m_traits_lst))))


count_file = 'GWAS_entries_grch37_remapping.tsv'
outfile = open('count_of_m_traits_for_gwas_catalog_mapped_genes_with_m_traits.tsv', 'w')
outfile.write('ensg_id\tcount_of_m_traits\n')
gwas_catalog_mapped_gene_set = generate_ensg_set(count_file)
print(str(len(gwas_catalog_mapped_gene_set)))
for ensg in gwas_catalog_mapped_gene_set:
    print(ensg)
    count_of_the_gene, m_traits = mapped_trait_counter(ensg, count_file)
    outfile.write(ensg + '\t' + str(count_of_the_gene) + '\t' + m_traits + '\n')
print('job done!')