const openModal = (modalId, data) => {
    // Obtén una referencia al modal y al contenido del modal.
    const modal = document.getElementById(modalId);
    const modalContent = modal.querySelector(".modal-content");

    // Construye el contenido del modal dinámicamente a partir del objeto.
    let modalHTML = "";
    for (const key in data) {
        if (Object.hasOwnProperty.call(data, key)) {
            modalHTML += `<p><strong>${key}:</strong> ${data[key]}</p>`;
        }
    }

    // Agrega un botón "X" al contenido del modal.
    modalHTML += `<button class="close" onclick="closeModal('${modalId}')">&times;</button>`;

    // Establece el contenido del modal y ábrelo.
    modalContent.innerHTML = modalHTML;
    modal.style.display = "block";

    // Agrega un manejador de eventos para cerrar el modal al hacer clic fuera de él.
    window.addEventListener("click", (event) => {
        if (event.target === modal) {
            closeModal(modalId);
        }
    });
};

const closeModal = (modalId) => {
    // Obtén una referencia al modal.
    const modal = document.getElementById(modalId);

    // Cierra el modal.
    modal.style.display = "none";
};
