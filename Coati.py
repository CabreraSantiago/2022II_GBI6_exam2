def faster_downloader():
    """
    Sirve para cargar id_coati.txt en id_coatiy descargar en formato genbank la información correspondiente a los identificadores de accesión usando el ENTREZ de Biopythony se guardar en coati y en coati.gb
    """
    
    return faster

sequences = []
names = []
with open('data\coati.txt', 'r+') as coati:
    fh = fh.read()
    line =  fh.split("\n")[0:]
    if line[0] == '>':
        names.append(line)
    else:
        sequences.append(line)

for i in range(len(sequences)):
    print(sequences[i], '\n')