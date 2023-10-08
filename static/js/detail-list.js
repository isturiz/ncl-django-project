const openModal = (modalId, data) => {
    // Obtén una referencia al modal y al contenido del modal.
    const modal = document.getElementById(modalId);
    const modalContent = modal.querySelector(".modal-content");

    // Divide el string del nombre y apellido en partes usando espacios como separadores.
    const nameParts = data['Nombre'].split(' ');

    // Filtra las partes válidas (no son 'None' ni 'undefined') del nombre y apellido.
    let filteredNameParts = nameParts.filter(part => part !== 'None' && part !== 'undefined');

    // Construye el contenido del modal para el nombre y apellido.
    let modalHTML = '';
    

    for (const key in data) {
        if (Object.hasOwnProperty.call(data, key)) {
            if (filteredNameParts.length > 0) {
                modalHTML += `<p><strong>Nombre:</strong> ${filteredNameParts.join(' ')}</p>`;
                filteredNameParts = 0
            }else {

                modalHTML += `<p><strong>${key}:</strong> ${data[key]}</p>`;
            }
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
