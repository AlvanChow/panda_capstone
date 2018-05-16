
<html>


<?php
    include("header.php");
?>

<head>
    <link rel="stylesheet" href="/static/mpg.css"/>
    <title>MPG</title>
</head>

<body>

    <img src="https://www.tesla.com/sites/default/files/images/software_update.jpg" alt = 'Tesla'/>
    <ul>
      <li><a href="/about"> About </a> </li>
      <li><a href="/faq">FAQ </a></li>
      <li><a href="/mpg"> MPG</a> </li>
    </ul>


    <h1>Tesla Page</h1>

    <label> Cylinders </label>
    <input id="cylinders"  type="text" value="6"/>

    <label> Horsepower </label>
    <input id="horsepower"  type="number" value="125"/>

    <label> Weight </label>
    <input id="weight"  type="number" value="2500"/>

    <br />
    <br />
    <button id = "inference"> Predict MPG </button>
    <input id = "mpg" type="text" readonly/>


    <button id = "scatter-button">Scatter Plot</button>
    <div id = "graph1"></div>
    <button id = "histo-button">Histogram</button>
    <div id = "graph2"></div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/plotly.js/1.35.2/plotly.min.js"></script>
    <script src="/static/mpg.js"></script>




</body>

</html>
