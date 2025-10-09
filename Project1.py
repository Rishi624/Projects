import cv2
import mediapipe as mp
import webbrowser
import threading
import speech_recognition as sr
import time
import platform
import pyautogui
import screen_brightness_control as sbc
import os
import subprocess

def set_chrome_path():
    """Sets the Chrome path for Windows."""
    if platform.system() == "Windows":
        try:
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            print(f"Chrome path set to: {chrome_path}")
        except webbrowser.Error:
            print("Error: Could not set Chrome path. Please verify the path.")

set_chrome_path()

def open_url(url):
    """Opens a URL in Chrome."""
    try:
        webbrowser.get('chrome').open_new_tab(url)
    except webbrowser.Error:
        print(f"Error opening URL: {url}. Make sure Chrome is installed and accessible.")

def handle_voice_commands():
    recognizer = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for voice commands...")
                audio = recognizer.listen(source, timeout=1)
                command = recognizer.recognize_google(audio).lower()
                print(f"Voice Command: {command}")

            global volume_mode, brightness_mode, url_detection_mode, scroll_mode

            if "scroll" in command and "exit" not in command:
                scroll_mode = True
                volume_mode = False
                brightness_mode = False
                url_detection_mode = False
                print("Scroll control mode activated")
            elif "volume" in command:
                volume_mode = True
                brightness_mode = False
                url_detection_mode = False
                scroll_mode = False
                print("Volume control mode activated")
            elif "brightness" in command:
                volume_mode = False
                brightness_mode = True
                url_detection_mode = False
                scroll_mode = False
                print("Brightness control mode activated")
            elif "exit" in command:
                volume_mode = False
                brightness_mode = False
                url_detection_mode = True
                scroll_mode = False
                print("URL detection mode activated")
            elif "open" in command:
                app_name = command.replace("open", "").strip()
                try:
                    if platform.system() == "Windows":
                        try:
                            subprocess.Popen(["notepad.exe"])
                            print(f"Opened {app_name}")
                        except FileNotFoundError:
                            try:
                                subprocess.Popen(["C:\\Windows\\System32\\notepad.exe"])
                                print(f"Opened {app_name}")
                            except FileNotFoundError:
                                print(f"Could not find application: {app_name}")
                    else:
                        subprocess.Popen([app_name])
                    print(f"Opened {app_name}")
                except FileNotFoundError:
                    print(f"Could not find application: {app_name}")
            elif "search google for" in command:
                search_query = command.replace("search google for", "").strip()
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
                print(f"Searching google for {search_query}")
            elif "shutdown computer" in command:
                if platform.system() == "Windows":
                    os.system("shutdown /s /t 1")
                else:
                    os.system("shutdown -h now")
                print("Shutting down computer")
            elif "restart computer" in command:
                if platform.system() == "Windows":
                    os.system("shutdown /r /t 1")
                else:
                    os.system("reboot")
                print("Restarting computer")
            elif "zoom in" in command and not scroll_mode and not volume_mode and not brightness_mode:
                pyautogui.hotkey('ctrl', '+')
            elif "zoom out" in command and not scroll_mode and not volume_mode and not brightness_mode:
                pyautogui.hotkey('ctrl', '-')

        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"Voice recognition error: {e}")

def detect_fingers():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    urls = {1: "https://www.google.com", 2: "https://www.youtube.com",
            3: "https://www.facebook.com", 4: "https://web.whatsapp.com/", }

    cap = cv2.VideoCapture(0)
    last_url_detection = 0
    url_opened = False
    global url_detection_mode, volume_mode, brightness_mode, scroll_mode
    url_detection_mode = True
    volume_mode = False
    brightness_mode = False
    scroll_mode = False

    threading.Thread(target=handle_voice_commands, daemon=True).start()

    with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.6, max_num_hands=1) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    finger_tips = [8, 12, 16, 20]
                    finger_counts = []

                    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
                        finger_counts.append(1)
                    else:
                        finger_counts.append(0)

                    for tip_index in finger_tips:
                        if hand_landmarks.landmark[tip_index].y < hand_landmarks.landmark[tip_index - 2].y:
                            finger_counts.append(1)
                        else:
                            finger_counts.append(0)

                    finger_count = sum(finger_counts)
                    current_time = time.time()

                    if volume_mode:
                        palm_y = hand_landmarks.landmark[0].y
                        if 'previous_palm_y' in detect_fingers.__dict__:
                            delta_y = palm_y - detect_fingers.previous_palm_y
                            if abs(delta_y) > 0.01:
                                if delta_y < 0:
                                    pyautogui.press('volumeup')
                                elif delta_y > 0:
                                    pyautogui.press('volumedown')
                        detect_fingers.previous_palm_y = palm_y
                    elif brightness_mode:
                        palm_y = hand_landmarks.landmark[0].y
                        if 'previous_palm_y' in detect_fingers.__dict__:
                            delta_y = palm_y - detect_fingers.previous_palm_y
                            if abs(delta_y) > 0.01:
                                if delta_y < 0:
                                    sbc.set_brightness('+5')
                                elif delta_y > 0:
                                    sbc.set_brightness('-5')
                        detect_fingers.previous_palm_y = palm_y
                    elif scroll_mode:
                        palm_y = hand_landmarks.landmark[0].y
                        if 'previous_palm_y' in detect_fingers.__dict__:
                            delta_y = palm_y - detect_fingers.previous_palm_y
                            if abs(delta_y) > 0.01:
                                if delta_y < 0:
                                    pyautogui.scroll(-20)  # Scroll down
                                elif delta_y > 0:
                                    pyautogui.scroll(20)   # Scroll up
                        detect_fingers.previous_palm_y = palm_y
                    elif url_detection_mode:
                        if finger_count in urls and current_time - last_url_detection > 5:
                            url = urls[finger_count]
                            print(f"Opening URL for {finger_count} fingers: {url}")
                            threading.Thread(target=open_url, args=(url,)).start()
                            last_url_detection = current_time
                            url_opened = True

                    if finger_count == 5 and url_opened:
                        url_detection_mode = True
                        url_opened = False
                        print("URL selection mode enabled")
                        last_url_detection = current_time

                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            cv2.imshow('Hand Tracking', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    set_chrome_path()
    detect_fingers()