import csv


def get_max_share_price(csv_filename):
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
                    print(
                        f'max share price for year {row["Year"]} and month {row["Month"]} is of company {key} which is ',
                        max(a, b, c),
                    )


if __name__ == "__main__":
    get_max_share_price("Beginners/CSV parsing/company_share_data.csv")
