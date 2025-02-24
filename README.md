# Emotion Detection Flask App

## Overview
This project is a **Flask-based web application** that uses **IBM Watson's NLP API** to analyze emotions in text. Users can submit a text input, and the system returns emotion scores for **anger, disgust, fear, joy, and sadness**, along with the **dominant emotion** detected.

---

## Features
- **Web-based API** with Flask.
- **Detects emotions** in text using IBM Watson NLP.
- **Returns structured JSON or formatted text responses**.
- **Handles errors gracefully** (e.g., missing input, API failures).
- **Deployable on cloud platforms** like **Heroku, AWS, or Render**.

---

## 📂 Project Structure
```
final_project/
│── Emotion_Analysis/                  # Main application directory
│── EmotionDetection/
│   ├── emotion_detection.py           # Emotion analysis logic using Watson API
│── static/                             # Static assets (CSS, JS, images)
│── templates/                          # HTML templates for the web UI
│   ├── index.html                      # Homepage template
│── test_emotion_detection.py           # Unit tests for emotion analysis
│── server.py                           # Flask app entry point
│── README.md                           # Documentation (this file)
│── LICENSE                             # License information
│── .gitignore                          # Ignore unnecessary files
```

---

## Installation & Setup
### Clone the Repository

### Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### Install Dependencies
```sh
pip install -request , json
```

### Run the Flask App
```sh
python server.py
```

### Test the API
- Open in browser:  
  ```
  http://127.0.0.1:5000/
  ```
- Analyze emotions via API:  
  ```
  http://127.0.0.1:5000/emotionDetector?textToAnalyze=I am so happy today!
  ```

---

## Running Unit Tests
To test the **emotion detection logic**, run:
```sh
python -m unittest test_emotion_detection.py
```

---

## API Endpoints
### Home Page
- **`GET /`** → Renders the home page (`index.html`).

### Emotion Analysis
- **`GET /emotionDetector?textToAnalyze=<your-text>`**
- Example:
  ```
  http://127.0.0.1:5000/emotionDetector?textToAnalyze=I love programming!
  ```
- **Response (Formatted Text Example)**:
  ```
  For the given statement, the system response is 'anger': 0.006, 'disgust': 0.002, 'fear': 0.009, 'joy': 0.968, and 'sadness': 0.049.
  The dominant emotion is joy.
  ```
- **Response (JSON Example)**:
  ```json
  {
      "anger": 0.006274985,
      "disgust": 0.0025598293,
      "fear": 0.009251528,
      "joy": 0.9680386,
      "sadness": 0.049744144,
      "dominant_emotion": "joy"
  }
  ```

---

## Error Handling
| Error Scenario | Response |
|---------------|----------|
| **No text provided** | `"Invalid text! Please try again!"` |
| **API returns 400 (Bad Request)** | `{ "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None }` |

---


**🚀 Happy Coding!**


