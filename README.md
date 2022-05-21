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