function deleteNote(id) {
    fetch(`/delete_note/${id}`, {
        method: 'POST',
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
        location.reload(); 
    })
    .catch(error => console.error('Erro ao excluir a nota:', error));
}