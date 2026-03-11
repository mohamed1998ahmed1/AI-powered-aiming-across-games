import cv2
import numpy as np
import mss
import ctypes
from ultralytics import YOLO
from pynput import mouse
import math
import sys
import os

# --- دالة حل مشكلة المسارات في التحويل ---
def get_resource_path(relative_path):
    """ تأخذ المسار وتجعله متوافقاً مع ملف الـ EXE """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# --- SETTINGS ---
CONF_LIMIT = 0.45
AIM_SENSITIVITY = 0.6 
SCAN_WIDTH = 416
is_aiming = False

# تحميل الموديل باستخدام الدالة الجديدة لضمان عدم خروج الملف "فاضي"
model_path = get_resource_path('yolov8n-pose.pt')
model = YOLO(model_path) 
sct = mss.mss()

def on_click(x, y, button, pressed):
    global is_aiming
    if button == mouse.Button.left:
        is_aiming = pressed

# تشغيل مستمع الماوس
listener = mouse.Listener(on_click=on_click)
listener.start()

def move_mouse(x, y):
    ctypes.windll.user32.mouse_event(0x0001, int(x), int(y), 0, 0)

def draw_enhanced_skeleton(frame, keypoints):
    edges = [
        (5, 7), (7, 9), (6, 8), (8, 10), (5, 6),
        (5, 11), (6, 12), (11, 12), (11, 13), (13, 15),
        (12, 14), (14, 16)
    ]
    for start, end in edges:
        p1, p2 = keypoints[start], keypoints[end]
        if p1[2] > 0.5 and p2[2] > 0.5:
            cv2.line(frame, (int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1])), (0, 255, 0), 1)
    
    nose = keypoints[0]
    if nose[2] > 0.5:
        shoulder_mid_x = int((keypoints[5][0] + keypoints[6][0]) / 2)
        shoulder_mid_y = int((keypoints[5][1] + keypoints[6][1]) / 2)
        cv2.line(frame, (int(nose[0]), int(nose[1])), (shoulder_mid_x, shoulder_mid_y), (0, 255, 0), 1)
        cv2.circle(frame, (int(nose[0]), int(nose[1])), 3, (0, 0, 255), -1)

def main_loop():
    screen_w = ctypes.windll.user32.GetSystemMetrics(0)
    screen_h = ctypes.windll.user32.GetSystemMetrics(1)
    
    monitor = {
        "top": (screen_h // 2) - (SCAN_WIDTH // 2), 
        "left": (screen_w // 2) - (SCAN_WIDTH // 2), 
        "width": SCAN_WIDTH, 
        "height": SCAN_WIDTH
    }
    center = SCAN_WIDTH // 2

    while True:
        img = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        results = model.predict(frame, conf=CONF_LIMIT, verbose=False)

        best_target = None
        min_dist = float('inf')

        for r in results:
            if not r.keypoints: continue
            kp = r.keypoints.data[0]
            
            if r.boxes:
                x1, y1, x2, y2 = map(int, r.boxes.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 1)

            draw_enhanced_skeleton(frame, kp)

            if kp[0][2] > 0.5:
                dist = math.sqrt((kp[0][0] - center)**2 + (kp[0][1] - center)**2)
                if dist < min_dist:
                    min_dist = dist
                    best_target = (kp[0][0], kp[0][1])

        if best_target and is_aiming:
            dx = (best_target[0] - center) * AIM_SENSITIVITY
            dy = (best_target[1] - center) * AIM_SENSITIVITY
            move_mouse(dx, dy)

        cv2.imshow("AI Vision System", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main_loop()