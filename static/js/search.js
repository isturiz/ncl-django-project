
document.addEventListener("DOMContentLoaded", function() {
    // for lesson seen and student active it's the same constant
    const STATUS = {
        ACTIVE: "active", 
        INACTIVE: "inactive",
    };
    
    const tableSearch = document.getElementById("table-search");
    const tableRows = document.querySelectorAll("#table-file tbody tr");
    const filterStatus = document.getElementById("filter-status");
    const resultMessage = document.getElementById("search-result-message");

    function filterTable() {
        const searchText = tableSearch.value.trim().toLowerCase();
        const filterValue = filterStatus.value;
        console.log(filterValue)
        let matchCount = 0;

        tableRows.forEach(function(row) {
            const rowData = row.textContent.toLowerCase();
            const isActive = row.dataset.status === STATUS.ACTIVE;
            console.log(isActive)

            // Active / Inactive filter
            if ((filterValue === "" || (filterValue === STATUS.ACTIVE && isActive) || (filterValue === STATUS.INACTIVE && !isActive)) && rowData.includes(searchText)) {
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
    }

    // Escuchar cambios en el filtro y el campo de búsqueda
    tableSearch.addEventListener("input", filterTable);
    filterStatus.addEventListener("change", filterTable);
});

