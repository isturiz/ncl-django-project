
document.addEventListener("DOMContentLoaded", function() {
    const tableSearch = document.getElementById("table-search");
    const tableRows = document.querySelectorAll("#table-file tbody tr");
    const resultMessage = document.getElementById("search-result-message");

    tableSearch.addEventListener("input", function() {
        const searchText = tableSearch.value.trim().toLowerCase();
        let matchCount = 0;

        tableRows.forEach(function(row) {
            const rowData = row.textContent.toLowerCase();
            if (rowData.includes(searchText)) {
                row.style.display = "";
                matchCount++;
            } else {
                row.style.display = "none";
            }
        });

        // Mostrar mensaje de resultado solo si hay texto en el campo de búsqueda
        if (searchText === "") {
            resultMessage.textContent = "";
        } else if (matchCount > 0) {
            resultMessage.textContent = `Se encontraron ${matchCount} coincidencias.`;
        } else {
            resultMessage.textContent = "No se encontraron coincidencias.";
        }
    });
});


// function doSearch() {
//     const tableReg = document.getElementById("table-file");
//     const searchText = document
//       .getElementById("table-search")
//       .value.toLowerCase();
//     let total = 0;
  
//     // Recorremos todas las filas con contenido de la tabla
//     for (let i = 1; i < tableReg.rows.length; i++) {
//       // Si el td tiene la clase "noSearch" no se busca en su contenido
//       if (tableReg.rows[i].classList.contains("noSearch")) {
//         continue;
//       }
  
//       let found = false;
//       const cellsOfRow = tableReg.rows[i].getElementsByTagName("td");
  
//       // Recorremos todas las celdas
//       for (let j = 0; j < cellsOfRow.length && !found; j++) {
//         const compareWith = cellsOfRow[j].innerHTML.toLowerCase();
  
//         // Buscamos el texto en el contenido de la celda
//         if (
//           searchText.length == 0 ||
//           compareWith.indexOf(searchText) > -1
//         ) {
//           found = true;
//           total++;
//         }
//       }
  
//       if (found) {
//         tableReg.rows[i].style.display = "";
//       } else {
//         // si no ha encontrado ninguna coincidencia, esconde la fila de la tabla
//         tableReg.rows[i].style.display = "none";
//       }
//     }
  
//     // mostramos las coincidencias
//     const lastTR = tableReg.rows[tableReg.rows.length - 1];
//     const td = lastTR.querySelector("td");
//     lastTR.classList.remove("hide", "text-red-500");
  
//     if (searchText == "") {
//       lastTR.classList.add("hide");
//       td.innerHTML = "";
//     } else if (total) {
//       td.innerHTML =
//         "Se ha encontrado " +
//         total +
//         " coincidencia" +
//         (total > 1 ? "s" : "");
//     } else {
//       lastTR.classList.add("text-red-500");
//       td.innerHTML = "No se han encontrado coincidencias";
//     }
//   }