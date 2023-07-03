import requests
import logging
import schedule
import time
import random
import smtplib

api_url: str = "https://type.fit/api/quotes"

logging.basicConfig(
    level=logging.INFO,
    filename="./Beginners/Cron Job/main.log",
    filemode="w",
    format="%(asctime)s %(levelname)s :  %(message)s",
)


def send_email(message: str):
    """
    Sends an email to the specified person about critical failures in program
    """
    try:
        session = smtplib.SMTP("smtp.gmail.com", 587)
        # tls
        session.starttls()
        # authentication
        session.login("sender_email_id", "sender_email_password")
        # sending mail
        session.sendmail("sender_email_id", "recipients_email", message)
        # quit
        session.quit()
    except Exception as e:
        logging.critical(f"Error sending mail:{e}")


def display_wise_thoughts() -> None:
    """
    Displays Random quotes from various perspectives of the world.
    """
    try:
        response = requests.get(api_url).json()
        random_index = random.randint(0, len(response))

        quote = f'{response[random_index]["text"]}\n by - {response[random_index]["author"]}'
        print(
            f'{response[random_index]["text"]}\n by - {response[random_index]["author"]}'
        )
        logging.info(quote)
    except Exception as e:
        logging.critical(e)
        send_email(e)


schedule.every(2).seconds.do(display_wise_thoughts)
if __name__ == "__main__":
    counter: int = 0
    while True:
        schedule.run_pending()
        time.sleep(1)
        counter += 1
        print(counter)
        if counter == 10:
            break
