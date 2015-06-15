# KEGG_mapping
## About
KEGG_mapping is a Python script for conversion of [BLAST2GO](https://www.blast2go.com/) KEGG mapping output. The "Export KEGG Data" option in BLAST2GO only allows an output in which each row corresponds to an enzyme, with all sequences annotated with the associated enzyme code given as a comma-separated list on a single line. KEGG_mapping converts this format to one in which each row corresponds to a sequence, with different KEGG pathways for a single sequence listed on multiple lines. This format is required for certain downstream software such as [GOSeq](http://www.bioconductor.org/packages/release/bioc/html/goseq.html).  

** PLEASE NOTE: KEGG_mapping is one of my first scripts written as a beginner programmer and so I apologise if the code is inelegant, unconventional or otherwise sub-optimal; it works for the intended purpose and I provide it in case it might be useful to others, but with no guarantees. **

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
KEGG_mapping outputs a text file, 'output.txt', with two columns. The first is the sequence name and the second is a KEGG pathway associated with that sequence.

There are likely to be duplicate entries in this text file, as some sequences may be associated with more than one enzyme in the same pathway. Before further use the file should be edited to remove these duplicate entries, e.g. using UNIX sort and uniq commands.
