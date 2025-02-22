from utils import load_data, load_template, adicionar_anotacao, delete_note
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
    adicionar_anotacao(titulo, detalhes)

def deletar_notas(id):
    delete_note(id)