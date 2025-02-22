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
    cursor.execute("select id, titulo, detalhes from notes")
    notas = [{"id": row[0], "titulo": row[1], "detalhes": row[2]} for row in cursor.fetchall()]
    conn.close()
    return notas

def adicionar_anotacao(titulo, detalhes):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("insert into notes (titulo, detalhes) values (?, ?)", (titulo, detalhes))
    conn.commit()
    conn.close()

def delete_note(id):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("delete from notes where id = ?", (id,))
    conn.commit()
    conn.close()

def load_template(template_name):
    with open(f'static/templates/{template_name}', 'r') as template_file:
        return template_file.read()

init_db()