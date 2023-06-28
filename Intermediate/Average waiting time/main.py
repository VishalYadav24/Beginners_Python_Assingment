import argparse


def calculate_least_waiting_time(order_count, order_details):
    temp = []
    current_time = 0
    total_waiting_time = 0
    if len(order_details) != 2 * int(order_count):
        raise ValueError("Please provide input equal to order_count")
    else:
        converted_list = [
            (int(order_details[i]), int(order_details[i + 1]))
            for i in range(0, len(order_details), 2)
        ]
        # sort the list by customer arrival time
        converted_list.sort(key=lambda x: x[0])
        print(converted_list)
        for i in range(0, len(converted_list) - 1):
            current_arrival_time = converted_list[i][0]
            next_arrival_time = converted_list[i + 1][0]
            current_cooking_time = converted_list[i][1]
            next_cooking_time = converted_list[i + 1][1]
            print(
                "ho",
                current_arrival_time,
                current_cooking_time,
                next_arrival_time,
                next_cooking_time,
            )
            if (current_time - current_arrival_time + current_cooking_time) < (
                current_time - next_arrival_time + next_cooking_time
            ):
                pass
            else:
                temp = converted_list[i]
                converted_list[i] = converted_list[i+1]
                converted_list[i+1] = temp

        print("hpoo", converted_list)
        for arrival_time, cooking_time in converted_list:
            if current_time > arrival_time:
                total_waiting_time += current_time - arrival_time + cooking_time
                print("1", current_time, arrival_time, total_waiting_time)
            else:
                current_time = arrival_time
                total_waiting_time += current_time - arrival_time + cooking_time
                print("2", current_time, arrival_time, total_waiting_time)
            current_time += cooking_time
            print("3", current_time, arrival_time, total_waiting_time)
        print(current_time, total_waiting_time // len(converted_list))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Give out least average waiting time	")
    parser.add_argument(
        "no_of_orders",
        metavar="no_of_orders",
        type=str,
        help="enter a integer denoting the number of orders",
    )
    parser.add_argument(
        "customer_arrival_time_and_pizza_making_time",
        metavar="customer_arrival_time_and_pizza_making_time",
        type=str,
        help="enter a integers separated by spaces denoting the customer arrival time and pizza making time",
        nargs="+",
    )
    order_count: str = parser.parse_args().no_of_orders
    order_details: str = parser.parse_args().customer_arrival_time_and_pizza_making_time
    calculate_least_waiting_time(order_count, order_details)
