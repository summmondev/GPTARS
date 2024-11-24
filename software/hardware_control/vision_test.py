import cv2

def vision_test():
    """
    Test the robot's vision by detecting objects with OpenCV.
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera not detected.")
        return

    print("Starting vision test...")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Vision Test", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Vision test complete.")
