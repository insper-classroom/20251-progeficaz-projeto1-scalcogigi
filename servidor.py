from flask import Flask, render_template_string, request, redirect, jsonify
import views
import sqlite3

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/')
def index():
    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo') 
    detalhes = request.form.get('detalhes') 

    views.submit(titulo, detalhes)  

    return redirect('/')  

@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    views.delete_note(note_id)
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return render_template_string("<h1>Página não encontrada</h1><p>Desculpe, mas a página que você está procurando não existe.</p>"), 404

if __name__ == '__main__':
    app.run(debug=True)