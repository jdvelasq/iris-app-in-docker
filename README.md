# Contenerización de una aplicación en Docker

Este ejemplo demuestra la creación de una aplicación contenerizadaa partir
de un modelo de machine learning.**

**Entrenamiento del modelo**

```bash
$ make train
```

**Creación del contenedor**

```bash
$ make build
```


**Ejecución de la app**

```bash
$ docker run --rm -it  --name iris_app -p 5010:5000 jdvelasq/iris_app
```

Habra la app en http://127.0.0.1:5010