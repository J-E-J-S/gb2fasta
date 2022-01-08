import os
import sys
import click
from Bio import SeqIO

@click.command()
@click.argument('file')
def cli(file):

    # extracts original genbank file name
    outFile = os.path.basename(os.path.splitext(file)[0])

    # check file doesn't already exist
    count = 1
    while os.path.isfile(outFile + '.fasta'):
        if count == 1:
            outFile = outFile + ' ({count})'.format(count=count)
        else:
            outFile = ' '.join(outFile.split()[0:-1]) + ' ({count})'.format(count=count)
        count += 1

    # convert .gb to .fasta
    SeqIO.convert(file, 'genbank', outFile + '.fasta', 'fasta')
    return

if __name__ == '__main__':
    cli()
