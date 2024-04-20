import os
import sys

def server_config():
    # Obtém o diretório pai deste script (onde está localizado o arquivo server_config.py)
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Adiciona o diretório pai ao PYTHONPATH
    sys.path.append(project_dir)

    # Se necessário, adicione outros diretórios ao PYTHONPATH
    # sys.path.append(os.path.join(project_dir, 'subdiretorio'))

    # Configurações adicionais podem ser feitas aqui, como inicialização do aplicativo Flask, etc.

if __name__ == "__main__":
    server_config()