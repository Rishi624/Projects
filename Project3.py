# # import cv2
# # import mediapipe as mp
# # import pyautogui
# # import time

# # # Initialize MediaPipe Hand Tracking
# # mp_drawing = mp.solutions.drawing_utils
# # mp_hands = mp.solutions.hands

# # # Get screen dimensions
# # screen_width, screen_height = pyautogui.size()

# # # Camera setup
# # cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

# # # Parameters for click detection (adjust as needed)
# # CLICK_THRESHOLD_TIME = 0.3  # Time in seconds finger needs to be still to register a click
# # finger_stable_start_time = None
# # previous_finger_position = None

# # with mp_hands.Hands(
# #     static_image_mode=False,
# #     max_num_hands=1,
# #     min_detection_confidence=0.7,
# #     min_tracking_confidence=0.5) as hands:

# #     while cap.isOpened():
# #         success, image = cap.read()
# #         if not success:
# #             print("Ignoring empty camera frame.")
# #             continue

# #         # Flip the image horizontally for a later selfie-view display, and convert
# #         # the BGR image to RGB.
# #         image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
# #         image.flags.writeable = False

# #         # Process the image and get hand landmarks
# #         results = hands.process(image)

# #         # Draw the hand annotations on the image.
# #         image.flags.writeable = True
# #         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# #         if results.multi_hand_landmarks:
# #             for hand_landmarks in results.multi_hand_landmarks:
# #                 # Get the index finger tip landmark (index 8)
# #                 index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

# #                 # Get the height and width of the image
# #                 image_height, image_width, _ = image.shape

# #                 # Convert normalized landmark coordinates to screen coordinates
# #                 finger_x = int(index_finger_tip.x * screen_width)
# #                 finger_y = int(index_finger_tip.y * screen_height)

# #                 # Move the mouse cursor
# #                 pyautogui.moveTo(finger_x, finger_y)

# #                 # Basic click detection (if finger stays relatively still)
# #                 current_finger_position = (finger_x, finger_y)
# #                 if previous_finger_position is not None:
# #                     distance = ((current_finger_position[0] - previous_finger_position[0])**2 +
# #                                 (current_finger_position[1] - previous_finger_position[1])**2)**0.5
# #                     if distance < 10:  # Adjust this threshold
# #                         if finger_stable_start_time is None:
# #                             finger_stable_start_time = time.time()
# #                         elif time.time() - finger_stable_start_time >= CLICK_THRESHOLD_TIME:
# #                             pyautogui.click()
# #                             finger_stable_start_time = None
# #                     else:
# #                         finger_stable_start_time = None

# #                 previous_finger_position = current_finger_position

# #                 # Draw the landmark on the image
# #                 mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

# #         # Display the image
# #         cv2.imshow('Hand Tracking', image)
# #         if cv2.waitKey(5) & 0xFF == 27:  # Press Esc to exit
# #             break

# # cap.release()
# # cv2.destroyAllWindows()










# import cv2
# import mediapipe as mp
# import pyautogui
# import time
# import collections

# # Initialize MediaPipe Hand Tracking
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands

# # Get screen dimensions
# screen_width, screen_height = pyautogui.size()

# # Camera setup
# cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

# # --- Cursor Smoothing Parameters ---
# SMOOTHING_WINDOW = 5  # Number of previous positions to average
# finger_position_history = collections.deque(maxlen=SMOOTHING_WINDOW)

# # --- Movement Threshold Parameter ---
# MOVEMENT_THRESHOLD = 8  # Minimum pixel movement to update cursor

# # --- Click Detection Parameters ---
# CLICK_THRESHOLD_TIME = 0.3  # Time in seconds finger needs to be still to register a click
# finger_stable_start_time = None
# previous_finger_position_raw = None
# previous_smoothed_position = None

# with mp_hands.Hands(
#     static_image_mode=False,
#     max_num_hands=1,
#     min_detection_confidence=0.7,
#     min_tracking_confidence=0.5) as hands:

#     while cap.isOpened():
#         success, image = cap.read()
#         if not success:
#             print("Ignoring empty camera frame.")
#             continue

#         # Flip the image horizontally for a later selfie-view display, and convert
#         # the BGR image to RGB.
#         image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
#         image.flags.writeable = False

#         # Process the image and get hand landmarks
#         results = hands.process(image)

#         # Draw the hand annotations on the image.
#         image.flags.writeable = True
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 # Get the index finger tip landmark (index 8)
#                 index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

#                 # Get the height and width of the image
#                 image_height, image_width, _ = image.shape

#                 # Convert normalized landmark coordinates to screen coordinates (RAW)
#                 raw_finger_x = int(index_finger_tip.x * screen_width)
#                 raw_finger_y = int(index_finger_tip.y * screen_height)
#                 current_raw_position = (raw_finger_x, raw_finger_y)

#                 # --- Apply Smoothing ---
#                 finger_position_history.append(current_raw_position)
#                 if len(finger_position_history) == SMOOTHING_WINDOW:
#                     smoothed_x = int(sum(p[0] for p in finger_position_history) / SMOOTHING_WINDOW)
#                     smoothed_y = int(sum(p[1] for p in finger_position_history) / SMOOTHING_WINDOW)
#                     current_smoothed_position = (smoothed_x, smoothed_y)
#                 else:
#                     current_smoothed_position = current_raw_position

#                 # --- Apply Movement Threshold and Move Cursor ---
#                 if previous_smoothed_position is not None:
#                     delta_x = abs(current_smoothed_position[0] - previous_smoothed_position[0])
#                     delta_y = abs(current_smoothed_position[1] - previous_smoothed_position[1])

#                     if delta_x > MOVEMENT_THRESHOLD or delta_y > MOVEMENT_THRESHOLD:
#                         pyautogui.moveTo(current_smoothed_position[0], current_smoothed_position[1])
#                 else:
#                     pyautogui.moveTo(current_smoothed_position[0], current_smoothed_position[1])

#                 # --- Basic Click Detection (based on smoothed position stability) ---
#                 if previous_smoothed_position is not None:
#                     distance = ((current_smoothed_position[0] - previous_smoothed_position[0])**2 +
#                                 (current_smoothed_position[1] - previous_smoothed_position[1])**2)**0.5
#                     if distance < 8:  # Adjust this threshold for stability
#                         if finger_stable_start_time is None:
#                             finger_stable_start_time = time.time()
#                         elif time.time() - finger_stable_start_time >= CLICK_THRESHOLD_TIME:
#                             pyautogui.click()
#                             finger_stable_start_time = None
#                     else:
#                         finger_stable_start_time = None
#                 else:
#                     finger_stable_start_time = None # Reset if no previous position

#                 previous_smoothed_position = current_smoothed_position
#                 previous_finger_position_raw = current_raw_position

#                 # Draw the landmark on the image
#                 mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#         # Display the image
#         cv2.imshow('Hand Tracking', image)
#         if cv2.waitKey(5) & 0xFF == 27:  # Press Esc to exit
#             break

# cap.release()
# cv2.destroyAllWindows()




import cv2
import mediapipe as mp
import pyautogui
import time
import collections

# Initialize MediaPipe Hand Tracking
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Camera setup
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

# --- Control State ---
finger_detected_first_time = False

# --- Cursor Smoothing Parameters ---
SMOOTHING_WINDOW = 5  # Number of previous positions to average
finger_position_history = collections.deque(maxlen=SMOOTHING_WINDOW)

# --- Movement Threshold Parameter ---
MOVEMENT_THRESHOLD = 8  # Minimum pixel movement to update cursor

# --- Click Detection Parameters ---
CLICK_THRESHOLD_TIME = 0.3  # Time in seconds finger needs to be still to register a click
finger_stable_start_time = None
previous_smoothed_position = None

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Process the image and get hand landmarks
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get the index finger tip landmark (index 8)
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                # Get the height and width of the image
                image_height, image_width, _ = image.shape

                # Convert normalized landmark coordinates to screen coordinates (RAW)
                raw_finger_x = int(index_finger_tip.x * screen_width)
                raw_finger_y = int(index_finger_tip.y * screen_height)
                current_raw_position = (raw_finger_x, raw_finger_y)

                # --- Control Flow: Move Cursor Only After First Detection ---
                if not finger_detected_first_time:
                    finger_detected_first_time = True
                    # We don't move the cursor on the very first detection
                    previous_smoothed_position = current_raw_position # Initialize with raw position
                else:
                    # --- Apply Smoothing ---
                    finger_position_history.append(current_raw_position)
                    if len(finger_position_history) == SMOOTHING_WINDOW:
                        smoothed_x = int(sum(p[0] for p in finger_position_history) / SMOOTHING_WINDOW)
                        smoothed_y = int(sum(p[1] for p in finger_position_history) / SMOOTHING_WINDOW)
                        current_smoothed_position = (smoothed_x, smoothed_y)
                    else:
                        current_smoothed_position = current_raw_position

                    # --- Apply Movement Threshold and Move Cursor ---
                    if previous_smoothed_position is not None:
                        delta_x = abs(current_smoothed_position[0] - previous_smoothed_position[0])
                        delta_y = abs(current_smoothed_position[1] - previous_smoothed_position[1])

                        if delta_x > MOVEMENT_THRESHOLD or delta_y > MOVEMENT_THRESHOLD:
                            pyautogui.moveTo(current_smoothed_position[0], current_smoothed_position[1])
                            previous_smoothed_position = current_smoothed_position
                    else:
                        pyautogui.moveTo(current_smoothed_position[0], current_smoothed_position[1])
                        previous_smoothed_position = current_smoothed_position

                    # --- Basic Click Detection (based on smoothed position stability) ---
                    if previous_smoothed_position is not None:
                        distance = ((current_smoothed_position[0] - previous_smoothed_position[0])**2 +
                                    (current_smoothed_position[1] - previous_smoothed_position[1])**2)**0.5
                        if distance < 8:  # Adjust this threshold for stability
                            if finger_stable_start_time is None:
                                finger_stable_start_time = time.time()
                            elif time.time() - finger_stable_start_time >= CLICK_THRESHOLD_TIME:
                                pyautogui.click()
                                finger_stable_start_time = None
                        else:
                            finger_stable_start_time = None
                    else:
                        finger_stable_start_time = None # Reset if no previous position

        else:
            # Reset the first detection flag if no hand is detected
            finger_detected_first_time = False
            finger_position_history.clear() # Clear history when hand is lost
            finger_stable_start_time = None # Reset click timer

        # Draw the landmark on the image
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display the image
        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(5) & 0xFF == 27:  # Press Esc to exit
            break

cap.release()
cv2.destroyAllWindows()