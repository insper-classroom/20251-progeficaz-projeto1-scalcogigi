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
    cursor.execute("SELECT titulo, detalhes FROM notes")
    notas = [{"titulo": row[0], "detalhes": row[1]} for row in cursor.fetchall()]
    conn.close()
    return notas

def adicionar_anotacao(titulo, detalhes):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (titulo, detalhes) VALUES (?, ?)", (titulo, detalhes))
    conn.commit()
    conn.close()

def load_template(template_name):
    with open(f'static/templates/{template_name}', 'r') as template_file:
        return template_file.read()

init_db()
