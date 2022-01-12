import time
import pandas as pd
import numpy as np

#Create a dictionary holding the data sources
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#assign the keys to a variable
CITY = CITY_DATA.keys()

#define a function to get the specified inputs and filters from users
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    #Defines a function to handle invalid inputs
    def choice_response():
        if city not in CITY:
            return "oops, this input is invalid. Please check your input and try again\n\nRestarting..."
        elif month not in MONTH:
            return "oops, this input is invalid. Please check your input and try again\n\nRestarting..."
        elif day not in WEEK_DATA:
            return "oops, this input is invalid. Please check your input and try again\n\nRestarting..."
        else:
            pass

# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #Creating an empty city variable to store input from user
    city = " "
    while city not in CITY:

        print("\nWelcome! Please choose your city")
        print("\n1.Chicago\n2.New york city\n3.Washington")
        print("\nInput should be in the format below e.g 'Chicago' ")

        #Converting user input to lower case to standardize them
        city = input().lower()

        if city not in CITY:
            print(choice_response())
    print("\nYou have chosen {} city".format(city.title()) )

    # TO DO: get user input for month (all, january, february, ... , june)

    #Create a dictionary to store all the months including the 'all' option
    MONTH_DATA = {"january":1, "february":2, "march":3, "april":4, "may":5 ,"june":6, "all":7}
    MONTH = MONTH_DATA.keys()
    month = " "
    while month not in MONTH:
        print("\nPlease indicate the month between January and June for which you want data:")
        print("\nAcccepted input format:\nProvide full month name in title case (e.g January)")
        print("\nIf you choose to view data for all the months, please input 'all' ")
        month = input().lower()

        if month not in MONTH:
            print(choice_response())
    print("You have chosen to view {} data".format(month.title()) )


    WEEK_DATA = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = " "
    while day not in WEEK_DATA:
        print("\nPlease indicate the day of the week for which you want data:")
        print("\nInput format:\nprovide full  name in title case (e.g Monday)")
        print("\nIf you choose to view data for all the days of the week, please input 'all' ")
   # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input().lower()
        if day not in WEEK_DATA:
            print(choice_response())
    print("\nYou have chosen to view {} data".format(day.title()) )
    print("\nyour selection is as follows:\n city - {}, month(s) - {} and day(s) - {}".format(city.upper(), month.upper(), day.upper()))


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("\nLoading data...")
    ## load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    ##convert the start time column to date time
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    ##Extract the month and day of the week form start timer to create new columns
    df["Month"] = df["Start Time"].dt.month
    df["Day_of_week"] = df["Start Time"].dt.day_name()

    ##Filter by month if applicable
    if month != "all":
        months =  ["january", "february", "march", "april", "may", "june"]
        month = months.index(month)+1

        ##filter by month and create an new dataframe
        df = df[df["Month"] == month]

    ##filter by day of week if applicable
    if day != "all":
        df = df[df["Day_of_week"] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df["Month"].mode()[0]
    print("Most popular month (where January = 1 ,..., June = 6): {}".format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df["Day_of_week"].mode()[0]
    print("Most popular day of the week : {}".format(popular_day))

    # TO DO: display the most common start hour
    ## extract hour from the start time column to create an hour column
    df["Hour"] = df["Start Time"].dt.hour


    ## find the most popular hour
    popular_hour = df["Hour"].mode()[0]
    print("The most popular start hour: {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("\nMost Commonly Used Start Station: {}".format(most_used_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("\nMost Commonly Used End Station: {}".format(commonly_used_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df["Start_end_station"] = (df["Start Station"] + " - " + df["End Station"])
    most_freq_start_end_station_combo = df["Start_end_station"].mode()[0]
    print("\nThe most frequently used combination of start and end station : {}".format(most_freq_start_end_station_combo))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df["Trip Duration"].sum()
    #Calculate duration in minutes and second
    minute, second = divmod(total_duration, 60)
    #Calculate the duration in Hours
    hours, minute = divmod(minute, 60)

    print("The total travel time is {} hours, {} minutes and {} seconds".format(hours,minute,second))


    # TO DO: display mean travel time
    average_travel_time = round(df["Trip Duration"].mean())

    #Find the average travel time in minutes and seconds
    mins,seconds = divmod(average_travel_time, 60)
    #Filter to print out hour format if minutes exceed 60
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print("The average trip duration is {} hrs, {} mins and {} seconds".format(hrs,mins,seconds))
    else:
        print("the average trip duration is {} mins and {} seconds".format(mins,seconds))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types = df["User Type"].value_counts().to_string()
    print("The number of users in each user type is seen below: \n\n{}".format(count_of_user_types))

    # TO DO: Display counts of gender
    #Use the try and except clause to display the number of users by gender and also accommodate files with no gender data
    try:
        count_of_gender = df["Gender"].value_counts().to_string()
        print("\nThe type of users by gender is given below:\n{}".format(count_of_gender))
    except:
        print("We are sorry! There are no gender data in this file")



    # TO DO: Display earliest, most recent, and most common year of birth
    #Use the try and except clause to display the earliest, most recent and common year of birth and also accommodate files with no birth data
    try:
        earliest_year_of_birth = int(df["Birth Year"].min())
        most_recent_year_of_birth = int(df["Birth Year"].max())
        most_common_year_of_birth = int(df["Birth Year"].mode()[0])
        print("\nThe earliest year of birth is: {}\n\nThe most recent year of birth is: {}\n\nThe most common year of birth is: {}\n".format(earliest_year_of_birth,most_recent_year_of_birth,most_common_year_of_birth))

    except:
        print("We are sorry! There are no birth date data in this file")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    response_list = ["yes", "no"]
    response_data = ""
    counting_input = 0
    while response_data not in response_list:
        print("\nDo you wish to view the raw data?\n\nPlease respond with either 'Yes' or 'No'")
        response_data = input().lower()
        if response_data == "yes":
            print(df.head())
        elif response_data not in response_list:
            print("\nPlease check your input\nInput does not match the accepted response\nAccepted response is either YES or NO\nRestarting...")

    #Loop to ask if the user wants to keep viewing data
    while response_data == "yes":
        print("Do you wish to view more raw data?")
        counting_input +=5
        response_data = input().lower()
        #print additional 5 rows if customer inputs yes
        if response_data == "yes":
            print(df[counting_input:counting_input+5])
        elif response_data != "yes":
            break

    print("-"*80)



#Min Function to call all previous sections
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
