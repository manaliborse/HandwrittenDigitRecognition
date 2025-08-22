
# MNIST Digit Detection Web App

This is a small web application that uses **TensorFlow Lite**, **AutoKeras**, and **OpenCV** to detect handwritten digits.  
You can either **upload an image** or use your **webcam** to recognize digits in real-time.  

---

## 📂 Project Structure
static/
├── uploads/ # Stores uploaded images
├── results/ # Stores processed results
templates/
└── index.html # Frontend HTML file
app.py # Main Flask app
mnist.tflite # Pre-trained TensorFlow Lite model
mnist_tflite_trainer.py # Script to train the model
mnist_tflite_model_test.py # Test the TFLite model
mnist_tflite_detection.py # Detect digits from a still image
mnist_tflite_live_detection.py # Detect digits using webcam
LICENSE
README.md

---

## 🚀 Features
- Upload an image of handwritten digits and get predictions.
- Use your webcam to recognize handwritten digits in real-time.
- Uses a **28x28 pixel MNIST-trained CNN model**.
- Lightweight **TensorFlow Lite model** for fast performance.

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   
2. Install the required dependencies:
pip install -r requirements.txt

(If you don’t have a requirements.txt, install manually: flask tensorflow opencv-python autokeras)

3. Run the app:
python app.py
   
4.Open your browser and go to:
http://127.0.0.1:5000

5. Usage
Upload Image → Upload a handwritten digit image (preferably clear and centered).
Webcam → Start the webcam and show digits to get real-time predictions.
