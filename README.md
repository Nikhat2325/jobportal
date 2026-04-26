# 💼 Job Portal Web Application (Django)

A full-featured Job Portal web application built using Django. This platform allows users to search and apply for jobs, while recruiters can post job vacancies and manage applicants.

---

## 🚀 Features

### 👤 User (Student)

* Register and Login
* View available jobs
* Search jobs by title
* Apply for jobs
* View applied jobs (My Applications)
* Delete application

### 🧑‍💼 Recruiter

* Register and Login
* Add job postings
* View posted jobs
* View applicants for each job
* Check applicant details

### 🔐 Admin

* Manage users, jobs, and applications via Django Admin Panel

---

## 🛠️ Technologies Used

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite3
* **Tools:** VS Code, Git, GitHub

---

## 📂 Project Structure

```
jobportal/
│
├── jobs/                # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│
├── jobportal/           # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3
├── manage.py
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/your-username/jobportal.git
```

2. Navigate to project folder:

```
cd jobportal
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run migrations:

```
python manage.py migrate
```

5. Create superuser:

```
python manage.py createsuperuser
```

6. Run server:

```
python manage.py runserver
```

7. Open browser:

```
http://127.0.0.1:8000/
```

---

## 🔑 User Roles

| Role      | Access                      |
| --------- | --------------------------- |
| User      | Apply for jobs              |
| Recruiter | Post jobs & view applicants |
| Admin     | Full control                |

---

## 📸 Screenshots

* User Login Page
* Recruiter Dashboard
* Job Listings
* Applications Page

(Add screenshots here later)

---

## 📌 Future Improvements

* Resume upload feature
* Email notifications
* Job filtering (location, salary, category)
* Payment integration
* Profile management

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📧 Contact

Developed by **NIKHAT PARVEEN**
GitHub: https://github.com/Nikhat2325

