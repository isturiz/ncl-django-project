// Only letters 
//data-validate-only-letters="true" <- property
const validateOnlyLettersInput = (inputField) => {
    inputField.addEventListener("input", () => {
        const inputValue = inputField.value;
        const isValid = /^[A-Za-zÁáÉéÍíÓóÚúÜüÑñ´.]*$/.test(inputValue);

        if (!isValid) {
            // alert("El campo debe contener solo letras.");
            inputField.value = inputValue.replace(/[^A-Za-zÁáÉéÍíÓóÚúÜüÑñ´.]+/g, "");
        }
    });
};






const validateLetterInputs = document.querySelectorAll("[data-validate-only-letters='true']");

validateLetterInputs.forEach((input) => {
    validateOnlyLettersInput(input);
});

// Only numbers
const validateOnlyNumbers = (inputField) => {
    inputField.addEventListener("input", () => {
        const inputValue = inputField.value;
        const isValid = /^\d+$/.test(inputValue); // Expresión regular para permitir solo números

        if (!isValid) {
            //alert("El campo debe contener solo números.");
            inputField.value = inputValue.replace(/[^\d]+/g, ""); // Eliminar caracteres no numéricos
        }
    });
};

const validateNumberInputs = document.querySelectorAll("[data-validate-only-numbers='true']");

validateNumberInputs.forEach((input) => {
    validateOnlyNumbers(input);
});


// Only dates
const validateOnlyDates = (inputField) => {
    inputField.addEventListener("input", () => {
        const inputValue = inputField.value;
        // El regex permite solo números y / en el formato dd/mm/yyyy
        const isValid = /^(\d{0,2}\/\d{0,2}\/\d{0,4})$/.test(inputValue);
        
        if (!isValid) {
            // Eliminar caracteres no válidos y corregir el formato
            const cleanedValue = inputValue.replace(/[^0-9/]/g, "");
            const parts = cleanedValue.split('/');
            if (parts[0] && parts[0].length > 2) {
                parts[0] = parts[0].slice(0, 2);
            }
            if (parts[1] && parts[1].length > 2) {
                parts[1] = parts[1].slice(0, 2);
            }
            if (parts[2] && parts[2].length > 4) {
                parts[2] = parts[2].slice(0, 4);
            }
            inputField.value = parts.join('/');
        }
    });
};

const validateDateInputs = document.querySelectorAll("[data-validate-only-dates='true']");

validateDateInputs.forEach((input) => {
    validateOnlyDates(input);
});
