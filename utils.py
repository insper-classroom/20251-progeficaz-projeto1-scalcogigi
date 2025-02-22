import sqlite3
import os

def init_db():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            detalhes TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def load_data():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, detalhes FROM notes")
    notas = [{"id": row[0], "titulo": row[1], "detalhes": row[2]} for row in cursor.fetchall()]
    conn.close()
    return notas


def adicionar_anotacao(titulo, detalhes):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (titulo, detalhes) VALUES (?, ?)", (titulo, detalhes))
    conn.commit()
    conn.close()

def remover_anotacao(note_id):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()

def atualizar_anotacao(note_id, titulo, detalhes):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET titulo = ?, detalhes = ? WHERE id = ?", (titulo, detalhes, note_id))
    conn.commit()
    conn.close()

def load_template(template_name):
    with open(f'static/templates/{template_name}', 'r') as template_file:
        return template_file.read()

init_db()
