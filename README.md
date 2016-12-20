# re_mapping, re analysis for grh37 snps
* `GWAS_snp_positions_on_grch37_autosome_remove_patch.tsv` as shown in the file name, is a list of positions for snps mapped to autosome main assembly only
* `entries_standard_rs_id.tsv` GWAS-catalog entries with standard rs id reported SNPs.
* `entries_non_rs_id.tsv` GWAS-catalog entries with non-standard rs id reported SNPs.
* `GWAS_entries_grch37_remapping.tsv` is the final file for GWAS-Catalog SNPs mapping to GRCh37
* `add_remapped_gene_to_standard_entries.py**` is the script used for add mapped genes to GWAS-Catalog SNPs ---- generated `GWAS_entries_grch37_remapping.tsv`
