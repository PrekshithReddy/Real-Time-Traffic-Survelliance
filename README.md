# 🚗 Real-Time Traffic Surveillance and Detection

A high-performance web application designed for real-time traffic monitoring, vehicle detection, and safety compliance (like helmet detection) using cutting-edge Deep Learning and AI.

---

## 🌟 Key Features

*   **Vehicle Tracking & Counting**: Uses YOLO to detect and count vehicles in real-time.
*   **Helmet/Safety Compliance**: Automated detection of helmets on two-wheelers for traffic safety.
*   **Performance Metrics**: Integrated analysis toolkit providing Accuracy, Precision, and Recall scores for AI models.
*   **User Management**: Secure authentication system for authorized traffic personnel.
*   **Video Processing**: Support for live processing of uploaded traffic footage.

---

## 🛠️ Built With

*   **Frontend**: HTML, CSS, JavaScript (Django Templates)
*   **Backend**: Python, Django Framework
*   **AI/ML**: YOLO v7, Keras, TensorFlow, NumPy, Scikit-Learn
*   **Database**: MySQL (Secured via `.env`)
*   **Vision**: OpenCV, Pymysql

---

## 🚀 Setup and Installation

Follow these steps to get your own instance running:

### 1. Clone the Portfolio
```bash
git clone https://github.com/PrekshithReddy/Real-Time-Traffic-Survelliance.git
cd Real-Time-Traffic-Survelliance
```

### 2. Configure Environment Variables
Copy the example file to your own `.env` and enter your database credentials:
```bash
# On Windows
copy .env.example .env
```
Now, open `.env` and fill in your **DB_NAME**, **DB_USER**, and **DB_PASSWORD**.

### 3. Model Weights (Crucial Step)
Due to size limits, we do not store the AI model weights on GitHub. 
👉 **Download the weights here: [INSERT YOUR GOOGLE DRIVE LINK HERE]**

Place the following files in the `/models` directory:
- `yolov7.weights`
- `yolov7.hdf5`
- `yolov7.cfg`

### 4. Install Dependencies
Make sure you have Python 3 installed, then run:
```bash
pip install -r requirements.txt
```

### 5. Setup Database
Run the SQL queries found in `DB.txt` on your MySQL server to initialize the tables.

---

## 🏃 Running the Application

Start the Django server:
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` in your browser to see the dashboard!

---

## 🛡️ Security Note
This project utilizes environment-based security. Real credentials and local database secrets are permanently ignored via `.gitignore` to prevent data leakage.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/PrekshithReddy/Real-Time-Traffic-Survelliance/issues).