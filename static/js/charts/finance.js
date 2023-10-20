const paymentData = {{ payment_data|safe }};

    const totalPaymentsAmountCurrentYear = "Total anual $" + {{ total_payments|safe }};
    const totalPaymentsAmountLastThreeMonths = "Total tres meses $" + {{ total_payments_amount_last_three_months|safe }};
    const totalPaymentsAmountLastSixMonths = "Total seis meses $" + {{ total_payments_amount_last_six_months|safe }};
    const totalPaymentsAmountLastNineMonths = "Total nueve meses $" + {{ total_payments_amount_last_nine_months|safe }};

    // All months 
    const monthlyPaymentData = {{ monthly_payment_data|safe }};
        // amount -> series
    const monthPaymentPrice = monthlyPaymentData.map(item => item.total);
    console.log("monthPaymentPrice", monthPaymentPrice)
        // month -> categories
    const monthLabels = monthlyPaymentData.map(item => {
        const monthNumber = item.month;
        const monthNames = [
            "Ene", "Feb", "Mar", "Abr", "May", "Jun",
            "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"
        ];

        return monthNames[monthNumber - 1]; 
    });

    // last three months
    const lastThreeMonths = {{ payments_data_last_three_months|safe }}
    const lastThreeMonthsPrice = lastThreeMonths.map(item => item.total);
    const lastThreeMonthLabels = lastThreeMonths.map(item => {
        const monthNumber = item.month;
        const monthNames = [
            "Ene", "Feb", "Mar", "Abr", "May", "Jun",
            "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"
        ];

        return monthNames[monthNumber - 1]; 
    });

    // last six months
    const lastSixMonths = {{ payments_data_last_six_months|safe }}
    const lastSixMonthsPrice = lastSixMonths.map(item => item.total);
    const lastSixMonthLabels = lastSixMonths.map(item => {
        const monthNumber = item.month;
        const monthNames = [
            "Ene", "Feb", "Mar", "Abr", "May", "Jun",
            "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"
        ];

        return monthNames[monthNumber - 1]; 
    });

    // last nine months
    const lastNineMonths = {{ payments_data_last_nine_months|safe }}
    const lastNineMonthsPrice = lastNineMonths.map(item => item.total);
    const lastNineMonthLabels = lastNineMonths.map(item => {
        const monthNumber = item.month;
        const monthNames = [
            "Ene", "Feb", "Mar", "Abr", "May", "Jun",
            "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"
        ];

        return monthNames[monthNumber - 1]; 
    });


    console.log("monthlyPaymentData:", monthlyPaymentData)


    // Extrae las series y las etiquetas del eje X a partir de los datos
    const paymentPrices = paymentData.map(payment => parseFloat(payment.price));

    const paymentDates = paymentData.map(payment => {
        const date = new Date(payment.date);
        const day = String(date.getDate()).padStart(2, '0'); // Obtiene el día y asegura que tenga dos dígitos
        const month = String(date.getMonth() + 1).padStart(2, '0'); // Obtiene el mes (agregando 1, ya que los meses comienzan en 0) y asegura que tenga dos dígitos
        const year = date.getFullYear(); // Obtiene el año

        return `${day}/${month}/${year}`;
    });

    paymentPrices.reverse()
    paymentDates.reverse(); 
    

    console.log("paymentDates:", paymentDates)

    console.log(paymentData)
    // ApexCharts options and config
    window.addEventListener("load", function() {
        let options = {
            chart: {
            height: "100%",
            maxWidth: "100%",
            type: "area",
            fontFamily: "Inter, sans-serif",
            dropShadow: {
                enabled: false,
            },
            toolbar: {
                show: false,
            },
            },
            tooltip: {
            enabled: true,
            x: {
                show: false,
            },
            },
            fill: {
            type: "gradient",
            gradient: {
                opacityFrom: 0.55,
                opacityTo: 0,
                shade: "#1C64F2",
                gradientToColors: ["#1C64F2"],
            },
            },
            dataLabels: {
            enabled: false,
            },
            stroke: {
            width: 6,
            },
            grid: {
            show: false,
            strokeDashArray: 4,
            padding: {
                left: 2,
                right: 2,
                top: 0
            },
            },
            series: [
            {
                name: "Payments",
                data: monthPaymentPrice,
                color: "#1A56DB",
            },
            ],
            xaxis: {
                categories: monthLabels,
                labels: {
                    show: true,
                    style: {
                        fontFamily: "Inter, sans-serif",
                        cssClass: 'text-xs font-normal fill-gray-500 dark:fill-gray-400'
                    }
                    
            },
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
            },
            yaxis: {
                show: true,
                labels: {
                show: true,
                style: {
                    fontFamily: "Inter, sans-serif",
                    cssClass: 'text-xs font-normal fill-gray-500 dark:fill-gray-400'
                },
                formatter: function (value) {
                    return '$' + value;
                }
                }
            },
        }

        if (document.getElementById("area-chart") && typeof ApexCharts !== 'undefined') {
            const chart = new ApexCharts(document.getElementById("area-chart"), options);
            chart.render();
            
            const filters = {
                'current-year': {
                    total: totalPaymentsAmountCurrentYear,
                    data: monthPaymentPrice,
                    labels: monthLabels, 
                },
                'mes-pasado': [200, 10, 100, 50, 5],
                'last-three-months': {
                    total: totalPaymentsAmountLastThreeMonths,
                    data: lastThreeMonthsPrice,
                    labels: lastThreeMonthLabels, 
                }, 
                'last-six-months': {
                    total: totalPaymentsAmountLastSixMonths,
                    data: lastSixMonthsPrice,
                    labels: lastSixMonthLabels, 
                },
                'last-nine-months': {
                    total: totalPaymentsAmountLastNineMonths,
                    data: lastNineMonthsPrice,
                    labels: lastNineMonthLabels, 
                },
            };
            
            // Agrega un evento de escucha al botón de filtro.
            const filterButton = document.getElementById("filterMonthButton");
            const dropdownButton = document.getElementById("dropdownDefaultButton");
            const idTotalAmount = document.getElementById("idTotalAmount")
            filterButton.addEventListener("click", function (event) {

                event.preventDefault();
            
                // Obtiene el filtro seleccionado a través del atributo "data-filter".
                const selectedFilter = event.target.getAttribute("data-filter");
            
                // Verifica si el filtro existe en el objeto "filters" y actualiza el gráfico si es válido.
                if (filters[selectedFilter]) {
                    chart.updateSeries([{ data: filters[selectedFilter].data }]);
                    chart.updateOptions({
                        xaxis: {
                            categories: filters[selectedFilter].labels,
                        },
                    });
                    idTotalAmount.textContent = filters[selectedFilter].total
                    
                }
                if (selectedFilter) {
                    const filterText = event.target.textContent;
                    dropdownButton.textContent = filterText;
                    // Cierra el menú desplegable (si es necesario).
                    // Aquí puedes agregar código para cerrar el menú desplegable si lo deseas.
                  }
                
            });
        }
    });
