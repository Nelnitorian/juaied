# Manual de uso

## src.loggerConf

### configureLogger()
_Se creará la carpeta 'log' en el lugar de ejecución y se devolverá tanto un logger como un handler._

_Para la creación:_

```
    logger,handler = loggerConf.configureLogger()
```

_Para la finalización:_

```
    loggerConf.removeLogger(logger,handler)
```

## PdfMaker

### PdfMaker(logger, username, nombre, apellidos, tarifa, qty, uprice, money, monitor)
_Se le han de pasar todos los argumentos, entre ellos el logger que generará los logs._

_Ejemplo de uso:_

```
    pdfmaker = PdfMaker(logger, username, nombre, apellidos, tarifa, qty, uprice, money, monitor)
```

### PdfMaker.dumpPdf()
_Una vez se tiene la clase creada, se ha de llamar al método dumpPdf para generar el pdf._

```
    pdfmaker.dumpPdf()
```

### Ejemplo completo de uso
```
    logger,handler = loggerConf.configureLogger()

    username = "usuario123"
    nombre = "pepe antonio"
    apellidos = "el del barrio"
    tarifa = "premium23"

    qty = 5
    uprice = 10
    money = 50
    monitor = "paquetes"

    pdfmaker = PdfMaker(logger, username, nombre, apellidos, tarifa, qty, uprice, money, monitor)
    pdfmaker.dumpPdf()
    loggerConf.removeLogger(logger,handler)
```
