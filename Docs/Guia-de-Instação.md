# Guia de Instalação

Esse documento descreve a instalação do ambiente docker para rodar o programa

# Instale o Docker
O _FS-S.C.A.M_ usa o Docker para virtualizar o ambiente de execução através de containers. 
Siga a documentação oficial do Docker dependendo do seu sistema operacional:
- [Linux (Ubuntu)](https://docs.docker.com/engine/install/ubuntu/) - O modo mais rápido é pelo [script de instalação oficial](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)
- [Windows 10](https://docs.docker.com/docker-for-windows/install/)

# Instale o docker-compose
Usamos o composer como orquestrador de containers para gerenciar os containers e recursos da rede virtual que os une. Caso esteja no Windows ou Mac, não é necessário instalar o docker-compose pois ele já vem embutido no Docker Desktop. Para o Linux, a [documentação oficial](https://docs.docker.com/compose/install/) descreve os seguintes comandos _bash_:

O arquvio é baixado diretamente do GitHub dependendo do tipo e aqruitetura do sitema operacional para o arquivo /usr/local/bin/docker-compose que deve estar incluso na PATH do sistema
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
Altera as permissões do arquivo para permitir que todos os usuários o excutem.
```bash
sudo chmod +x /usr/local/bin/docker-compose
```
Testa a instação
```bash
docker-compose --version 
```

# Clone o repositório
Use o git e clone o repositório do GitHub, o git vem instalado por padrão em muitas distribuições Linux, se não for o seu caso o instale usado o gerenciador de pacotes da sua distribuição.
```bash
git clone https://github.com/Droid-M/FE-S.C.A.M.git
```

# Entre na pasta e crie os containers
```bash
cd FE-S.C.A.M/
docker-compose up -d
```

# Acesse a aplicação WEB
Abra o navegador de sua preferência e vá para http://127.0.0.1/.