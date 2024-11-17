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
    return result
    
def find_min_max(num_list):
    maximum = max(num_list)
    minimum = min(num_list)

    min_max_list = [minimum, maximum]
    return min_max_list

def sort_temperature(num_list):
   num_list.sort()    # a = sorted(num_list)
   return num_list

def calc_median_temperature(sorted_list):
      median_temperature = statistics.median(sorted_list)
      return median_temperature



def main():
    print ("Temperature Calculation: ")
    display_main_menu()

    num_list = get_user_input()
    print("The numbers:", num_list)

    average = calc_average(num_list)
    print("Average of num_list:", average)

    min_max = find_min_max(num_list)
    print("Minimum and Maximum:", min_max)

    sorted_list = sort_temperature(num_list)
    print("Ascending order list:", sorted_list)

    median_temp = calc_median_temperature(sorted_list)
    print("Median Temperature:", median_temp)

if __name__ == "__main__":
    main()
