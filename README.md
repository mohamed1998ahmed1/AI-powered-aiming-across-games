# AI-Powered Aiming Across Games (APAG)

**APAG** is an open-source performance analysis and input control engine for FPS games, leveraging Computer Vision and state-of-the-art Deep Learning models.

### 🎯 Purpose

The goal of this project is to explore the intersection of **Computer Vision** and **Human-Computer Interaction** in gaming. It focuses on analyzing aim metrics, response times, and developing mathematically precise sensitivity curves to help players study and improve their muscle memory.

### 🛠 Tech Stack

* **Python** - Core language.
* **OpenCV** - Real-time image processing.
* **Ultralytics YOLOv8** - Target detection and Pose Estimation.
* **MSS** - High-speed screen capturing.
* **Windows API** - Low-level input manipulation.

### 📊 Features & Roadmap

* [x] **Real-time Detection:** Using YOLOv8-pose for precise keypoint tracking.
* [x] **Coordinate Calculation:** Accurate distance mapping ($dx, dy$) for input systems.
* [ ] **Smoothing:** Implementing advanced interpolation (Lerp) to mimic human-like movement.
* [ ] **Telemetry System:** Storing performance metrics (accuracy, reaction time) in JSON/CSV for post-game analysis.
* [ ] **GUI Dashboard:** A visual interface to track progress and statistics.

### 🤝 How to Contribute

We welcome contributions from developers and researchers! You can help by:

1. **Performance Optimization:** Improving frame processing speeds and reducing latency.
2. **Mathematical Curves:** Designing smoother sensitivity algorithms.
3. **Data Analysis:** Building a dashboard to visualize player performance.

---

### ⚠️ Disclaimer

*This project is intended **strictly for educational and research purposes**. It was developed to explore the applications of Computer Vision in gaming environments. We do not encourage or endorse the use of this code in protected online games. Please adhere to the terms of service of any game you play.*

### 📄 License

This project is licensed under the **MIT License**.

---

### 💡 Quick Tip for your GitHub Repository:

قبل أن ترفع الكود، تأكد من إنشاء ملف باسم **`.gitignore`** وأضف فيه السطور التالية لمنع رفع الملفات الكبيرة أو ملفات البيئة:

```text
venv/
__pycache__/
*.pt
*.log
.env

```

**هل تود أن أقوم بتقسيم الكود الخاص بك إلى "ملفات" منظمة (Modularization) قبل أن ترفعه على GitHub ليكون أسهل في القراءة والمساهمة؟** هذا سيعطي انطباعاً بأن المشروع تم التخطيط له باحترافية.
