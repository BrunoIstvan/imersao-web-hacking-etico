## Módulo 01 / Exercício 02 - SSRF e LFI - Payloads


Ao verificar que a página está esperando uma URL, o atacante pode executar diversos testes para verificar se aplicação se enquadra numa vulnerabilidade do tipo SSRF/LFI.

Um exemplo de exploração por parte do atacante é tentar acessar recursos internos do servidor que não deveriam ser acessíveis.

No exemplo abaixo, o atacante acessa diretamente o arquivo de sistema:
	
    file:///etc/passwd
    
Já nesse exemplo, o atacante passa pelo próprio site que faz uma requisição para a mesma aplicação e lê o arquivo de sistema.

    http://localhost:5000/fetch?url=file:///etc/passwd

