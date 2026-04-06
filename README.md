# 💳 Smart Banking System (CLI-Based)

A command-line banking application built with Python that simulates real-world banking operations such as account creation, deposits, withdrawals, transfers, and analytics.

---

## 🚀 Features

### 👤 Account Management

* Create bank accounts with unique account numbers
* Secure PIN authentication system
* Account lock after multiple failed login attempts

---

### 💰 Transactions

* Deposit money
* Withdraw money (with balance validation)
* Transfer money between users
* Prevent self-transfer
* Daily transaction limit enforcement

---

### 🧾 Transaction Tracking

* Full transaction history with timestamps
* Paginated transaction viewing
* Structured transaction types (deposit, withdrawal, transfer)

---

### 🔐 Security Features

* PIN authentication system
* Account lock after 3 failed attempts
* Fraud prevention (no overdrafts, no invalid transfers)

---

### 📊 Analytics Dashboard

* Total money in the bank
* Richest customer
* Oldest account
* Most active account (by transaction count)

---

### 🏆 Ranking System

* Top 3 richest accounts

---

### 📂 Data Persistence

* All data stored in JSON files
* Automatic save after every transaction
* Logging system for tracking system activity

---

## 🧠 Technologies Used

* Python
* JSON (for storage)
* Datetime (for timestamps)
* File handling

---

## 📁 Project Structure

```bash
banking_app/
│
├── main.py        # Application entry point
├── core.py        # Business logic
├── utils.py       # Helper functions
├── storage.py     # File handling & logging
├── config.py      # Configuration variables
├── data.json      # Database (users)
├── logs.txt       # Activity logs
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone <https://github.com/successdevop/CLI_banking_system.git>
```

2. Navigate into the project folder:

```bash
cd CLI_banking_system
```

3. Run the program:

```bash
python main.py
```

---

## 🖥️ Menu Options

```text
1. Create Account
2. Deposit
3. Withdraw
4. Transfer
5. Balance
6. Transaction History
7. Analytics
8. Top 3 Accounts
9. Find User
0. Exit
```

---

## 📌 Sample Data Structure

```json
{
    "id": 1,
    "name": "John Doe",
    "account_number": "1234567890",
    "pin": "1234",
    "balance": 5000,
    "transactions": [],
    "created_at": "2026-04-04T09:00:00",
    "user_locked": false
}
```

---

## 🔥 Future Improvements

* Convert to web app using Flask or Django
* Add database (SQLite/PostgreSQL)
* Implement JWT authentication
* Add email/SMS notifications
* Build REST API endpoints
* Add admin dashboard

---

## 🎯 Learning Outcomes

This project demonstrates:

* Backend system design
* Authentication logic
* State management
* File-based database handling
* Error logging
* Real-world financial logic

---

## 👨‍💻 Author

Built by **[Success.I.R (successdevop)]**

---

## 📄 License

This project is open-source and intended for educational purposes.
