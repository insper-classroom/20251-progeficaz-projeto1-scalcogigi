function editNote(element) {
    let noteId = element.getAttribute('data-id');
    let title = element.querySelector('strong');
    let details = element.querySelector('.details');
    
    let newTitle = prompt('Editar título:', title.textContent);
    let newDetails = prompt('Editar detalhes:', details.textContent);
    
    if (newTitle && newDetails) {
        fetch(`/edit_note/${noteId}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: `titulo=${newTitle}&detalhes=${newDetails}`
        }).then(() => location.reload());
    }
}

function deleteNote(noteId) {
    console.log("Tentando excluir a nota com ID:", noteId); // Verifica se a função é chamada
    fetch(`/delete_note/${noteId}`, {
        method: 'POST',
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro na requisição: ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        alert(data.mensagem); // Exibe a mensagem de sucesso
        document.querySelector(`li[data-id='${noteId}']`).remove(); // Remove o item da lista
    })
    .catch(error => console.error('Erro ao excluir a nota:', error));
}
