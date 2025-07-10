# 📚 Study Share — Local File Sharing Web Server (LAN-Based)

A simple, secure, and beautiful local file-sharing web server** built using Python Flask for offline file exchange within hostel rooms, classrooms, or small groups over LAN/Wi-Fi—no internet required!

---

## 🚀 Features

* ✅ Upload & download any file within the same Wi-Fi network (LAN)
* ✅ Simple, study-themed aesthetic (Navy Blue + White)
* ✅ Password-protected access for security
* ✅ Runs on Ubuntu/Linux using minimal resources
* ✅ 100% works offline (no need for Internet)

---

## 🎯 Use Case Scenarios

* Share PDFs, notes, project files in hostel or campus
* Transfer files between phone ↔️ laptop without internet
* Quick, secure sharing without using third-party apps

---

## 🛠 Tech Stack

| Technology     | Usage                            |
| -------------- | -------------------------------- |
| Python 3       | Backend scripting                |
| Flask          | Lightweight web server framework |
| HTML & CSS     | Frontend UI (study theme)        |
| Linux (Ubuntu) | Hosting environment              |

---

## 📂 Folder Structure

```
FileShareProject/
│
├── uploads/               # Folder where uploaded files are stored
├── file_share_server.py   # Main Python app
└── README.md              # This file
```

---

## ⚙️ How to Run (Beginner Friendly)

### 1️⃣ Prerequisites

* ✅ Python 3 installed
* ✅ Flask installed (`pip3 install flask`)

### 2️⃣ Set Up

```bash
# Create project folder
mkdir ~/FileShareProject
cd ~/FileShareProject

# Save the Python script as file_share_server.py

# Run the server
python3 file_share_server.py
```

### 3️⃣ Access the Web App

1. Find your Ubuntu IP:

   ```bash
   hostname -I
   ```
2. Open browser on any device connected to same Wi-Fi:

   ```
   http://<Your-IP>:8000
   ```
3. Login using:

   * Username: guest
   * Password: hostel123
4. Upload or download files easily.

---

## 🔐 Security

* Built-in username/password (stored securely in code).
* Add custom credentials by editing these variables in file_share_server.py:

python
USERNAME = 'your_username'
PASSWORD = 'your_password'


---

## 🌟 Future Improvements (Ideas)

| Feature                    | Description                                 |
| -------------------------- | ------------------------------------------- |
| 🎨 Dark/Light Theme switch | Allow users to change themes                |
| 📟 QR Code Generator       | For quick mobile access                     |
| 🗑️ Auto-delete old files  | Save storage by deleting files after X days |
| 📦 Bulk Downloads          | Download multiple files as ZIP              |

---

## 📢 Author

👩‍💻 Dhanashri Katkar & Samiksha Chavan
✨ Final Year B.Tech, Computer Engineering
💡 Passionate about tech, creativity & solving real-world problems.

---

## 📝 License

This project is open for **personal and academic use**. Feel free to improve it and share credits.
