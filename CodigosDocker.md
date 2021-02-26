## Comandos e Passos para fazer backend com mysql e docker

*  Passo 1: Criar um arquivo Dockerfile
*  Passo 2: Criar img com docker build -t nomeqvcquer -f diretorioDoDockerfile .
*  Passo 3: docker run -d --rm --name nomeConteiner nomeiMG
*  Passo 4: Criar arquivo .sql e usar docker exec que significa que vamos rodar comandos

*docker exec -i nomeConteiner mysql -u root -p root < script.sql* 
