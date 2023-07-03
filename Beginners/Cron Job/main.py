import requests
import logging
import schedule
import time
import random

api_url: str = "https://type.fit/api/quotes"

logging.basicConfig(
    level=logging.INFO,
    filename="./Beginners/Cron Job/main.log",
    filemode="w",
    format="%(asctime)s %(levelname)s :  %(message)s",
)


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
        logging.warning(e)

schedule.every(2).seconds.do(display_wise_thoughts)
if __name__ == "__main__":
    counter:int = 0
    while True:
        schedule.run_pending()
        time.sleep(1)
        counter += 1
        print(counter)
        if counter == 10:
            break
