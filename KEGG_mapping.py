#!/usr/bin/env python

# dealing with command line input
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename',type=str)
args = parser.parse_args()

# reading input
dict = {}
genes_plus_pathway = []
delimiter1 = '\t'
delimiter2 = ', '
delimiter3= '; '

file = open(args.filename)
file.readline()
for line in file:
	pathway_list = []
        split = line.split(delimiter1)
        pathway = split[0]
        genes = split[5].split(delimiter2)
	for gene in genes:
		gene_plus_pathway = gene+'\t'+pathway
		if gene_plus_pathway not in genes_plus_pathway:
			genes_plus_pathway.append(gene_plus_pathway)
			if dict.has_key(gene):
				dict[gene] = dict[gene] + '; ' + pathway
			else:
				dict[gene] = pathway
file.close()

# writing output

output = open('KEGG_mapping_1.txt', 'w')
for gene in dict:
    	output.write(gene + '\t' + dict[gene] + '\n')
output.close()

output = open('KEGG_mapping_2.txt', 'w')
for gene in dict:
	pathway_list = dict[gene].split(delimiter3)
	for pathway in pathway_list:
    		output.write(gene + '\t' + pathway + '\n')
output.close()
