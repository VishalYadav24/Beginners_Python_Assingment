import argparse
import re
import requests


def check_input(pnr_no: str)-> bool:
    """Check input string for 10 digits
    Arguments: pnr_no (str) : train pnr number input given by user

    Returns:
       True : if input string is valid i.e it has 10 digits
    Raises:
       Exception : if input string is invalid
    """
    regex_pattern = r"^(\d{10})$"
    if re.match(regex_pattern, pnr_no):
        return True
    else:
        raise Exception("Please enter a valid pnr")


def check_pnr_status(pnr_no: str) -> dict:
    """Checks seat confirmation status for given pnr.

    Arguments:pnr_no (str) : train pnr number input given by user

    Returns:
        dict containing info about seat confirmation status, source and destination of travel
    """
    if check_input(pnr_no):
        try:
            url = f"https://pnr-status-indian-railway.p.rapidapi.com/pnr-check/{pnr_no}"
            print(url)

            headers = {
                "X-RapidAPI-Key": "5bffbefba1mshae4ff40591f1f99p141716jsnc19b06fcab09",
                "X-RapidAPI-Host": "pnr-status-indian-railway.p.rapidapi.com",
            }

            response = requests.get(url, headers=headers)
            response_object = response.json()
            if response_object["status"]:
                boarding_info = response_object["data"]["boardingInfo"]
                destination_info = response_object["data"]["destinationInfo"]
                seat_info = response_object["data"]["seatInfo"]

                result = {
                    "success": True,
                    "boarding_at": boarding_info["stationName"],
                    "arrival_at": destination_info["stationName"],
                    "seat_info": seat_info,
                }

                return result

            else:
                return response_object["error"]
        except Exception as e:
            print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Provides seat confirmation status using train PNR status"
    )
    parser.add_argument("pnr", metavar="pnr number", type=str, help="enter your pnr")
    args: str = parser.parse_args().pnr
    print(check_pnr_status(args))
