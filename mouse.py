import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)  # Only one hand for simplicity
mp_draw = mp.solutions.drawing_utils

# Get screen size
screen_width, screen_height = pyautogui.size()

# Start video capture
camera = cv2.VideoCapture(0)

while True:
    ret, image = camera.read()
    if not ret:
        break

    image = cv2.flip(image, 1)  # Mirror the image
    image_height, image_width, _ = image.shape

    # Convert to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_image)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark

            # Get index finger tip (id=8) and thumb tip (id=4)
            index_finger_tip = landmarks[8]
            thumb_tip = landmarks[4]

            # Convert normalized coordinates to screen coordinates
            x1 = int(index_finger_tip.x * image_width)
            y1 = int(index_finger_tip.y * image_height)

            x2 = int(thumb_tip.x * image_width)
            y2 = int(thumb_tip.y * image_height)

            # Draw circles
            cv2.circle(image, (x1, y1), 10, (0, 255, 255), cv2.FILLED)
            cv2.circle(image, (x2, y2), 10, (0, 255, 255), cv2.FILLED)

            # Move mouse based on index finger
            screen_x = int(index_finger_tip.x * screen_width)
            screen_y = int(index_finger_tip.y * screen_height)
            pyautogui.moveTo(screen_x, screen_y)

            # Calculate distance between thumb and index finger
            distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
            print(f"Distance: {distance}")

            if distance < 40:  # Threshold for "click"
                pyautogui.click()
                print("Clicked")

    # Display the image
    cv2.imshow("Hand Tracking Mouse Control", image)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release resources
camera.release()
cv2.destroyAllWindows()
