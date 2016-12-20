def dictionary():
    """
    build a dictionary with ensg ids as keys, and count of mapped traits and mapped traits as values
    :return:
    """
    with open('count_of_m_traits_for_gwas_catalog_mapped_genes_with_m_traits.tsv', 'r') as f:
        next(f)
        d = {}
        for line in f:
            l = line.strip().split('\t', 1)
            # print(l[0])
            # print(l[1])
            d[l[0]] = l[1]
        return d


outfile = open('1kb_flank_mapping_gd_count_final.tsv', 'w')
ensg_count_dict = dictionary()
with open('old_no_m_traits_af_single_file_glengthwithflanks.tsv', 'r') as f:
    header = next(f)
    outfile.write(header.strip() + '\t1k_flank_mapping_counts\tmapped_traits\n')
    for line in f:
        ensg_id = line.strip().split('\t', 1)[0]
        count_info = ensg_count_dict.get(ensg_id)
        if count_info is None:
            outfile.write(line.strip() + '\t0\n')
        else:
            outfile.write(line.strip() + '\t' + count_info + '\n')
print('job done!')