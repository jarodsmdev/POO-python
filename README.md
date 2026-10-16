<div align="center">

# Python POO

### Curso de Programación Orientada a Objetos en Python

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![POO](https://img.shields.io/badge/Paradigma-POO-4B8BBE?style=for-the-badge&logo=codeigniter&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-En%20progreso-success?style=for-the-badge)
![Licencia](https://img.shields.io/badge/Licencia-MIT-yellow?style=for-the-badge)
![Idioma](https://img.shields.io/badge/Idioma-Espa%C3%B1ol-red?style=for-the-badge)

Repositorio de estudio y práctica de **Programación Orientada a Objetos** con Python.
Organizado por *tracks* progresivos, ejercicios y proyectos aplicados.

</div>

---

## Tabla de contenidos

- [Descripción](#descripción)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Contenido por track](#contenido-por-track)
- [Proyectos destacados](#proyectos-destacados)
- [Requisitos](#requisitos)
- [Cómo ejecutar](#cómo-ejecutar)
- [Conceptos cubiertos](#conceptos-cubiertos)
- [Autor](#autor)
- [Licencia](#licencia)

---

## Descripción

Este repositorio reúne el material, los ejercicios y los proyectos desarrollados durante
el aprendizaje de **POO en Python**. Avanza de forma incremental: desde la creación de
clases y objetos hasta el diseño de aplicaciones completas con encapsulamiento,
composición y persistencia básica.

---

## Estructura del repositorio

```text
PYTHON_POO/
├── DESARROLLO/            # Ejercicios de desarrollo incremental (1.py – 5.py)
├── EJERCICIOS/            # Ejercicios numerados (1 – 30)
├── EJERCICIOS_PYTHON/     # Listas, diccionarios y funciones
├── GUIAS_JAVIER_PEÑA/     # Guías teóricas y ejemplos (PDF + Python)
├── POO/                   # Fundamentos: clase Producto y documentación
├── PRACTICA/              # Prácticas aplicadas (productos, envíos)
├── TRACK2/                # Introducción a clases y objetos
├── TRACK3/                # Métodos, funciones y casos prácticos
├── TRACK4/                # Encapsulamiento y cuentas bancarias
├── TRACK5/                # Proyecto tienda (v1 y v2)
├── TRACK6/                # Ensayos y evaluación
└── TRACK7/                # Caso integrador: bodega (FPY1101)
```

---

## Contenido por track

| Track | Tema | Archivos clave |
|:-----:|------|----------------|
| **2** | Clases y objetos | `Producto.py`, `creandoClase.py` |
| **3** | Métodos y funciones | `funciones.py`, `Caso1.py` – `Caso4.py` |
| **4** | Encapsulamiento | `cuentaBancaria.py`, `encapsulamiento1.py` – `4.py` |
| **5** | Composición y aplicaciones | `tienda_v1/`, `tienda_v2/` |
| **6** | Evaluación | `ENSAYO V.py` |
| **7** | Caso integrador | `FPY1101.py` |

---

## Proyectos destacados

### Tienda v2 — Sistema de carrito
Aplicación de consola con menú interactivo que gestiona productos y un carrito de compras.

```text
TRACK5/tienda_v2/
├── main.py
└── models/
    ├── application.py   # Lógica y menú principal
    ├── producto.py      # Entidad Producto
    ├── carrito.py       # Carrito de compras
    └── item_carrito.py  # Ítem del carrito
```

### Cuenta Bancaria — Encapsulamiento
Clase `CuentaBancaria` con atributos privados, depósitos, retiros y validaciones seguras.

### Bodega — Caso integrador
Gestión de productos con diccionarios: registro, stock, ventas y valorización total.

---

## Requisitos

![Python](https://img.shields.io/badge/Requiere-Python%203.8%2B-blue?style=flat-square&logo=python&logoColor=white)

- Python **3.8 o superior**
- Sin dependencias externas

---

## Cómo ejecutar

Clona el repositorio e ingresa al directorio:

```bash
git clone <url-del-repositorio>
cd PYTHON_POO
```

Ejecuta cualquier script directamente:

```bash
# Proyecto tienda v2
python -m TRACK5.tienda_v2.main

# Caso integrador bodega
python TRACK7/FPY1101.py

# Fundamentos de POO
python POO/1.ClaseProducto.py
```

---

## Conceptos cubiertos

<div align="center">

![Clases](https://img.shields.io/badge/Clases-y%20Objetos-3776AB?style=flat-square)
![Herencia](https://img.shields.io/badge/Constructor-__init__-4B8BBE?style=flat-square)
![Métodos](https://img.shields.io/badge/Métodos-y%20self-306998?style=flat-square)
![Encapsulamiento](https://img.shields.io/badge/Encapsulamiento-Private%20%2F%20Public-FFD43B?style=flat-square)
![Dunder](https://img.shields.io/badge/Métodos%20especiales-__str__-FFE873?style=flat-square)
![Composición](https://img.shields.io/badge/Composición-Objetos-8A2BE2?style=flat-square)

</div>

- Definición de **clases** y creación de **objetos**
- **Constructor** `__init__` y uso de `self`
- **Atributos** públicos y privados
- **Métodos** de instancia y de negocio
- Métodos especiales (`__str__`)
- **Encapsulamiento** con *getters* y *setters*
- **Composición** de objetos (carrito, ítems)

---

## Autor

<div align="center">

**Hecho con dedicación para el aprendizaje de Python**

![Hecho con](https://img.shields.io/badge/Hecho%20con-Python%20%2B%20%E2%9D%A4-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

---

## Licencia

Distribuido bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más información.

<div align="center">

![MIT](https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge)

</div>
