
inputfile ="DNA.txt" # to open the required txt file
f = open(inputfile, "r")
seq = f.read()

#print("done") ## test if file opens

SLC={'I':['ATT', 'ATC', 'ATA'],
'L':['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'],
'V':['GTT', 'GTC', 'GTA', 'GTG'],
'F':['TTT', 'TTC'],
'M':['ATG'],
'C':['TGT', 'TGC'],
'A':['GCT', 'GCC', 'GCA', 'GCG'],
'G':['GGT', 'GGC', 'GGA', 'GGG'],
'P':['CCT', 'CCC', 'CCA', 'CCG'],
'T':['ACT', 'ACC', 'ACA', 'ACG'],
'S':['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
'Y':['TAT','TAC'],
'W':['TGG'],
'Q':['CAA','CAG'],
'N':['AAT','AAC'],
'H':['CAT','CAC'],
'E':['GAA', 'GAG'],
'D':['GAT', 'GAC'],
'K':['AAA', 'AAG'],
'R':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
'Stop':['TAA','TAG','TGA']
}

def translate(DNA):
    num=3
    range=0
    seq=''
    while (num<len(DNA)+1):
        x=DNA[range:num]
        for key in SLC.keys():
            if x in SLC[key]:
                seq+=key
        num+=3
        range+=3
    print(seq)

def mutate():
    f=open('DNA.txt','r')
    x=f.read()
    x=str(x)
    aind=x.replace('a','A')
    c=open('normalDNA.txt','w')
    c.write(aind)
    bind=x.replace('a','T')
    d=open('mutatedDNA.txt','w')
    d.write(bind)
    print('**********   NormalDNA  ****************')
    txtTranslate(aind)
    print('**********   MutatedDNA  ****************')
    txtTranslate(bind)

def txtTranslate(txt):
    return translate(txt)

mutate()

