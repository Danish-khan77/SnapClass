# 📸 Snapclass – AI-Powered Smart Attendance System

Snapclass is an AI-powered attendance management system that automates classroom attendance using Face Recognition and Voice Recognition. It helps teachers manage subjects, enroll students, analyze classroom photos, and maintain attendance records through an interactive dashboard.

## ✨ Features

- **Face Recognition:** Automatically identifies students from classroom photographs.
- **Voice Attendance:** Supports voice-based attendance.
- **Subject Management:** Create and manage subjects.
- **Student Enrollment:** Enroll students using subject codes.
- **Automated Attendance:** Automatically marks students as Present or Absent.
- **Attendance History:** View and track previous attendance records.
- **Teacher Dashboard:** Manage classroom attendance and subjects in one place.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| AI/ML | Face Recognition, Voice Recognition |
| Computer Vision | OpenCV / Image Processing |
| Database | Supabase (PostgreSQL) |
| Data Processing | NumPy, Pandas |

## 📂 Project Structure

```text
Snapclass/
│
├── src/
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   ├── screens/
│   └── ui/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/Danish-khan77/SnapClass.git
```

**2. Navigate to the project directory**

```bash
cd SnapClass
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Configure Supabase**

Create a Supabase project and configure your project URL and API key in your environment configuration.

Never commit database credentials or API keys to GitHub.

**7. Run the application**

```bash
streamlit run app.py
```

## 🚀 Application Workflow

1. Teacher registers or logs into the platform.
2. Teacher creates a subject.
3. Students enroll using the subject code.
4. Teacher uploads classroom photographs.
5. AI analyzes images and identifies enrolled students.
6. Attendance results are generated automatically.
7. Teachers can review attendance history.

## 🔮 Future Enhancements

- Improved face recognition accuracy.
- Advanced voice recognition.
- Attendance analytics and visualization.
- Enhanced student performance insights.
- Cloud deployment and scalability.

## 👨‍💻 Developer

**Danish Khan**

- GitHub: [@Danish-khan77](https://github.com/Danish-khan77)
- LinkedIn: [Danish Khan](https://linkedin.com/in/danish-khan-cse)

---

⭐ If you find Snapclass interesting, consider giving this repository a star!

**Snapclass – Making Classroom Attendance Smarter with AI.**