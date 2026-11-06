# ⏱️ Sistema de Automatización de Marcaciones

Sistema desarrollado en Python para registrar y verificar las marcaciones de entrada y salida de empleados, identificando automáticamente atrasos y salidas anticipadas según el horario establecido.

## 🎯 Objetivo

Automatizar el control de asistencia de los empleados mediante el registro de sus marcaciones, permitiendo determinar si una entrada es normal o atrasada, y si una salida es anticipada o posterior al horario laboral.

## ⚙️ Funcionalidades

- **Gestión de empleados:** registrar empleados con nombre y departamento.
- **Registro de marcaciones:** almacenar entradas y salidas con fecha y hora.
- **Detección de atrasos:** identificar entradas posteriores a las 08:15.
- **Detección de salidas anticipadas:** identificar salidas anteriores a las 17:00.
- **Clasificación de marcaciones:** determinar el estado de cada registro.
- **Almacenamiento de datos:** guardar la información en PostgreSQL.

## 🧰 Tecnologías

| Tecnología | Función |
|---|---|
| Python | Lógica y reglas de negocio. |
| FastAPI | Crear la API y exponer sus funcionalidades. |
| PostgreSQL | Almacenar empleados y marcaciones. |
| Make.com | Automatizar el flujo de trabajo e integrar servicios. |

### Construcción por componentes

El proyecto se desarrolla por etapas:

1. **Python:** implementar la lógica de registro y validación de marcaciones.
2. **PostgreSQL:** crear las tablas para almacenar la información.
3. **FastAPI:** exponer la lógica mediante endpoints HTTP y generar documentación automática.
4. **Make.com:** conectar los componentes y automatizar el proceso.

## 🗄️ Modelo de datos

El sistema utiliza dos entidades relacionadas:

### Empleado

| Campo | Tipo | Descripción |
|---|---|---|
| empleado_id | INTEGER | Identificador único (PK). |
| nombre | VARCHAR | Nombre del empleado. |
| departamento | VARCHAR | Departamento al que pertenece. |

### Marcacion

| Campo | Tipo | Descripción |
|---|---|---|
| marcacion_id | INTEGER | Identificador único (PK). |
| tipo | VARCHAR | Entrada o salida. |
| fecha_hora | TIMESTAMP | Fecha y hora del registro. |
| estado | VARCHAR | Resultado de la validación. |
| empleado_id | INTEGER | Identificador del empleado (FK). |

### Relación

Un empleado puede tener múltiples marcaciones. Cada marcación pertenece a un único empleado.

## 📋 Reglas de negocio

Las siguientes reglas determinan cómo se clasifican las marcaciones:

**Horario de entrada: 08:15**

- Una entrada hasta las 08:15 inclusive se considera `normal`.
- Una entrada posterior a las 08:15 se considera `atrasado`.

**Horario de salida: 17:00**

- Una salida anterior a las 17:00 se considera `salida anticipada`.
- Una salida posterior a las 17:00 se considera `salida posterior`.
- Una salida exactamente a las 17:00 se considera `normal`.

**Reglas generales**

- Cada empleado debe tener un identificador único.
- Cada marcación debe contener un empleado, un tipo y una fecha y hora.
- Solo se permiten dos tipos de marcación: `entrada` y `salida`.
- El estado se determina automáticamente según el tipo de marcación y el horario establecido.

## 📁 Estructura del proyecto

```text
automatizacion-basica-marcaciones/
│
├── api/
│   ├── base_de_datos.py
│   ├── crear_tablas.py
│   ├── entidades.py
│   ├── main.py
│   ├── modelos.py
│   └── servicios.py
│
├── simulador/
│   └── simulador.py
│
├── tests/
│   └── test_servicios.py
│
├── .gitignore
├── diagrama.jpg
├── requirements.txt
└── README.md
```

### Descripción de los componentes

| Archivo | Responsabilidad |
|---|---|
| `base_de_datos.py` | Configuración de conexión a PostgreSQL. |
| `crear_tablas.py` | Creación de las tablas. |
| `entidades.py` | Definición de las entidades. |
| `modelos.py` | Modelos utilizados por la API. |
| `main.py` | Punto de entrada de FastAPI. |
| `servicios.py` | Lógica de registro y validación. |
| `simulador.py` | Simulación de marcaciones de empleados. |
| `test_servicios.py` | Pruebas de la lógica del sistema. |

## 🚀 Instalación y ejecución

**1. Clonar el repositorio**

```bash
git clone URL_DEL_REPOSITORIO
cd automatizacion-marcaje
```

**2. Crear un entorno virtual**

```bash
python -m venv venv
```

**3. Activar el entorno virtual**

Windows:

```bash
venv\Scripts\activate
```

**4. Instalar dependencias**

```bash
pip install -r requirements.txt
```

**5. Configurar PostgreSQL**

Configurar los datos de conexión a la base de datos antes de ejecutar el proyecto.

**6. Crear las tablas**

```bash
python -m api.crear_tablas
```

**7. Iniciar la API**

```bash
uvicorn api.main:app --reload
```

La documentación automática de FastAPI estará disponible en:

```text
http://127.0.0.1:8000/docs
```

## 🧪 Pruebas

Para ejecutar las pruebas de los servicios:

```bash
pytest
```

## 📌 Estado del proyecto

Proyecto en desarrollo. Se construye progresivamente mediante componentes independientes, comenzando por la lógica de negocio y avanzando hacia la integración y automatización del proceso.

---

**Creado y desarrollado por Elías Soto.**