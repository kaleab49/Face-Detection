
import threading
import cv2
from deepface import DeepFace

# Initialize webcam
cap = cv2.VideoCapture(0)  

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

# Load reference image
reference_img = cv2.imread("ref.jpg")

def check_face(frame):
  global face_match
  try:
      if DeepFace.verify(frame, reference_img.copy())['verified']:
          face_match = True
      else:
          face_match = False
  except Exception as e:
      print("DeepFace error:", e)  # Debugging output
      face_match = False

while True:
  ret, frame = cap.read()
  if ret:
      if counter % 30 == 0:
          threading.Thread(target=check_face, args=(frame.copy(),)).start()
      counter += 1
      
      # Display result
      text = "MATCH!" if face_match else "NO MATCH!"
      color = (255, 0, 0) if face_match else (0, 0, 255)
      cv2.putText(frame, text, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)
      
      cv2.imshow("Video", frame)

  # Exit when 'q' is pressed
  if cv2.waitKey(1) & 0xFF == ord("q"):
      break

# Cleanup
cap.release()
cv2.destroyAllWindows()
