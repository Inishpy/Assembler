comp = {"0": '0101010', "1": '0111111', "-1": "0111010", "D": "0001100", "A": "0110000", "!D": "0001101", "!A": '0110001', "-D": '0001111', "-A": '0110011', "D+1":'0011111', "A+1": '0110111', "D-1": '0001110', "A-1": '0110010', "D+A": '0000010', "D-A": '0010011', "A-D": '0000111', "D&A": '0000000', "D|A":'0010101',"M":'1110000', "!M": '1110001', "-M": '1110011', "M+1": '1110111', "M-1": '1110010', "D+M": '1000010', "D-M": '1010011', "M-D": '1000111', "D&M": '1000000', "D|M":'1010101'}
dest = {"M": '001', "D": '010', 'MD': '011', "A": '100', "AM": '101', "AD": '110', "AMD": '111'}
jump = {"JGT": '001', "JEQ": '010', "JGE": '011', "JLT": '100', "JNE": '101', 'JLE': '110', 'JMP': '111'}

pre_symbols = {"SP": '0', "LCL": '1', "ARG": '2', "THIS": '3', "THAT": '4', "R0": '0',"R1": '1',"R2": '2',"R3": '3',"R4": '4',"R5": '5',"R6": '6',"R7": '7',"R8": '8',"R9": '9',"R10": '10',"R11": '11',"R12": '12',"R13": '13',"R14": '14',"R15": '15', "SCREEN": '16384', "KBD": '24576' }


filename = input('type file name with asm extention ')
file = open(filename + str('.asm'))

file = file.readlines()

for i in range(len(file)):
    file[i] = (''.join(file[i].split()))


for i in range(len(file)):
    file[i] = (file[i].split('//')[0])

file4 = []
for i in file:
    if i != '':
        file4.append(i)

line = 0
varm = 16
for i in file4:
    if '(' not in i:
        line += 1

    if '(' in i:
        Label = i.split('(')[1]
        Label = Label.split(')')[0]
        if Label not in pre_symbols:
            pre_symbols[str(Label)] = str(line)

for i in file4:
    if '@' in i and (i.split('@')[1]).islower() and not (i.split('@')[1]).isnumeric():
        if i.split('@')[1] not in pre_symbols:
            pre_symbols[str(i.split('@')[1])] = str(varm)
            varm += 1

for i in range(len(file4)):
    
    if "@" in file4[i]:
        x = file4[i].split('@')[1]
        if x.isnumeric():
            n = bin(int(file4[i].split('@')[1])).replace("0b", '')
            file4[i] = str(0) * (16 - len(n)) + n + '\n'
        elif x.islower():
            if x in pre_symbols:
                n = bin(int(pre_symbols[str(x)])).replace('0b', '')
                file4[i] = str(0) * (16 - len(n)) + n + '\n'
        elif x.isupper():
            if x in pre_symbols:
                n = bin(int(pre_symbols[str(x)])).replace('0b', '')
                file4[i] = str(0) * (16 - len(n)) + n + '\n'
        else:
            if x in pre_symbols:
                n = bin(int(pre_symbols[str(x)])).replace('0b', '')
                file4[i] = str(0) * (16 - len(n)) + n + '\n'

    else:
        if "=" in file4[i] and ";" in file4[i]:
            x = file4[i].split('=')[0]
            x_ =  file4[i].split('=')[1]
            y = x_.split(';')[0]
            z = x_.split(';')[1]

            xbin = dest[str(x)]
            ybin = comp[str(y)]
            zbin = jump[str(z)]

            file4[i] = "111" + ybin + xbin + zbin + '\n'

        elif '=' in file4[i] and ';' not in file4[i]:
            x = file4[i].split('=')[0]
            y =  file4[i].split('=')[1]

            xbin = dest[str(x)]
            ybin = comp[str(y)]
            zbin = '000'

            file4[i] = "111" + ybin + xbin + zbin + '\n'

        elif '='  not in file4[i] and ';' in file4[i]:
            y = file4[i].split(';')[0]
            z =  file4[i].split(';')[1]

            xbin = '000'
            ybin = comp[str(y)]
            zbin = jump[str(z)]

            file4[i] = "111" + ybin + xbin + zbin + '\n'  




hack = open(filename + str('.hack'), 'w')

for i in file4:
    if '(' not in i:
        hack.write(i)

hack.close()
file.close()
print(pre_symbols)
