from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

result_handle = NCBIWWW.qblast(
    "blastn",
    "nt",
    open("subseq_py.fasta").read(),
    entrez_query="Pan troglodytes[Organism]",
    expect=1e-3,
    hitlist_size=10
)
identities = []
blast_records = NCBIXML.parse(result_handle)
for blast_record in blast_records:
    if len(blast_record.alignments) >= 1:
        alignment = blast_record.alignments[0]
        if len(alignment.hsps) >= 1:
            hsp = alignment.hsps[0]
            identity = 100.0 * hsp.identities / hsp.align_length
            identities.append(identity)
mean_identity = sum(identities) / len(identities)
print("Mean identity:", mean_identity)