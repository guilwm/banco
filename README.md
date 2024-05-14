[TOC]

# Guia de instalação do Python no linux

## Atualização da versão do Python

Aqui será feito um passo a passo para instalar uma versão recente do python no linux. O primeiro passo é adicionar um PPA (Personal Package Archives) ao linux, e para isso, deve-se usar um software chamado software-properties-common que pode ser obtido com o comando abaixo1:

- sudo apt-get install software-properties-common

Após a instalação do common, o repositório do python pode ser adicionado usando o comando:

- sudo add-apt-repository ppa:deadsnakes/ppa

Agora, uma versão recente do python pode ser instalada usando:


- sudo apt-get install python3.11

Alem disso, deve-se instalar o pip

sudo apt-get install python3-pip

e também o git

sudo apt-get install git-all

## Configurando o Git

Após instalar o git, atualizar as credenciais com os comandos:

- git config --global user.name *"FIRST_NAME LAST_NAME"*
- git config --global user.email "MY_NAME@example.com"

Note que estes comandos configura seu git de forma global, para todos os projetos. 

## Priorizando a versão do Python

Agora, a prioridade do python pode ser mudada com os seguintes comandos:

- sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
- sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2

para verificar a prioridade, usar:

- sudo update-alternatives --config python3

após usar o comando acima, escolher qual python será priorizado, usando o número dado. Um asterisco no início mostra qual python está priorizado.

Aqui no caso, foi digitado 1 para escolher a versão 3.11

Neste caso, uma versão do python 3.11 foi colocada em prioridade 1 e ao digitar o comando python3 --version, ela deverá ser mostrada. Para verificar as outras versões, python3.xx --version.  

## Instalando o poetry

O **poetry** é um poderoso gerenciador do python. Sua instalação requer um passo a passo e aqui será mostrado o que deve ser feito. O primeiro passo é instalar o curl caso não tenha sido feito.

- sudo snap install curl

Após a instalação do curl, um problema de distutils pode acontecer. Para resolver isso, basta mudar a prioridade da versão python para uma mais nova ou usar:


- sudo apt-get install python3-distutils

- sudo apt-get install python3-apt

OBS: pode ser que o método acima não funcione (ao instalar o pendulum, pode dar erro). Assim, deverá ser usado o comando especifico sudo apt-get install python3.xx-distutils

Resolvido os problemas, o poetry pode ser instalado usando o comando[3]:

- curl -sSL https://install.python-poetry.org | python3 -

Após a instalação, adicionar export PATH="/home/user/.local/bin:$PATH" ao arquivo bashrc que está oculto na pasta home e reiniciar o computador.

## Arquivo Makefile

Antes de criar um arquivo make, é necessário instalar o make. Isso pode ser feito com o comando abaixo:

- sudo apt install -y make

Após a instalação, o arquivo makefile pode ser criado normalmente.
