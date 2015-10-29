# KEGG_mapping
## About
KEGG_mapping is a Python script for converting [BLAST2GO](https://www.blast2go.com/) KEGG mapping output. The "Export KEGG Data" option in BLAST2GO only allows an output in which each row corresponds to an enzyme, with all sequences annotated with the associated enzyme code given as a comma-separated list on a single line. KEGG_mapping converts this format to one in which each row corresponds to a sequence. This format is required for certain downstream software such as [GOSeq](http://www.bioconductor.org/packages/release/bioc/html/goseq.html).  

## Citation
KEGG_mapping is not associated with a paper; to cite it please use:

    Sutton, ER. (2015). KEGG_mapping [Software]. 
    Available at https://github.com/ElizabethSutton/KEGG_mapping.

## Requirements
KEGG_mapping requires Python.

## Usage
KEGG_mapping takes as its input a tab-delimited text file produced by the "Export KEGG Data" option of [BLAST2GO](https://www.blast2go.com/).

### *Example*
The command might be:

    ./KEGG_mapping.py BLAST2GO_KEGG_mapping.txt

## Output
KEGG_mapping outputs two text files, 'KEGG_mapping_1.txt' and 'KEGG_mapping_2.txt'. Both of these have two columns. The first is the sequence name and the second is one or more KEGG pathways associated with that sequence. In 'KEGG_mapping_1.txt', all pathways for a sequence are listed as a semicolon-delimited list on one line. In 'KEGG_mapping_2.txt', each pathway is listed on a separate line.
