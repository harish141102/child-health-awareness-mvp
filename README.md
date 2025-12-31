# 🧒 Child Health Early Awareness System

### Microsoft Imagine Cup 2025 Submission

---

## 👥 Team Information
**Team Name:** Democratizers  
**Project Title:** Child Health Early Awareness System  

---

## 🌍 Problem Statement (Imagine Cup: Impact)
Many child health issues go unnoticed in early stages due to:
- Limited access to healthcare professionals
- Delayed medical checkups
- Lack of early awareness tools for parents and caregivers  

This delay can lead to worsening conditions that could have been addressed earlier with timely attention.

---

## 💡 Solution Overview (Imagine Cup: Innovation)
The **Child Health Early Awareness System** is an AI-powered web application that provides **early awareness insights** by analyzing uploaded child images.

⚠️ **Important:**  
This system does **NOT** provide medical diagnosis.  
It is designed to:
- Demonstrate **technical feasibility**
- Promote **early awareness**
- Encourage seeking professional medical advice

---

## 🚀 How the Solution Works
1. User uploads an image through a clean healthcare-themed interface  
2. Image is securely sent to a Flask backend  
3. Backend processes the image using **Azure AI Vision**  
4. Visual features and tags are extracted  
5. A simple, explainable **risk awareness level** is returned to the user  

---

## 🧠 Use of AI & Microsoft Azure (Imagine Cup: Technical Depth)

### Azure Services Used
- **Azure AI Vision (Image Analysis)**
- Azure SDK for Python

### Why Azure AI Vision?
- Reliable cloud-based image analysis
- Scalable and production-ready
- Aligns with Responsible AI principles
- Part of the Microsoft AI ecosystem

The AI is used strictly for **feature extraction and awareness**, not diagnosis.

---

## 🏗️ System Architecture
Frontend (HTML / CSS / JavaScript)
↓
Flask Backend API
↓
Azure AI Vision
↓
Extracted Image Tags
↓
Early Health Awareness Result

yaml
Copy code

---

## 🛠️ Technology Stack

### Frontend
- HTML
- CSS (Healthcare-themed UI)
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS

### Cloud & AI
- Azure AI Vision

### Tools
- Git
- GitHub

---

## ⚙️ How to Run the Project Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/child-health-awareness-mvp.git
cd child-health-awareness-mvp

2️⃣ Backend Setup
bash
Copy code
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Set Azure Credentials
bash
Copy code
setx AZURE_VISION_ENDPOINT "your_azure_endpoint"
setx AZURE_VISION_KEY "your_azure_key"
Run Backend
bash
Copy code
cd backend
python app.py
Backend runs on:

cpp
Copy code
http://127.0.0.1:5000

3️⃣ Frontend Setup
bash
Copy code
cd frontend
python -m http.server 5500
Open in browser:

arduino
Copy code
http://127.0.0.1:5500/index.html

🧪 Demo Flow (Imagine Cup: Usability)
Open Landing Page

Click Get Started

Upload an image

Submit for analysis

View early awareness result

⚠️ Responsible AI & Ethics (Imagine Cup: Responsibility)
No real medical diagnosis is provided

No claims of clinical accuracy

No real patient data is used

Results are clearly marked as early awareness only

Disclaimer
This system is intended solely for educational and early awareness purposes and does not replace professional medical consultation.

🌱 Future Scope (Imagine Cup: Scalability)
Training on ethically sourced, clinically validated datasets

Collaboration with healthcare professionals and NGOs

Improved risk classification models

Mobile application support

Multilingual accessibility

Deployment with regulatory compliance

🏆 Imagine Cup Alignment Summary
Imagine Cup Criteria	How This Project Meets It
Impact	                Addresses child health awareness
Innovation	            AI-powered early awareness system
Technical               Depth	Azure AI Vision + Flask backend
Responsibility	        Ethical AI, no diagnosis claims
Feasibility	            Fully working end-to-end MVP

📌 Final Note
This project demonstrates how Microsoft Azure AI services can be responsibly used to create scalable, ethical, and impactful solutions for real-world challenges.

Built with responsibility. Designed for impact. Powered by Azure.