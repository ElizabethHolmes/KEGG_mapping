#!/usr/bin/env python

# dealing with command line input
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename',type=str)
args = parser.parse_args()

# reading input
gene_names = []
pathway_names = []
initial_loci = []
delimiter1 = '\t'
delimiter2 = ', '

file = open(args.filename)
file.readline()
for line in file:
        split = line.split(delimiter1)
        pathway = split[0]
        genes = split[5].split(delimiter2)
	for gene in genes:
		gene_names.append(gene)
		pathway_names.append(pathway)
file.close()

# writing output

output = open('KEGG_mapping.txt', 'w')
for i in range (0, len(gene_names)):
    output.write(gene_names[i] + '\t' + pathway_names[i] + '\n')
output.close()
