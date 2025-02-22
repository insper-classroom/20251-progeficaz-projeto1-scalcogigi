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
    fetch(`/delete_note/${noteId}`, {method: 'POST'})
        .then(() => location.reload());
}
