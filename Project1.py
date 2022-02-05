"""
This is the main file for Project 1. It includes the class for State
as well as all the functions for the program.

Author: Muhib Sheikh
Version: 1.0 Last Updated: 2/4/2022
Email: n01403705@unf.edu
"""
import csv


class State:
    """
    This class is used to create a State object. It contains the name of the state, the capital, the region,
    the number of us house seats, the population, the covid cases, and the covid deaths, the fully vaccinated rates,
    the median household income, and the violent crime rate. It also contains the covid cases per 100,000 people,
    the covid deaths per 100,000 people, and the covid case fatality rate per 100,000 people.
    """

    def __init__(self, state_name, capitol, region, us_house_seats, population, covid_cases, covid_deaths,
                 full_vax_rates, median_household_income, violent_crime_rate):
        """
        This is the constructor for the State class.
        It takes in all the parameters and sets them to the class variables.
        :param state_name: The name of the state
        :param capitol: The capital of the state
        :param region: The region of the state
        :param us_house_seats: The number of US House seats
        :param population: The population of the state
        :param covid_cases: The number of covid cases in the state
        :param covid_deaths: The number of covid deaths in the state
        :param full_vax_rates: The full vaccination rates of the state
        :param median_household_income: The median household income of the state
        :param violent_crime_rate: The violent crime rate of the state
        :return: None
        """
        self.state_name = state_name
        self.capitol = capitol
        self.region = region
        self.us_house_seats = us_house_seats
        self.population = population
        self.covid_cases = covid_cases
        self.covid_deaths = covid_deaths
        self.full_vax_rates = float(full_vax_rates) / 100
        self.median_household_income = median_household_income
        self.violent_crime_rate = violent_crime_rate
        self.case_rate = (float(self.covid_cases) / float(self.population)) * 100000
        self.death_rate = (float(self.covid_deaths) / float(self.population)) * 100000
        self.case_fatality_rate = float(self.death_rate) / float(self.case_rate)

    def get_state_name(self):
        """
        This is the getter method for the state name.
        :return: the state name
        """
        return self.state_name

    def set_state_name(self, x):
        """
        This is the setter method for the state name.
        :param x: value to set the state name to
        """
        self.state_name = x

    def get_capitol(self):
        """
        This is the getter method for the capital.
        :return: the capital
        """
        return self.capitol

    def set_capitol(self, x):
        """
        This is the setter method for the capital.
        :param x: value to set the capital to
        """
        self.capitol = x

    def get_region(self):
        """
        This is the getter method for the region.
        :return: the region
        """
        return self.region

    def set_region(self, x):
        """
        This is the setter method for the region.
        :param x: value to set the region to
        """
        self.region = x

    def get_us_house_seats(self):
        """
        This is the getter method for the number of US House seats.
        :return: the number of US House seats
        """
        return self.us_house_seats

    def set_us_house_seats(self, x):
        """
        This is the setter method for the number of US House seats.
        :param x: value to set the number of US House seats to
        """
        self.us_house_seats = x

    def get_population(self):
        """
        This is the getter method for the population.
        :return: the population
        """
        return self.population

    def set_population(self, x):
        """
        This is the setter method for the population.
        :param x: value to set the population to
        """
        self.population = x

    def get_covid_cases(self):
        """
        This is the getter method for the number of covid cases.
        :return: the number of covid cases
        """
        return self.covid_cases

    def set_covid_cases(self, x):
        """
        This is the setter method for the number of covid cases.
        :param x: value to set the number of covid cases to
        """
        self.covid_cases = x

    def get_covid_deaths(self):
        """
        This is the getter method for the number of covid deaths.
        :return: the number of covid deaths
        """
        return self.covid_deaths

    def set_covid_deaths(self, x):
        """
        This is the setter method for the number of covid deaths.
        :param x: value to set the number of covid deaths to
        """
        self.covid_deaths = x

    def get_full_vax_rates(self):
        """
        This is the getter method for the full vaccination rates.
        :return: the full vaccination rates
        """
        return self.full_vax_rates

    def set_full_vax_rates(self, x):
        """
        This is the setter method for the full vaccination rates. This is a percentage.
        :param x: value to set the full vaccination rates to
        """
        self.full_vax_rates = x

    def get_median_household_income(self):
        """
        This is the getter method for the median household income.
        :return: the median household income
        """
        return self.median_household_income

    def set_median_household_income(self, x):
        """
        This is the setter method for the median household income.
        :param x: value to set the median household income to
        """
        self.median_household_income = x

    def get_violent_crime_rate(self):
        """
        This is the getter method for the violent crime rate.
        :return: the violent crime rate
        """
        return self.violent_crime_rate

    def set_violent_crime_rate(self, x):
        """
        This is the setter method for the violent crime rate.
        :param x: value to set the violent crime rate to
        """
        self.violent_crime_rate = x

    def __str__(self):
        """
        This is the string method for the State class.
        :return: the string representation of the State class
        """

        return (
            'Name           MHI        VCR         CFR          Case Rate    Death Rate   FVR   \n'
            '-----------------------------------------------------------------------------------\n'
            f'{self.state_name: <15}{self.median_household_income: <11}{self.violent_crime_rate: <12}'
            f'{self.case_fatality_rate: <13.6f}{self.case_rate: <13.2f}{self.death_rate: <13.2f}'
            f'{self.full_vax_rates: <6.3}\n'
        )

    def __gt__(self, s):
        """
        This is the greater than method for the State class.
        :param s: the state to compare to
        :return: True if the state has a name that comes first, False otherwise
        """
        s1 = self.state_name
        s2 = s.state_name
        if s1 < s2:
            return True
        else:
            return False


# Global Variable for State List
states = []


def read_data(f_name):
    """
    This function reads the data from the csv file and creates a list of State objects.
    :param f_name: the name of the csv file to read
    :return: number of states read
    """

    with open(f'{f_name}', 'r') as f:
        lines = csv.reader(f)
        next(lines)
        num_lines = 0
        for sn, c, r, uhs, p, cc, cd, fvr, mdi, vcr in lines:
            num_lines += 1
            newState = State(sn, c, r, uhs, p, cc, cd, fvr, mdi, vcr)
            states.append(newState)
        return num_lines


def state_report():
    """
    This function prints a report of the states.
    """
    for s in states:
        print(s)


def partition(arr, low, high):
    """
    This function partitions the array into two parts.
    :param arr: array to partition
    :param low: lowest index
    :param high: highest index
    :return: next index
    """
    i = low - 1
    piv = arr[high]

    for j in range(low, high):
        if arr[j].state_name <= piv.state_name:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    """
    This function sorts the array using the quick sort algorithm.
    :param arr: array to sort
    :param low: lowest index
    :param high: highest index
    """

    if len(arr) == 1:
        return arr
    if low < high:
        part_index = partition(arr, low, high)

        quick_sort(arr, low, part_index - 1)
        quick_sort(arr, part_index + 1, high)


def merge_sort(arr):
    """
    This function sorts the array using the merge sort algorithm.
    :param arr: array to sort
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i].case_fatality_rate < right[j].case_fatality_rate:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1


def binary_search(arr, s, l=0, h=len(states) - 1):
    """
    This function searches for the state in the array using the binary search algorithm.
    :param arr: array to search
    :param s: state name to search for
    :param l: lowest index
    :param h: highest index
    :return: index of state if found, else -1
    """

    if h >= l:

        mid = (h + l) // 2
        if arr[mid].state_name == s:
            return mid
        elif arr[mid].state_name > s:
            return binary_search(arr, s, l, mid - 1)
        else:
            return binary_search(arr, s, mid + 1, h)
    else:
        return -1


def sequential_search(arr, s):
    """
    This function searches for the state in the array using the sequential search algorithm.
    :param arr: array to search
    :param s: state name to search for
    :return: index of state name if found, else -1
    """
    for i in range(len(arr)):
        if arr[i].state_name == s:
            return i
    return -1


def sort_state_name():
    """
    This function sorts the state names in the array using the quick sort algorithm.
    """
    quick_sort(states, 0, len(states) - 1)
    print('States sorted by Name.')


def sort_case_fatality_rate():
    """
    This function sorts the case fatality rates in the array using the merge sort algorithm.
    """
    merge_sort(states)
    print('States sorted by Case Fatality Rate.')


def find_state(s):
    """
    This function searches for the state in the array using the binary search algorithm if
    the data is sorted by state name, and sequential search if otherwise.
    :param s: state name to search for
    """
    # check if states array is sorted by state name
    if all(states[i].state_name <= states[i + 1].state_name for i in range(len(states) - 1)):
        print('Binary Search\n')
        index = binary_search(states, s)
    else:
        print('Sequential Search\n')
        index = sequential_search(states, s)
    if index == -1:
        print(f'Error: {s} not found')
    else:
        print(
            f'Name:       {states[index].state_name: <14}\n'
            f'MHI:        {states[index].median_household_income: <11}\n'
            f'VCR:        {states[index].violent_crime_rate: <12}\n'
            f'CFR:        {states[index].case_fatality_rate: <13.6f}\n'
            f'Case Rate:  {states[index].case_rate: <13.2f}\n'
            f'Death Rate: {states[index].death_rate: <13.2f}\n'
            f'FV Rate:    {states[index].full_vax_rates: <6.3f}\n'
        )


def spearmans():
    """
    This function calculates the Spearman's rank correlation coefficient.
    yet to be implemented
    """
    pass


if __name__ == "__main__":
    """
    This is the main function. It calls the functions to read the data, prints the menu,
    takes user input, and calls the appropriate function.
    """
    file_name = 'States.csv'
    count = read_data(file_name)
    print('CAP4620 Project 1\n')
    print(f'There were {count} state records read from {file_name}')

    while True:
        print(
            '''
1. Print a state report
2. Sort by name
3. Sort by case fatality rate
4. Find and print a State for a given name
5. Print Spearman’s rho matrix
6. Quit
''',
            end=''
        )
        option = input('Enter your choice: ')
        # print(option)
        print()
        if option == '6':
            print('Have a great day!')
            break
        elif option == '1':
            state_report()
        elif option == '2':
            sort_state_name()
        elif option == '3':
            sort_case_fatality_rate()
        elif option == '4':
            state = input('Enter a state name: ')
            find_state(state)
        elif option == '5':
            spearmans()
        else:
            print('ERROR: Invalid choice, please enter 1-6')
