import cv2
from ultralytics import YOLO

model = YOLO("best.pt") 

def detect_drowsiness(video_source=0):

    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        print("Error: Could not open video source.")
        return
    
    print("[INFO] Starting detection... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        results = model(frame)

        drowsy_detected = False
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0]) 
                if model.names[class_id] == "Drowsy":  
                    drowsy_detected = True

                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                    confidence = box.conf[0]

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cv2.putText(
                        frame,
                        f"Drowsy {confidence:.2f}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 0, 255),
                        2,
                    )


        cv2.imshow("Drowsiness Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Detection stopped.")


if __name__ == "__main__":
    detect_drowsiness()
