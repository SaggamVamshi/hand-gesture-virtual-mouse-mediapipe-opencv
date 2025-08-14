# Hand Gesture Virtual Mouse (MediaPipe + OpenCV)

A computer vision–based **virtual mouse** that uses **hand gestures** for controlling the cursor and performing click actions.
Built with **MediaPipe**, **OpenCV**, and **PyAutoGUI**, this project enables **AI-powered Human–Computer Interaction** without any physical mouse.

## ✨ Features

* **Real-time hand tracking** using MediaPipe
* **Cursor control** with index finger movements
* **Click detection** via thumb–index pinch gesture
* Works with any standard webcam
* Lightweight and platform-independent

## 🛠️ Tech Stack

* **Python**
* **OpenCV** – image processing & webcam feed
* **MediaPipe** – hand landmark detection
* **PyAutoGUI** – mouse control

## 🚀 How It Works

1. Captures webcam video and detects **21 hand landmarks**.
2. Maps the **index finger tip** to the screen coordinates for cursor movement.
3. Measures distance between **thumb tip** and **index tip**.
4. If the distance is below a threshold → triggers a **mouse click**.

## 📷 Demo

*(Add a screenshot or GIF here of your project in action)*

## 📦 Installation

```bash
git clone https://github.com/yourusername/hand-gesture-virtual-mouse.git
cd hand-gesture-virtual-mouse
pip install -r requirements.txt
python virtual_mouse.py
```

## 📜 License

This project is open source under the [MIT License](LICENSE).

---
