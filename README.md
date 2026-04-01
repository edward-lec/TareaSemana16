# 📋 Aplicación GUI - Lista de Tareas (Semana 16)

## 📌 Descripción del Proyecto

El sistema permitirá gestionar tareas diarias a través de una interfaz gráfica desarrollada en Tkinter. A diferencia de la versión anterior, esta nueva implementación deberá permitir que el usuario interactúe tanto con el mouse como con el teclado, optimizando la experiencia de uso. Se deberá conservar la lógica del sistema previamente desarrollada, integrando nuevos eventos que permitan ejecutar acciones de forma más eficiente.



## 🎯 Objetivo

Implementar una interfaz gráfica que permita al usuario gestionar tareas (agregar, completar y eliminar) mediante el uso combinado de mouse y teclado, mejorando la experiencia de interacción sin modificar la lógica del sistema.

---

## 🧱 Arquitectura del Sistema

El proyecto está estructurado bajo una arquitectura modular por capas:

```
```plaintext
lista_tareas_app/
│
├── main.py
├── modelos/
│   ├── __init__.py
│   └── tarea.py
├── servicios/
│   ├── __init__.py
│   └── tarea_servicio.py
└── ui/
    ├── __init__.py
    └── app_tkinter.py
```

### 🔹 Descripción de capas

* **modelos/**
  Contiene la clase `Tarea`, que representa la entidad del sistema.

* **servicios/**
  Contiene la lógica de negocio (`TareaServicio`), encargada de gestionar las tareas.

* **ui/**
  Contiene la interfaz gráfica desarrollada con Tkinter (`AppTkinter`).

* **main.py**
  Punto de entrada del sistema que inicializa la aplicación.

---

## ⚙️ Funcionalidades

* ✔ Agregar tareas
* ✔ Marcar tareas como completadas
* ✔ Eliminar tareas
* ✔ Visualizar lista de tareas
* ✔ Diferenciación visual:

  * 🔴 Pendiente
  * 🟢 Completada

---

## ⌨️ Atajos de Teclado

Se implementaron eventos de teclado mediante `.bind()` para mejorar la interacción:

* **Enter** → Agregar tarea
* **c** → Marcar tarea como completada con la c minúscula
* **Delete / D** → Eliminar tarea
* **Escape** → Cerrar la aplicación

---

## 🖱️ Interacción con Mouse

* Botones para ejecutar acciones
* Doble clic sobre una tarea para marcarla como completada

---

## 🎨 Mejora de Usabilidad

El sistema mejora la experiencia del usuario mediante:

* Reducción de uso del mouse
* Interacción más rápida con teclado
* Feedback visual claro (colores por estado)
* Organización clara de la información

---

## 🛠️ Tecnologías Utilizadas

* Python
* Tkinter (interfaz gráfica)

---

---

## 📦 Generación de Ejecutable

El sistema puede ser convertido a ejecutable mediante PyInstaller:

```bash
pyinstaller --onefile --windowed main.py
```

El archivo ejecutable se generará en la carpeta:

```
dist/main.exe
```

---

## 👨‍💻 Autor

**Leiber Correa**

---

## 📚 Observaciones

El proyecto mantiene la lógica de la Semana 15, incorporando mejoras únicamente en la interfaz gráfica, respetando la separación de responsabilidades y la arquitectura por capas.

---
