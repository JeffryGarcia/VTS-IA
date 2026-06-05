from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")


cap = cv2.VideoCapture("traffic.mp4")


vehicle_classes = [
    "car",
    "motorcycle",
    "bus",
    "truck"
]

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame, verbose=False)

    carros = 0
    motos = 0
    buses = 0
    camiones = 0

    for result in results:

        boxes = result.boxes

        for box in boxes:

            cls = int(box.cls[0])

            nombre = model.names[cls]

            if nombre not in vehicle_classes:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                nombre,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

            if nombre == "car":
                carros += 1

            elif nombre == "motorcycle":
                motos += 1

            elif nombre == "bus":
                buses += 1

            elif nombre == "truck":
                camiones += 1

    total = carros + motos + buses + camiones

    if total >= 15:
        estado = "CONGESTION ALTA"
        prioridad = "CARRIL NORTE"

    elif total >= 8:
        estado = "TRAFICO MEDIO"
        prioridad = "NORMAL"

    else:
        estado = "TRAFICO BAJO"
        prioridad = "NINGUNA"

    cv2.putText(
        frame,
        f"Vehiculos: {total}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Carros: {carros}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Motos: {motos}",
        (20, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Buses: {buses}",
        (20, 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Camiones: {camiones}",
        (20, 170),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        estado,
        (20, 220),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        f"Prioridad: {prioridad}",
        (20, 260),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 0, 0),
        2
    )

    cv2.imshow(
        "Sistema Inteligente de Trafico",
        frame
    )

    tecla = cv2.waitKey(1)

    if tecla == 27:
        break

cap.release()
cv2.destroyAllWindows()