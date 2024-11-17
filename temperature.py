import statistics

def display_main_menu():
    print("Enter some numbers separated by commas (eg. 5, 67, 32)")


def get_user_input():
    str_list = input().split(",")
    float_list = [float(x.strip()) for x in str_list]
    return float_list

def calc_average(num_list):
    average = sum(num_list)/len(num_list)
    result = "{:.2f}".format(average)

    print("Average of num_list:", result)
    return 0
    
def find_min_max(num_list):
    maximum = max(num_list)
    minimum = min(num_list)

    min_max_list = [minimum, maximum]
    print("Minimum and Maximum:", min_max_list)
    return 1

def sort_temperature(num_list):
   num_list.sort()    # a = sorted(num_list)
   return num_list

def calc_median_temperature(sorted_list):
      median_temperature = statistics.median(sorted_list)
      print("Median Temperature:", median_temperature)
      return 2



def main():
    print ("Temperature Calculation: ")
    display_main_menu()

    num_list = get_user_input()
    print("The numbers:", num_list)

    calc_average(num_list)
   

    find_min_max(num_list)
   

    sorted_list = sort_temperature(num_list)
    print("Ascending order list:", sorted_list)

    calc_median_temperature(sorted_list)
   

if __name__ == "__main__":
    main()
