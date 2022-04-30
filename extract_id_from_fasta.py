# @Time     :  16:00
# @Author   : petaleaf
# @FileName : extract_id_from_fasta.py
# @Software : Pycharm


from Bio import SeqIO
import sys


if len(sys.argv) != 3:
    print('Usage: python extract_id_from_fasta.py <fasta.fasta> <xx.out >')
    sys.exit()
idlist = []
for seqrecord in SeqIO.parse(sys.argv[1],"fasta"):
    idlist.append(seqrecord.id+"\n")
print(len(idlist))


with open(sys.argv[2],"w",encoding="UTF-8") as outputfile:
    for id in idlist:
        outputfile.write(id)

