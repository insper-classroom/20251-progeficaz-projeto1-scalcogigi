document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const tituloInput = document.getElementById("titulo");
    const detalhesInput = document.getElementById("detalhes");

    form.addEventListener("submit", function (event) {
        if (!tituloInput.value.trim() || !detalhesInput.value.trim()) {
            event.preventDefault();
            alert("Por favor, preencha todos os campos antes de enviar!");
        }
    });
});
