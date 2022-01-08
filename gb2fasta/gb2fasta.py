import os
import sys
import click
from Bio import SeqIO

file = r'C:/Users/James/Documents/gb2fasta/gb2fasta/pRS315.gb'

def parseGb(file):

    # extracts original genbank file name
    outFile = os.path.basename(os.path.splitext(file)[0])
    print(outFile)
    # check file doesn't already exist
    count = 1
    while os.path.isfile(outFile + '.fasta'):
        if count == 1:
            outFile = outFile + ' ({count})'.format(count=count)
        else:
            outFile = ' '.join(outFile.split()[0:-1]) + ' ({count})'.format(count=count)
        count += 1

    SeqIO.convert(file, 'genbank', outFile + '.fasta', 'fasta')

parseGb(file)
