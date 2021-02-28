#!/usr/bin/env python3

import fileinput
import requests as r
import re
from io import StringIO
from Bio import SeqIO

motif = re.compile('(?=(N[^P][ST][^P]))')

for id in fileinput.input():
    id = id.rstrip()
    response = r.post(f'https://www.uniprot.org/uniprot/{id}.fasta')
    seq = list(SeqIO.parse(StringIO(response.text), 'fasta'))[0]
    pos = [m.start()+1 for m in motif.finditer(str(seq.seq))]
    if len(pos):
        print(id)
        print(*pos)
