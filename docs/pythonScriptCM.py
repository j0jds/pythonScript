import os
import re

def main():
    # Dicionário para armazenar o próximo número disponível para cada extensão
    counters = {}

    # ------------------------------------------------------------------
    # PRIMEIRA ETAPA: Identificar arquivos já numerados (ex: 1.txt, 2.jpg)
    # e atualizar os contadores para continuar a sequência.
    # ------------------------------------------------------------------
    for filename in os.listdir('.'):
        if not os.path.isfile(filename):
            continue  # Ignora diretórios

        # Verifica se o nome segue o padrão "número.extensão"
        match = re.match(r'^(\d+)\.([^.]+)$', filename)
        if match:
            number = int(match.group(1))   # Número atual do arquivo
            ext = match.group(2)           # Extensão (ex: 'txt', 'pdf')

            # Se a extensão não existe no dicionário ou o número encontrado
            # é maior ou igual ao valor armazenado, atualiza o contador
            # para o próximo número disponível (número + 1)
            if ext not in counters or number >= counters[ext]:
                counters[ext] = number + 1

    # ------------------------------------------------------------------
    # SEGUNDA ETAPA: Renomear todos os outros arquivos que ainda não
    # seguem o padrão "número.extensão" (excluindo scripts Python,
    # arquivos ocultos e os já numerados).
    # ------------------------------------------------------------------
    for filename in os.listdir('.'):
        # Ignora arquivos ocultos
        if filename.startswith('.'):
            continue

        if not os.path.isfile(filename):
            continue

        # Ignora o próprio script Python para não renomeá-lo
        if filename.endswith('.py'):
            continue

        # Ignora arquivos que já estão no formato "número.extensão"
        if re.match(r'^\d+\.[^.]+$', filename):
            continue

        # Obtém a extensão do arquivo (parte após o último ponto)
        # Se não houver extensão, usa o próprio nome do arquivo
        parts = filename.split('.')
        if len(parts) > 1:
            extension = parts[-1]
        else:
            extension = filename

        # Se a extensão ainda não foi vista, inicia o contador em 1
        if extension not in counters:
            counters[extension] = 1

        # Gera o novo nome no formato "contador.extensão"
        new_name = f"{counters[extension]}.{extension}"

        # Garante que o nome não colida com arquivos existentes
        while os.path.exists(new_name):
            counters[extension] += 1
            new_name = f"{counters[extension]}.{extension}"

        # Executa a renomeação
        os.rename(filename, new_name)

        # Incrementa o contador para a próxima renomeação da mesma extensão
        counters[extension] += 1

    print("Done.")

if __name__ == "__main__":
    main()