# 🗳️ Online Voting System

An end-to-end, secure online voting platform built using **Python Flask**, **HTML/CSS**, and **SQLite**. This web app enables voters to log in and vote, while administrators can manage candidates and track real-time results.

---

## 📦 Features

- 🔐 Admin login with password
- 🙋‍♂️ Voter verification using unique Voter ID
- 🗳️ Vote submission with one vote per user enforcement
- 📊 Real-time vote tally for all candidates
- ➕ Admins can add/delete candidates
- 🔄 Reset all votes for fresh polling
- 🌐 Beautiful responsive frontend using custom CSS
- ☁️ Deploy-ready configuration with Render

---

## 🗂️ Project Structure
                    ┌────────────┐
                    │  Homepage  │
                    └────┬───────┘
                         │
              ┌──────────┴───────────┐
              │                      │
        ┌─────▼─────┐          ┌─────▼──────┐
        │ Voter Flow │          │ Admin Flow │
        └─────┬─────┘          └─────┬──────┘
              │                      │
      ┌───────▼──────────┐    ┌──────▼──────────┐
      │ Voter Login Page │    │ Admin Login Page│
      └───────┬──────────┘    └──────┬──────────┘
              │                      │
   ┌──────────▼───────────┐   ┌──────▼────────────┐
   │ Candidate Selection  │   │ Admin Dashboard   │
   └──────────┬───────────┘   └──────┬────────────┘
              │                      │
    ┌─────────▼─────────┐   ┌────────▼──────────┐
    │ Submit Vote Route │   │ Add/Delete/Reset  │
    └───────────────────┘   └───────────────────┘
---

## 🛠️ Technologies Used

| Component   | Usage                        |
|------------|-------------------------------|
| Flask       | Backend framework             |
| SQLite      | Local database                |
| HTML/CSS    | Frontend design               |
| Jinja2      | Flask templating              |
| Render.com  | Cloud deployment platform     |

---


---

## ⚙️ Tech Stack

| Layer       | Tool         |
|-------------|--------------|
| Backend     | Flask (Python) |
| Frontend    | HTML5 + CSS3  |
| Templating  | Jinja2        |
| Database    | SQLite3       |
| Hosting     | Render.com    |

---

## 🗃️ Database Schema

### `voters`

| Column   | Type | Description           |
|----------|------|-----------------------|
| id       | TEXT | Unique Voter ID       |
| name     | TEXT | Voter’s full name     |
| voted    | INT  | Whether voted (0 or 1)|

### `candidates`

| Column   | Type | Description         |
|----------|------|---------------------|
| id       | INT  | Candidate ID        |
| name     | TEXT | Candidate Name      |
| votes    | INT  | Number of votes     |

---

## 🌐 Routes Overview

| Route                    | Method | Description                             |
|--------------------------|--------|-----------------------------------------|
| `/`                      | GET    | Homepage with navigation buttons        |
| `/vote`                  | GET/POST | Voter Login page & logic                |
| `/candidates`            | GET    | Displays candidate list to vote         |
| `/submit_vote`           | POST   | Handles vote submission                 |
| `/admin`                 | GET/POST | Admin Login                             |
| `/admin_panel`           | GET    | Admin dashboard with current results    |
| `/add_candidate`         | POST   | Add new candidate                       |
| `/delete_candidate/<id>`| GET    | Delete a candidate                      |
| `/reset_votes`           | GET    | Reset all votes                         |

---

## 📁 Folder Structure


---

## ⚙️ Tech Stack

| Layer       | Tool         |
|-------------|--------------|
| Backend     | Flask (Python) |
| Frontend    | HTML5 + CSS3  |
| Templating  | Jinja2        |
| Database    | SQLite3       |
| Hosting     | Render.com    |

---

## 🗃️ Database Schema

### `voters`

| Column   | Type | Description           |
|----------|------|-----------------------|
| id       | TEXT | Unique Voter ID       |
| name     | TEXT | Voter’s full name     |
| voted    | INT  | Whether voted (0 or 1)|

### `candidates`

| Column   | Type | Description         |
|----------|------|---------------------|
| id       | INT  | Candidate ID        |
| name     | TEXT | Candidate Name      |
| votes    | INT  | Number of votes     |

---

## 🌐 Routes Overview

| Route                    | Method | Description                             |
|--------------------------|--------|-----------------------------------------|
| `/`                      | GET    | Homepage with navigation buttons        |
| `/vote`                  | GET/POST | Voter Login page & logic                |
| `/candidates`            | GET    | Displays candidate list to vote         |
| `/submit_vote`           | POST   | Handles vote submission                 |
| `/admin`                 | GET/POST | Admin Login                             |
| `/admin_panel`           | GET    | Admin dashboard with current results    |
| `/add_candidate`         | POST   | Add new candidate                       |
| `/delete_candidate/<id>`| GET    | Delete a candidate                      |
| `/reset_votes`           | GET    | Reset all votes                         |

---

## 📁 Folder Structure


online-voting-system/ │ ├── app.py ├── requirements.txt ├── render.yaml ├── static/ │   └── css/ │       └── style.css ├── templates/ │   ├── index.html │   ├── admin_login.html │   ├── admin_panel.html │   ├── voter_login.html │   ├── vote.html │   └── candidates.html └── README.md

---

## 🧪 How to Run Locally

```bash
# 1. Install Flask
pip install flask

# 2. Run the application
python app.py

