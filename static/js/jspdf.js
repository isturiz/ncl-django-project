document.addEventListener("DOMContentLoaded", function () {
    const { jsPDF } = window.jspdf;

    // Función para abrir la tabla como PDF en una nueva pestaña
    function openTableAsPDF() {
        const doc = new jsPDF();
        doc.text("Tabla de Estudiantes", 100, 10, 'center');

        // Obtener la tabla
        const table = document.getElementById("table-file");

        // Obtener todas las filas de la tabla
        const rows = table.querySelectorAll("tbody tr");

        // Iterar a través de las filas y agregar sus datos al PDF
        rows.forEach((row, index) => {
            const columns = row.querySelectorAll("td");
            let rowData = [];
            columns.forEach((column) => {
                rowData.push(column.textContent.trim());
            });
            doc.text(rowData.join(" | "), 10, 20 + index * 10);
        });

        // Generar el blob del PDF
        const pdfBlob = doc.output("blob");

        // Crear una URL object y abrir en una nueva pestaña
        const pdfURL = URL.createObjectURL(pdfBlob);
        window.open(pdfURL, "_blank");

        // Liberar la URL object cuando ya no se necesite
        URL.revokeObjectURL(pdfURL);
    }

    // Agregar un evento click al botón de exportación
    const exportButton = document.getElementById("export-pdf-button");
    exportButton.addEventListener("click", openTableAsPDF);
});
