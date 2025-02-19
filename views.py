from utils import load_data, load_template, adicionar_anotacao
from flask import request, jsonify

def index():
    note_template = "<li><strong>{title}</strong>: {details}</li>"
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    # print(notes)

    return load_template('index.html').format(notes=notes)

def submit(titulo, detalhes):
    if not titulo or not detalhes:
        return jsonify({'mensagem': 'Título e detalhes são obrigatórios.'}), 400

    # print(f'Título: {titulo}, Detalhes: {detalhes}')
    adicionar_anotacao(titulo, detalhes)

    return jsonify({'mensagem': 'Anotação adicionada com sucesso!'}), 201
