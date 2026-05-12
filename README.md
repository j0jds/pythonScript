# Renomeador Automático de Arquivos

## Propósito
Este script renomeia automaticamente todos os arquivos do diretório atual para um formato numerado sequencial: "número.extensão" (ex.: 1.txt, 2.jpg, 3.pdf). Ele ignora arquivos já numerados, arquivos ocultos e o próprio script.

## Como Funciona

### Etapa 1: Escanear arquivos já numerados
- Lista todos os arquivos no diretório atual.
- Ignora subdiretórios.
- Procura por arquivos no padrão "número.extensão" (ex.: 1.txt, 10.jpg).
- Para cada um, registra o maior número encontrado por extensão.
- Armazena o próximo número disponível para cada extensão em um dicionário (counters[extensão] = maior_número + 1).

### Etapa 2: Renomear arquivos não numerados
- Percorre todos os arquivos novamente.
- Ignora:
  * Arquivos ocultos (que começam com ponto)
  * Diretórios
  * O próprio script (arquivos que terminam com .py)
  * Arquivos que já estão no formato "número.extensão"
- Para cada arquivo restante:
  * Extrai a extensão (texto após o último ponto). Se não houver ponto, usa o nome completo como extensão.
  * Se a extensão ainda não estiver no dicionário, inicializa com 1.
  * Cria o novo nome: f"{counters[extensão]}.{extensão}"
  * Verifica conflito de nome; se o nome já existir, incrementa o contador até achar um livre.
  * Renomeia o arquivo.
  * Incrementa o contador daquela extensão (assim o próximo arquivo com mesma extensão recebe o próximo número).

## Comportamentos Importantes
- Arquivos sem extensão são tratados como se o nome inteiro fosse a "extensão". Exemplo: "readme" vira "1.readme".
- A numeração é independente por extensão. Exemplo: arquivos .txt têm sua própria sequência (1.txt, 2.txt...), arquivos .jpg têm a deles (1.jpg, 2.jpg...).
- Arquivos já numerados não são renomeados, mas seus números são respeitados e a sequência continua a partir do maior número existente.

## Exemplo
Antes de executar:
  documento.pdf
  imagem.jpg
  anotacao.txt
  1.txt

Depois de executar:
  1.pdf
  1.jpg
  1.txt   (inalterado – já estava numerado)
  2.txt   (veio de anotacao.txt)

## Requisitos
- Python 3.x