import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (width, 0), (0, height), (0, 255, 0), 5)
    img = cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 255), 5)
    img = cv2.circle(img, (400, 400), 50, (255, 255, 0), -1)
    img = cv2.ellipse(img, (300, 300), (100, 50), 0, 0, 180, (255, 0, 255), -1)
    img = cv2.putText(
        img, "OpenCV", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 150, 0), 3
    )
    img = cv2.putText(
        img, "Naruto", (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 150, 0), 3
    )

    cv2.imshow("frame", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
