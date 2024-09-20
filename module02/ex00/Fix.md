## Módulo 02 / Exercício 00 - Deserialization with RCE - Fix

A vulnerabilidade detectada ocorre por conta da utilização da biblioteca pickle do Python que possui uma vulnerabilidade conhecida. O pickle só é recomendado usar para tratar dados confiáveis. Caso contrário, será passível de ataques.

Para corrigir esse problema é recomendado utilizar outros formatos para serialização de dados como json ou yaml.

 