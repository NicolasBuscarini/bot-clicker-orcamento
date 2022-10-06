# bot-clicker-orcamento

Bot para automatizar o preenchimento de formulários de orçamento dentro de um sistema do PROTHEUS

*Não há nada que um humano possa fazer que um computador não consiga, e da mesma maneira não há nada que um computador faça que um humano não consiga. A diferença é a velocidade de processamento e de memoria.*
## Como rodar o projeto

- <a href="#instalar-python-">É necessario ter o python instalado na maquina.</a>
- Execute o .bat para instalar as dependencias: `/bot/instalar.bat`.
- Mantenha o PROTHEUS aberto na tela de orçamento.
- Execute o .bat para rodar o projeto: `./executar.bat`.
- O bot irá abrir uma janela do navegador para configurar o orçamento.
- <a href=".README_assets/exemplo.xlsx" download="exemplo.xlsx">Seguir o padrão de preenchimento da planilha (NÃO MUDAR OS HEADERS).<a>

## Tecnologias utilizadas no desenvolvimento


| Tecnologia | Versão |
|:-----------|-------:|
| Python     | 3.10.2 |

## Instalar Python !<img src=".README_assets/c8a054c3.png" alt="drawing" style="width:50px; margin-left: 20px;"/>

Um guia rápido para instalar o Python em diferentes sistemas operacionais.

1. <a href="#windows-">Instalar no Windows</a>.
2. <a href="#linux-">Instalar no Linux</a>.

### Windows !<img src=".README_assets/34140973.png" alt="drawing" style="width:40px; margin-left: 20px;"/>

- Se você ainda não instalou o Python em seu sistema operacional Windows, baixe e instale o instalador mais recente do Python3 na página de downloads do Python [Python Downloads Page](https://www.python.org/downloads/)
  - Certifique-se de marcar a caixa durante a instalação que ***adiciona o Python ao PATH***.
    Depois que o Python estiver instalado, você poderá abrir uma janela de comando, digitar python, pressionar ENTER e ver um prompt do Python aberto. Digite quit() para sair. Você também deve poder executar o comando pip e ver suas opções. Se ambos funcionarem, então você está pronto para ir.

### **Linux** !<img src=".README_assets/0139364d.png" alt="drawing" style="width:40px; margin-left: 20px;"/>

- **Raspberry Pi OS** pode precisar de Python e PIP
  - Instale-os: `sudo apt install -y python3-pip`
- **Debian (Ubuntu)** podem precisar de Python e PIP
  - Atualize a lista de repositórios APT disponíveis com `sudo apt update`
  - Instale Python and PIP: `sudo apt install -y python3-pip`
- **RHEL (CentOS)** distributions usually need PIP
  - Instale o EPEL package: `sudo yum install -y epel-release`
  - Instale PIP: `sudo yum install -y python3-pip`
