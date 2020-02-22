import cv2

cap = cv2.VideoCapture(0)
forcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', forcc, 20.0, (640, 480))

while cap.isOpened():
    #ret is boolean value if frame is valid
    ret, frame = cap.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        out.write(frame)

        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()