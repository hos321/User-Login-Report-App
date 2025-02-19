
import frappe
import csv, io

@frappe.whitelist()
def send_login_report():
    # 1. Fetch user data
    users = frappe.get_all("User", filters={"enabled": 1}, fields=["first_name", "last_name", "login_before"])

    # 2. Generate CSV in-memory
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["First Name", "Last Name", "Login Attempts"])
    for user in users:
        writer.writerow([user.first_name, user.last_name, user.login_before])

    # 3. Send Email
    frappe.sendmail(
        recipients=["hoseenheba83@gmail.com"],
        subject="Daily Login Report",
        message="Please find attached the daily login report.",
        attachments=[{
            "fname": "user_login_stats.csv",
            "fcontent": output.getvalue()
        }]
    )
