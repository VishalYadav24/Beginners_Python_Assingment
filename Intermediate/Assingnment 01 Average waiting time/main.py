import argparse


def calculate_least_waiting_time(order_count: str, order_details: str) -> int:
    """
    Calculates the least average waiting time for a given pizza order to be served to a customer.
    
    Arguments:
       order_count: str -> total number of order to be served i.e length of the order_details list
       order_details: str -> list of order details (customer arrival time, pizza cooking time)

    Returns:
        Least Average Waiting Time (int)    

    """
    print(order_details)
    temp: list = []
    current_time: int = 0
    total_waiting_time: int = 0
    # checking if user has provided order_details upto order_count
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
        # moving the order_details element which has less waiting time first
        for i in range(0, len(converted_list) - 1):
            current_arrival_time = converted_list[i][0]
            next_arrival_time = converted_list[i + 1][0]
            current_cooking_time = converted_list[i][1]
            next_cooking_time = converted_list[i + 1][1]
            print(current_time)
            if ( current_arrival_time + current_cooking_time) < (
                 next_arrival_time + next_cooking_time
            ):
                pass
            else:
                # swapping positions
                temp = converted_list[i]
                converted_list[i] = converted_list[i + 1]
                converted_list[i + 1] = temp

        # computing total waiting time and average waiting time
        print(converted_list)
        for arrival_time, cooking_time in converted_list:
            if current_time > arrival_time:
                total_waiting_time += current_time - arrival_time + cooking_time
            else:
                current_time = arrival_time
                total_waiting_time += current_time - arrival_time + cooking_time
            current_time += cooking_time
        return (total_waiting_time // len(converted_list))


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
    print("Average waiting time is :",calculate_least_waiting_time(order_count, order_details))
