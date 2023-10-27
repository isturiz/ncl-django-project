// Only letters 
//data-validate-letters="true"
const validateInput = (inputField) => {
    inputField.addEventListener("input", () => {
        const inputValue = inputField.value;
        const isValid = /^[A-Za-z]+$/.test(inputValue);

        if (!isValid) {
            alert("El campo debe contener solo letras.");
            inputField.value = inputValue.replace(/[^A-Za-z]+/g, "");
        }
    });
};

const validateNumbers = (inputField) => {
    inputField.addEventListener("input", () => {
        const inputValue = inputField.value;
        const isValid = /^\d+$/.test(inputValue); // Expresión regular para permitir solo números

        if (!isValid) {
            alert("El campo debe contener solo números.");
            inputField.value = inputValue.replace(/[^\d]+/g, ""); // Eliminar caracteres no numéricos
        }
    });
};


// student_form.html



document.addEventListener("DOMContentLoaded", function () {
    const firstNameField = document.getElementById("id_first_name");
    const secondNameField = document.getElementById("id_second_name");
    const firstSurnameField  = document.getElementById("id_first_surname");
    const secondSurnameField  = document.getElementById("id_second_surname");
    
    function validateInput(inputField) {
        inputField.addEventListener("input", function () {
            const inputValue = inputField.value;
            const isValid = /^[A-Za-z]+$/.test(inputValue);

            if (!isValid) {
                alert("El campo debe contener solo letras.");
                inputField.value = inputValue.replace(/[^A-Za-z]+/g, "");
            }
        });
    }

    validateInput(firstNameField);
    validateInput(secondNameField);
    validateInput(firstSurnameField);
    validateInput(secondSurnameField);
});

document.addEventListener("DOMContentLoaded", function () {
    const phoneField = document.getElementById("id_phone_number");
    const identifyCardField = document.getElementById("id_identify_card");

    function validateNumericField(field) {
        field.addEventListener("input", function () {
            const inputValue = field.value;
            const numericValue = inputValue.replace(/\D/g, ''); // Elimina todos los caracteres que no sean dígitos
            field.value = numericValue;

            if (inputValue !== numericValue) {
                alert("El campo debe contener solo números.");
            }
        });
    }

    validateNumericField(phoneField);
    validateNumericField(identifyCardField);
});


document.addEventListener("DOMContentLoaded", function () {
    const emailField = document.getElementById("id_email");

    emailField.addEventListener("change", function () {
        const inputValue = emailField.value;
        // Expresión regular para validar una dirección de correo electrónico
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

        if (!emailPattern.test(inputValue)) {
            alert("Por favor, ingrese una dirección de correo electrónico válida.");
            emailField.value = ''; // Limpia el campo si la dirección no es válida
        }
    });
});




// teacher_form.html

document.addEventListener("DOMContentLoaded", function () {
    const firstNameField = document.getElementById("id_first_name");
    const secondNameField = document.getElementById("id_second_name");
    const firstSurnameField  = document.getElementById("id_first_surname");
    const secondSurnameField  = document.getElementById("id_second_surname");
    
    function validateInput(inputField) {
        inputField.addEventListener("input", function () {
            const inputValue = inputField.value;
            const isValid = /^[A-Za-z]+$/.test(inputValue);

            if (!isValid) {
                alert("El campo debe contener solo letras.");
                inputField.value = inputValue.replace(/[^A-Za-z]+/g, "");
            }
        });
    }

    validateInput(firstNameField);
    validateInput(secondNameField);
    validateInput(firstSurnameField);
    validateInput(secondSurnameField);
});

document.addEventListener("DOMContentLoaded", function () {
    const phoneField = document.getElementById("id_phone_number");
    const identifyCardField = document.getElementById("id_identify_card");

    function validateNumericField(field) {
        field.addEventListener("input", function () {
            const inputValue = field.value;
            const numericValue = inputValue.replace(/\D/g, ''); // Elimina todos los caracteres que no sean dígitos
            field.value = numericValue;

            if (inputValue !== numericValue) {
                alert("El campo debe contener solo números.");
            }
        });
    }

    validateNumericField(phoneField);
    validateNumericField(identifyCardField);

document.addEventListener("DOMContentLoaded", function () {
    const emailField = document.getElementById("id_email");

    emailField.addEventListener("change", function () {
        const inputValue = emailField.value;
        // Expresión regular para validar una dirección de correo electrónico
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

        if (!emailPattern.test(inputValue)) {
            alert("Por favor, ingrese una dirección de correo electrónico válida.");
            emailField.value = ''; // Limpia el campo si la dirección no es válida
        }
    });
});




// subscription_types_form.html


document.addEventListener("DOMContentLoaded", function () {
    const nameField = document.getElementById("id_name");

    
    function validateInput(inputField) {
        inputField.addEventListener("input", function () {
            const inputValue = inputField.value;
            const isValid = /^[A-Za-z]+$/.test(inputValue);

            if (!isValid) {
                alert("El campo debe contener solo letras.");
                inputField.value = inputValue.replace(/[^A-Za-z]+/g, "");
            }
        });
    }

    validateInput(nameField);
});
