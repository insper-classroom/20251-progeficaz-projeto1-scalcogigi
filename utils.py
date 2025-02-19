import json
import os

def load_data(filename):
    file_path = os.path.join("static", "data", filename)
    
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def load_template(template_name):
    with open(f'static/templates/{template_name}', 'r') as template_file:
        return template_file.read()

def adicionar_anotacao(titulo, detalhes):
    caminho_arquivo = os.path.join("static", "data", "notes.json") 

    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'w') as arquivo:
            json.dump([], arquivo)

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        notas = json.load(arquivo)

    nova_anotacao = {
        'titulo': titulo,
        'detalhes': detalhes
    }
    notas.append(nova_anotacao)

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(notas, arquivo, ensure_ascii=False, indent=4)
