# 🎓 SnapClass — AI-Powered Smart Attendance System

<p align="center">
  <img src="https://i.ibb.co/YTYGn5qV/logo.png" alt="SnapClass Logo" width="120"/>
</p>

<h3 align="center">Making Classroom Attendance Faster, Smarter & More Secure with AI</h3>

<p align="center">
  An intelligent attendance management platform powered by Facial Recognition, Voice Biometrics, and QR-Based Enrollment.
</p>

<p align="center">
  <a href="https://snap-class-three.vercel.app/"><strong>🌐 Visit Website</strong></a>
  &nbsp; | &nbsp;
  <a href="https://snapclass-dk.streamlit.app/"><strong>🚀 Launch Application</strong></a>
</p>

---

## 🌐 Live Demo

| Platform | Description | Link |
|---|---|---|
| 🌐 Website | SnapClass Landing Page | [Visit Website](https://snap-class-three.vercel.app/) |
| 🚀 Application | AI-Powered Smart Attendance System | [Launch Application](https://snapclass-dk.streamlit.app/) |

SnapClass is an AI-powered attendance management system designed to simplify classroom attendance. It replaces traditional manual roll calls with intelligent face and voice recognition, allowing teachers to record attendance efficiently while students can manage their enrollment and attendance records.

---

## ✨ Key Features

### 👨‍🏫 Teacher Portal

- **Teacher Authentication:** Secure teacher registration and login.
- **Subject Management:** Create and manage classroom subjects.
- **QR Code Generation:** Generate unique QR codes and shareable enrollment links for each subject.
- **AI Face Attendance:** Upload classroom photographs to detect and recognize multiple registered students.
- **AI Voice Attendance:** Identify students through their unique voice characteristics.
- **Attendance Management:** Maintain and review attendance records.
- **Classroom Management:** Manage enrolled students and subject information.

### 🎓 Student Portal

- **Face Recognition Login:** Authenticate students using facial recognition.
- **Student Registration:** Register student information and biometric data.
- **Voice Enrollment:** Register voice samples for voice-based identification.
- **QR-Based Enrollment:** Join subjects by scanning a QR code or opening a shared link.
- **Personal Dashboard:** View enrolled subjects and attendance information.
- **Subject Management:** Enroll in or leave subjects.

---

## 🧠 AI & Machine Learning Modules

### 📸 1. Facial Recognition Attendance

SnapClass uses computer vision and machine learning to identify students from classroom photographs.

**Workflow:**

1. Teacher uploads a classroom photograph.
2. The system detects faces in the image.
3. Facial features are converted into numerical embeddings.
4. A trained machine learning classifier identifies registered students.
5. Attendance is recorded for recognized students.

**Technologies:**

- Dlib
- Face Recognition Models
- Scikit-learn
- NumPy

### 🎙️ 2. Voice-Based Student Identification

SnapClass uses voice biometrics to identify students based on their individual voice characteristics.

**Workflow:**

1. Students speak during the attendance session.
2. The system processes the recorded audio.
3. Audio features and voice embeddings are extracted.
4. The extracted voice representation is compared with registered voice profiles.
5. The identified student's attendance can be recorded.

**Technologies:**

- Librosa
- Resemblyzer
- PyTorch
- WebRTC VAD

### 📱 3. QR-Based Subject Enrollment

Every subject can have a unique enrollment code and QR code.

**Workflow:**

1. Teacher creates a subject.
2. SnapClass generates a subject code.
3. A QR code and shareable joining link are generated.
4. Students scan the QR code or open the link.
5. Students can proceed through the enrollment flow.

**Technology:** Segno

---

## ⚙️ System Workflow

### Teacher Workflow

```text
Teacher Registration / Login
          |
          v
    Teacher Dashboard
          |
          v
     Create Subject
          |
          v
 Generate QR Code & Join Link
          |
          v
  Manage Enrolled Students
          |
          v
     Take Attendance
        /       \
       v         v
   Face AI    Voice AI
       \         /
        v       v
    Attendance Records
```

### Student Workflow

```text
Student Registration / Login
            |
            v
      Face Recognition
            |
            v
      Student Dashboard
            |
            v
    Join Subject Using
       QR Code / Code
            |
            v
     Biometric Enrollment
            |
            v
    View Attendance Records
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend / UI | Streamlit |
| Database | Supabase (PostgreSQL) |
| Face Recognition | Dlib, Face Recognition Models |
| Machine Learning | Scikit-learn |
| Voice Recognition | Resemblyzer |
| Audio Processing | Librosa, WebRTC VAD |
| Deep Learning | PyTorch |
| Image Processing | Pillow |
| Data Processing | NumPy, Pandas |
| QR Code Generation | Segno |
| Authentication Security | bcrypt |
| Version Control | Git & GitHub |
| Landing Page Deployment | Vercel |
| Application Deployment | Streamlit Community Cloud |

---

## 📂 Project Structure

```text
SnapClass/
│
├── app.py
├── requirements.txt
├── attendance_queries.sql
│
├── landing_page/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── ...
│
└── src/
    │
    ├── screens/
    │   ├── home_screen.py
    │   ├── teacher_screen.py
    │   └── student_screen.py
    │
    ├── components/
    │   ├── header.py
    │   ├── footer.py
    │   ├── subject_card.py
    │   ├── dialog_auto_enroll.py
    │   └── ...
    │
    ├── database/
    │   ├── config.py
    │   └── ...
    │
    ├── pipelines/
    │   ├── face_pipeline.py
    │   └── ...
    │
    └── ui/
        └── base_layout.py
```

---

## 🚀 Getting Started

Follow these instructions to run SnapClass locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Danish-khan77/SnapClass.git
```

### 2. Navigate to the Project Directory

```bash
cd SnapClass
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Supabase

Create a Supabase project and configure the required database tables.

Add your Supabase credentials to Streamlit secrets.

Create:

`.streamlit/secrets.toml`

```toml
SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_KEY"
```

Use the exact secret names expected by your database configuration.

**Important:** Never commit your actual database credentials or secrets to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 🔐 Security & Data Management

SnapClass is designed with separate teacher and student workflows and uses Supabase for backend data management.

Key considerations:

- Password hashing using bcrypt.
- Role-based application workflows.
- Centralized database management.
- Biometric-based identity verification.
- Secure configuration through Streamlit secrets.

Biometric data should be handled responsibly, with appropriate user consent and access controls.

---

## 🎯 Project Objectives

- Reduce the time spent on manual classroom attendance.
- Minimize proxy attendance through biometric identification.
- Automate student identification using AI.
- Simplify subject enrollment through QR codes.
- Provide a centralized platform for teachers and students.
- Make attendance management more efficient and accessible.

---

## 🔮 Future Enhancements

- Real-time camera-based attendance.
- Advanced liveness detection.
- Improved biometric verification and anti-spoofing.
- Detailed attendance analytics and visualization.
- Automated attendance notifications.
- Enhanced reporting and downloadable attendance summaries.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork this repository.
2. Create a feature branch.

```bash
git checkout -b feature/YourFeature
```

3. Commit your changes.

```bash
git commit -m "Add: YourFeature"
```

4. Push your branch.

```bash
git push origin feature/YourFeature
```

5. Open a Pull Request.

---

## 👨‍💻 Author

**Danish Khan**

B.Tech — Computer Science & Engineering (Blockchain Technology)

- GitHub: [Danish-khan77](https://github.com/Danish-khan77)
- LinkedIn: [Danish Khan](https://linkedin.com/in/danish-khan-cse)

---

## ⭐ Support

If you find SnapClass interesting or useful, consider giving this repository a ⭐ on GitHub.

**SnapClass — Making Attendance Faster Using AI.** 🎓