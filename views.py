from utils import *
from flask import request, jsonify

def index():
    note_template = """
    <li data-id='{id}' onclick='editNote(this)'>
        <strong>{title}</strong>: <span class='details'>{details}</span>
        <button onclick='deleteNote({id})'>X</button>
    </li>
    """
    notes_li = [
        note_template.format(id=dados['id'], title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)


def submit(titulo, detalhes):
    if not titulo or not detalhes:
        return jsonify({'mensagem': 'Título e detalhes são obrigatórios.'}), 400
    adicionar_anotacao(titulo, detalhes)
    return jsonify({'mensagem': 'Anotação adicionada com sucesso!'}), 201

def delete_note(note_id):
    remover_anotacao(note_id)

def edit_note(note_id, titulo, detalhes):
    atualizar_anotacao(note_id, titulo, detalhes)