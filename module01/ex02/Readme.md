## Módulo 01 / Exercício 02 - SSRF e LFI - Explicação

## O que é?
A vulnerabilidade em questão é conhecida como SSRF (Server Side Request Forgery) e LFI (Local File Inclusion) do lado do servidor. 

SSRF é uma vulnerabilidade de segurança em que um invasor pode forjar solicitações de um servidor da web para acessar recursos internos que normalmente não seriam acessíveis a partir de uma conexão externa. Isso pode incluir informações de configuração, dados do usuário ou até mesmo recursos do sistema operacional. O atacante pode usar a vulnerabilidade para manipular solicitações HTTP ou outros protocolos para se comunicar com sistemas internos, como bancos de dados ou sistemas de arquivos. Com o SSRF também é possível fazer com que o seu servidor faça requisições para servidores de terceiros, existindo a possibilidade de utilizá-lo como uma forma de ataque a um outro alvo. 

Já o LFI é uma vulnerabilidade que ocorre quando uma aplicação web usa o caminho de um arquivo como entrada de dados, sem validar ou filtrar adequadamente essa entrada. Isso permite que um atacante manipule essa entrada para incluir arquivos locais do servidor web, que normalmente não deveriam ser acessíveis pela aplicação.


A exploração bem-sucedida de SSRF/LFI pode permitir que um atacante: 
* Acesse recursos e informações confidenciais, incluindo dados do usuário, credenciais, arquivos de configuração e até realizar ataque a servidores de terceiros.
* Cause danos de imagem à companhia.
