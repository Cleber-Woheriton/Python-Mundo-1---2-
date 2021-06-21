#(Desafio 76) Crie um programa que tenha uma tupla única com nome de
# produtos e seus respectivos preços, na sequência. No final mostre
# uma listagem de preços em forma tabular.

print(f'\033[1;30;43m{" Tabela de Preços e Produtos ":=^70}\033[m')

prod = (25762, 'ADAPTADOR BLUETOOH USB RECEPTOR DE AUDIO 2 EM 1 5.0 YET-TR6', 8.50,
        19333, 'ADAPTADOR BLUETOOTH CSR 2.0 DONGLE USB-P-PC', 3.20,
        17683, 'ADAPTADOR BLUETOOTH CSR 4.0 DONGLE USB-P-PC', 4.90,
        20890, 'ADAPTADOR BLUETOOTH CSR 5.0 DONGLE USB-P-PC', 7.80,
        13031, 'ADAPTADOR BLUETOOTH GRIFFIN GF-100A USB-P-PC', 2.50,
        19274, 'ADAPTADOR BLUETOOTH HAVIT HV-888 USB', 6.50,
        28143, 'APTADOR CONECTOR HDMI MACHO / MACHO', 2.70,
        21300, 'ADAPTADOR CONECTOR HDMI MACHO L / FEMEA', 3.50,
        26608, 'ADAPTADOR CONVERSOR 2VGA/RCA/S-VIDEO PRATA', 10.40,
        20695, 'ADAPTADOR CONVERSOR GAMING REDRAGON ERIS GA-200 PRETO', 16.00,
        13539, 'ADAPTADOR CONVERSOR HDMI / RCA FULLHD 1080 BRANCO', 14.00,
        15317, 'ADAPTADOR DISPLAY PORT / HDMI', 11.00,
        14276, 'ADAPTADOR DVI-A VGA ANALOGICO', 3.40,
        45578, 'HD EXTERNO / 3 TB', 300)
val = len(prod)
c = 0
print(f'\033[33m{"Código"} {"Produto":^50} {"Valor":^31}\033[m')
while c < val:
    print(f'\033[35m{prod[c]}\033[m | {prod[c+1]:.<60} | R$: {prod[c+2]:>5.2f}')
    c += 3
