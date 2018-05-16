$(document).ready(function () {
    console.log('web page is ready');
    $('#inference').click(async function () {
        console.log('button was clicked');
        const cylinders = parseFloat($('#cylinders').val());
        const horsepower = parseFloat($('#horsepower').val());
        const weight = parseFloat($('#weight').val());
        const data = {
            cylinders,
            horsepower,
            weight
        };
        console.log(data);

        const response = await $.ajax('/inference', {
            data: JSON.stringify(data),
            method: 'post',
            contentType: 'application/json'
        });

        console.log('response', response);
        $('#mpg').val(response.prediction);
    });
    $('#scatter-button').click(async function () {
        console.log('scatter');
        const response = await $.ajax('/plot');
        const mpg = response.map(a => a[0]);
        const weight = response.map(a => a[1]);
        console.log(mpg);
        const trace = [{
            x: weight,
            y: mpg,
            mode: 'markers',
            type: 'scatter'
        }];
        const layout = {
            xaxis: {
                title: 'Weight'
            },
            yaxis: {
                title: 'MPG'
            },
            title: 'MPG by Weight',
            width: 700,
            height: 300
        };
        Plotly.plot($('#graph1')[0], trace, layout);
    });
    $('#histo-button').click(async function () {
        console.log('histogram');
        const response = await $.ajax('/plot');
        const mpg = response.map(a => a[0]);
        const trace = [{
            x: mpg,
            type: 'histogram'
        }];
        const layout = {
            xaxis: {
                title: 'MPG'
            },
            yaxis: {
                title: 'Count'
            },
            title: 'MPG by Count',
            width: 700,
            height: 300
        };
        Plotly.plot($('#graph2')[0], trace, layout);
        console.log('histogram');


        $('#panda_click').click(async function () {
            console.log('asd');

            $('#panda_output').val('asd');


    });
});
