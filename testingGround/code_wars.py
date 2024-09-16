import string

def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))


print(DNA_strand("ATTGC"))  # "ATTGC" --> "TAACG"
print(DNA_strand("GTAT"))  # "GTAT" --> "CATA"
