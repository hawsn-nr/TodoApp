# 📝 TodoApp

A simple and clean **Todo List** web application built with **Django**. Users can create, update, complete, and delete tasks through an intuitive interface.

## 🚀 Features

* ✅ Create new tasks
* ✏️ Edit existing tasks
* ✔️ Mark tasks as completed/incomplete
* 🗑️ Delete tasks
* 👤 User authentication (Sign Up & Sign In)
* 🔒 Each user has their own personal todo list
* 🎨 Clean and responsive UI

## 🛠️ Tech Stack

* **Backend:** Django
* **Database:** PostgreSQL (recommended) / SQLite
* **Frontend:** HTML, CSS
* **Authentication:** Django Authentication System

---

## 📂 Project Structure

```text
TodoApp/
│── todo_project/      # Django project settings
│── todoApp/           # Main application
│── templates/         # HTML templates
│── static/            # CSS & Images
│── manage.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/hawsn-nr/TodoApp.git
cd TodoApp
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django psycopg2-binary
```

or

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Configuration

### PostgreSQL

Update `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "Todo",
        "USER": "root",
        "PASSWORD": "YOUR_PASSWORD",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

If you prefer SQLite, simply remove the PostgreSQL configuration.

---

## 🔄 Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ▶️ Run the Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

You can add screenshots here.

```
screenshots/
├── home.png
├── login.png
└── register.png
```

Example:

```markdown
![Home Page](screenshots/home.png)
```

---

## 📌 Future Improvements

* Task categories
* Due dates
* Task priorities
* Search and filtering
* REST API
* Dark mode
* Mobile-friendly improvements

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Hawsn**

GitHub: https://github.com/hawsn-nr
