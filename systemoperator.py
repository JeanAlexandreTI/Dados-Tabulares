# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

import pandas as pd

windows = 0
unix = 0
linux = 0
netware = 0
macOs = 0
outro = 0

while True:
    option = int(input("""Qual o melhor Sistema Operacional para uso em servidores?
                    
    [1] -> Windows Server
    [2] -> Unix
    [3] -> Linux
    [4] -> Netware
    [5] -> Mac OS
    [6] -> Outro
    Opção: """))

    if option == 1:
        windows += 1

    elif option == 2:
        unix += 1

    elif option == 3:
        linux += 1
    
    elif option == 4:
        netware += 1
    
    elif option == 5:
        macOs += 1
    
    elif option == 6:
        outro += 1 

    else:
        break


total_votos = windows + unix + linux + netware + macOs + outro

df = pd.DataFrame({
    "Sistemas Operacionais" : ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"],
    "Votos" : [windows, unix, linux, netware, macOs, outro],
    "%" : [(windows / total_votos) * 100, (unix / total_votos) * 100, (linux / total_votos) * 100,
    (netware / total_votos) * 100, (macOs / total_votos) * 100, (outro / total_votos) * 100],
})

print(f"\n{df}")
print(f"Total de votos: {total_votos}")