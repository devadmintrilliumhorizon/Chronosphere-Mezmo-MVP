import logging
import time
import random
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Set up logging
log_file = "logs/app.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

messages = [
    "user_signup_success user_id=1234 region=us-east",
    "user_login_failed user_id=5678 region=eu-west reason=invalid_password",
    "transaction_processed tx_id=7890 amount=42.50 status=success",
    "error_processing_payment user_id=4321 error_code=402",
    "health_check passed status=200",
]

print("Log generator started. Writing logs to logs/app.log...")

while True:
    message = random.choice(messages)
    level = logging.INFO if "error" not in message else logging.ERROR
    logging.log(level, message)
    time.sleep(2)
