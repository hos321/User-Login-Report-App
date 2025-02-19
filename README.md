Below is a **sample `README.md`** that you can include in your GitHub repository for the **User Login Report App** (or similarly named project). It provides an end-to-end guide for installing, configuring, and using your custom ERPNext app, along with references to official ERPNext and Frappe documentation.

---

# **User Login Report App**

This custom ERPNext app generates and emails a daily CSV report of user login attempts (first name, last name, and login attempts). It leverages ERPNext’s scheduler to send the report automatically once per day.

---

## **Table of Contents**
1. [Overview](#overview)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
4. [Configuration](#configuration)  
5. [Usage](#usage)  
6. [Troubleshooting](#troubleshooting)  
7. [License](#license)  
8. [References](#references)

---

## **Overview**
- **Goal**: Collect user login data (first name, last name, login attempts) from the ERPNext User doctype.
- **Method**: A Python function (`send_login_report`) fetches the user data, generates a CSV, and emails it to a predefined address.
- **Automation**: Scheduled to run **daily** using ERPNext’s built-in scheduler events.

---

## **Prerequisites**

- **ERPNext Version**: v14+  
- **Frappe Framework**: v14+  
- **Python**: 3.9+  
- **Bench CLI**: Installed and functional  
- A working ERPNext site (local or on a server)

> **Note**: This app has been tested with ERPNext v14. If you use a different version, some settings may vary.

---

## **Installation**

1. **Get the App**  
   ```bash
   bench get-app user_login_report https://github.com/<your-username>/user_login_report.git
   ```
   Replace `<your-username>` with your GitHub handle (and adjust the repo name if necessary).

2. **Install the App on Your Site**  
   ```bash
   bench --site <your-site-name> install-app user_login_report
   ```
   For example, if your site is named `erp.mysite.local`, then:
   ```bash
   bench --site erp.mysite.local install-app user_login_report
   ```

3. **(Optional) Migrate**  
   It’s often good practice to run a migration to ensure all database schema changes apply:
   ```bash
   bench --site <your-site-name> migrate
   ```

---

## **Configuration**

1. **Enable Outgoing Email**  
   - Go to **Settings > Email Account** in your ERPNext desk.  
   - Create (or edit) an email account with correct SMTP settings.  
     - **Enable Outgoing** = checked  
     - **Default Outgoing** = checked (so ERPNext knows which account to use by default)  
   - If using Gmail with 2FA, generate an [App Password](https://support.google.com/accounts/answer/185833) and use that instead of your normal password.

2. **Enable the Scheduler**  
   ```bash
   bench enable-scheduler
   ```
   This ensures Frappe/ERPNext scheduled tasks will run.

3. **Check `hooks.py` for Scheduling**  
   In the app’s `hooks.py`, you should have something like:
   ```python
   scheduler_events = {
     "daily": [
       "user_login_report.tasks.send_login_report"
     ]
   }
   ```
   This tells ERPNext to run `send_login_report` once every day.

---

## **Usage**

1. **Daily Automation**  
   - By default, the scheduler will automatically call `send_login_report` once per day. The time is typically set in your site’s [Scheduler settings](https://frappeframework.com/docs/v14/user/en/python-api/hooks#scheduler_events).  

2. **Manual Trigger**  
   You can also **manually call** the function via REST API:
   ```plaintext
   GET /api/method/user_login_report.tasks.send_login_report
   ```
   Replace `/api/` with your actual site domain (e.g., `https://erp.mysite.local/api/method/...`).

3. **Check Email Queue**  
   - In ERPNext, go to **Settings > Email Queue** to see if the email was queued or sent successfully.  
   - If there’s an error, check **Error Log** or your system’s log files (`bench logs`).

---

## **Troubleshooting**

- **“Please setup default Email Account” Error**  
  - Ensure you have a **Default Outgoing** email account configured.  
  - See official docs: [ERPNext Email Account Setup](https://docs.erpnext.com/docs/v14/user/manual/en/setting-up/email/email-account).

- **SMTPAuthenticationError (Gmail)**  
  - If using Gmail with 2FA, set up an [App Password](https://support.google.com/accounts/answer/185833).  
  - Verify the SMTP server is `smtp.gmail.com` with port `587` and TLS enabled.

- **Scheduler Not Running**  
  - Make sure you have run `bench enable-scheduler`.  
  - Check logs: `bench doctor` and `bench scheduler enable`.  
  - Verify no outstanding errors in **Error Logs**.

---

## **License**

[MIT License](LICENSE) – Or use whichever license suits your project.

---

## **References**

1. **ERPNext Documentation**  
   [https://docs.erpnext.com/](https://docs.erpnext.com/)  
2. **Frappe Framework (Scheduler Events)**  
   [https://frappeframework.com/docs/v14/user/en/python-api/hooks#scheduler_events](https://frappeframework.com/docs/v14/user/en/python-api/hooks#scheduler_events)  
3. **App Passwords (Google)**  
   [https://support.google.com/accounts/answer/185833](https://support.google.com/accounts/answer/185833)  
4. **Frappe App Development**  
   [https://frappeframework.com/docs/v14/user/en/basics/app-development](https://frappeframework.com/docs/v14/user/en/basics/app-development)

---

### **Contact**
For questions or suggestions, feel free to open an issue on this GitHub repository or reach out to the maintainer at `<your-email@domain.com>`.

---

**Enjoy your automated Daily Login Report!**
