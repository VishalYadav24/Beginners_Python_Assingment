import csv


def get_max_share_price(csv_filename: str) -> str:
    """ Opens a CSV file and reads it to find the max share price of a company in a particular month of a year.
        
        Arguments:
          csv_filename : str -> path to the CSV file
        Returns:
          message string - showing info of company which had max share price in particular month of specific year  
    """
    with open(csv_filename, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        for row in data:
            a = row["Company A"]
            b = row["Company B"]
            c = row["Company C"]
            max_value = max(a, b, c)
            for key, value in row.items():
                if value == max_value:
                    return(
                        f'max share price for year {row["Year"]} and month {row["Month"]} is of company {key} which is: {max(a, b, c)}'
                        
                    )


if __name__ == "__main__":
    print(get_max_share_price("Beginners/CSV parsing/company_share_data.csv"))
