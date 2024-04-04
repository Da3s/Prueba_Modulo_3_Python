from string import Template

# instantiate template
template = Template("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>
    <h1>Aves de Chile</h1>
    <br>

    $contenido
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</body>

</html>                   
""")

template2 = Template("""
    <div class="card" style="width: 18rem;">
        <img src="$url_img_full"
            class="card-img-top" alt="$nombre_espanol" width="200">
        <div class="card-body">
            <h5 class="card-title">$nombre_espanol</h5>
            <p class="card-text">$nombre_ingles</p>
        </div>
    </div>
""")