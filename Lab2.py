def display_main_menu():
    print("Enter some numbers seperated by comas ( e.g.5,67,32)")

def get_user_input():
    num_list = []
    str = input()
    str_list = str.split(",")

    for item in str_list:
        num_list.append(int(item))
    return num_list

def calc_average_temperature(num_list):
    sum =0
    count =0
    for item in num_list:
        sum = sum+item
        count=count +1
    average= sum/count
    return average

def calc_min_max_temperature(num_list):
    print("The maximum number is: ",max(num_list))
    print("The minimum number is: ",min(num_list))


def main():
    print ("ET0735 (DevOps for AIoT) - Lab2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print("The average is ", calc_average_temperature(num_list))
    calc_min_max_temperature(num_list)

if __name__=='__main__':
 main()

