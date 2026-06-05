# VTS-IA

Sistema de simulación de tráfico inteligente basado en visión artificial para la gestión adaptativa de semáforos.

## Descripción

VTS-IA (Vehicle Traffic System with Artificial Intelligence) es un prototipo desarrollado para analizar el flujo vehicular mediante visión artificial utilizando Python, OpenCV y YOLOv8.

El sistema procesa un video de tráfico, identifica vehículos en tiempo real y estima el nivel de congestión para apoyar la toma de decisiones en semáforos inteligentes.

## Características

* Detección de vehículos mediante Inteligencia Artificial.
* Reconocimiento de:

  * Automóviles
  * Motocicletas
  * Autobuses
  * Camiones
* Conteo automático de vehículos.
* Clasificación del nivel de tráfico.
* Simulación de prioridad para semáforos inteligentes.
* Procesamiento de video en tiempo real.

## Tecnologías utilizadas

* Python 3.13+
* OpenCV
* Ultralytics YOLOv8
* NumPy

## Estructura del proyecto

```text
VTS-IA/
│
├── cameras.py      # Código principal
├── traffic.mp4     # Video de prueba
├── yolov8n.pt      # Modelo YOLOv8
└── README.md
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/JeffryGarcia/VTS-IA.git
cd VTS-IA
```

### 2. Crear un entorno virtual (opcional)

```bash
python -m venv venv
```

Activar en Windows:

```bash
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install opencv-python
pip install ultralytics
pip install numpy
```

También puedes instalar todo con:

```bash
pip install opencv-python ultralytics numpy
```

## Ejecución

Ejecutar el sistema:

```bash
python cameras.py
```

## Funcionamiento

1. El sistema carga el video `traffic.mp4`.
2. YOLOv8 analiza cada fotograma.
3. Se detectan y clasifican los vehículos presentes.
4. Se realiza un conteo automático.
5. Se calcula el nivel de congestión.
6. Se determina la prioridad de circulación.
7. La información se muestra en tiempo real sobre el video.

## Ejemplo de salida

```text
Vehiculos: 18
Carros: 12
Motos: 3
Buses: 1
Camiones: 2

CONGESTION ALTA
Prioridad: CARRIL NORTE
```

## Aplicación en Semáforos Inteligentes

Este proyecto forma parte de una propuesta de semáforos inteligentes donde cámaras y algoritmos de visión artificial analizan el tráfico para optimizar los tiempos de luz verde, reducir congestionamientos y mejorar la movilidad urbana.

## Autor

Jeffry A. García

## Licencia

Proyecto desarrollado con fines académicos y educativos.
