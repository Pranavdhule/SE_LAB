"""
OTP Verification Program using Gmail SMTP to send OTP emails.
"""
import os
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTPException

def generate_otp():
    """
    Generate a 4-digit random OTP.
    Returns:
        str: A randomly generated 4-digit OTP.
    """
    return str(random.randint(1000, 9999))

def send_email(sender_email, app_password, recipient_email, otp):
    """
    Send an email containing the OTP using Gmail SMTP.

    Args:
        sender_email (str): Sender's email address.
        app_password (str): App password for the sender's email.
        recipient_email (str): Recipient's email address.
        otp (str): The generated OTP to send.
    Raises:
        SMTPException: For any SMTP-related errors.
    """
    smtp_server = "smtp.gmail.com"
    port = 587
    print("Connecting to SMTP server...")
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            print("SMTP connection secured.")

            print("Logging into email account...")
            server.login(sender_email, app_password)
            print("Login successful!")

            # Email content setup
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = "OTP Verification"

            body = f"Your OTP is: {otp}"
            message.attach(MIMEText(body, "plain"))

            # Send the email
            print(f"Sending email to {recipient_email}...")
            server.sendmail(sender_email, recipient_email, message.as_string())
            print("Email sent successfully!")
    except SMTPException as error:
        print(f"Failed to send email: {error}")
        raise

def verify_otp(expected_otp):
    """
    Verify the OTP entered by the user against the expected OTP.
    Args:
        expected_otp (str): The OTP that was sent to the user.
    Returns:
        bool: True if the OTP matches, False otherwise.
    """
    user_input = input("Enter Your OTP >>: ").strip()
    if user_input == expected_otp:
        print("OTP Verified Successfully!")
        return True
    print("Invalid OTP. Please try again.")
    return False

def get_email_credentials():
    """
    Retrieve sender email and app password from environment variables.
    Returns:
        tuple: sender_email and app_password.
    Raises:
        ValueError: If credentials are not set.
    """
    sender_email = "pranavdhule04@gmail.com"
    app_password = "vvve csmg ryrs mmol"

    if not sender_email or not app_password:
        raise ValueError("Email credentials not set in environment variables.")
    return sender_email, app_password

def main():
    """
    Main function to orchestrate the OTP generation, email sending, and verification process.
    """
    try:
        # Load email credentials
        sender_email, app_password = get_email_credentials()
        print("Generating OTP...")
        otp = generate_otp()
        print("OTP generated successfully.")

        # Get recipient email and send the email
        recipient_email = input("Enter the recipient's email: ").strip()
        send_email(sender_email, app_password, recipient_email, otp)

        # Verify OTP
        if verify_otp(otp):
            print("Verification process completed successfully.")
        else:
            print("Verification failed.")
    except ValueError as err:
        print(f"Configuration Error: {err}")
    except Exception as error:  # pylint: disable=broad-except
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
