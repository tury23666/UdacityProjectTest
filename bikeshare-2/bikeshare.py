import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_LIST = ["all", "january", "february", "march", "april", "may", "june"]
DAY_LIST = ["all", "monday","tuesday","wednesday", "thursday", "friday", "saturday", "sunday"]
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    correct_city = False
    while(not correct_city):
        city_input = input("What city do you want to know information about?: ")
        city = city_input.lower()
        if(city=="chicago" or city =="new york city" or city=="washington"):
            correct_city = True
        
    # TO DO: get user input for month (all, january, february, ... , june)
    correct_month = False
    while(not correct_month):
        month_input = input("What month, all, january, february, march, april, may, june?: ")
        month = month_input.lower()
        if(month in MONTH_LIST):
            correct_month = True
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    correct_day = False
    while(not correct_day):
        day_input = input("Input for day of week (all, monday, tuesday, ... sunday)?: ")
        day = day_input.lower()
        if(day in DAY_LIST):
            correct_day = True
     


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
    df = pd.read_csv(CITY_DATA[city])
#     print(df.head())
#     print(df.columns)
#     print(df.info())
#     print(df.describe())
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    df['month'].value_counts()
    popular_month = df['month'].mode()[0]
    print("Most common month: " , popular_month)
    # TO DO: display the most common day of week
    df['day_of_week'].value_counts()
    popular_day = df['day_of_week'].mode()[0]
    print("Most common day of the week: " , popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common start hour: " , popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station: " , popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station: " , popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Pair'] = df['Start Station'] + ' <-> ' + df['End Station']
    most_common_pair = df['Station Pair'].mode()[0]
    sp_counts = df['Station Pair'].value_counts()
    print("The most common trip is: ", most_common_pair, " count: ", sp_counts[0] )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
#     print(df['Start Time'].dtype)     
#     print(df['End Time'].dtype) 

    # TO DO: display total travel time
    most_common_pair = df['Station Pair'].mode()[0]
#     print(most_common_pair)
    df['time_travel'] = pd.to_datetime (df['End Time']) - pd.to_datetime (df['Start Time'])
    subset_df = df[df['Station Pair'] == most_common_pair]
#     print(subset_df)
    max_time_travel = subset_df['time_travel'].sum()
    print("Total travel time for this common trip: ", max_time_travel )
    
    # TO DO: display mean travel time
    average_travel = subset_df['time_travel'].mean()
    print("The mean travel time for this trip", average_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("Counts of user types : ")
    print(user_type_counts)
    print()

    # TO DO: Display counts of gender
#     print(df['Gender'])
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender : ")
        print(gender_counts)
        print()

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year_earliest = df['Birth Year'].min()
        birth_year_recent = df['Birth Year'].max()
        birth_year_common = df['Birth Year'].mode()
        print("Earliest Birth Year : ", birth_year_earliest)
        print("Most Cecent Birth Year : ", birth_year_recent)
        print("Most Common Birth Year : ", birth_year_common)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    """Displays statistics of 5 line raw data"""
    raw_promp = False
    while_key = True
   
    row_start_index = 0
    row_end_index = 5
    pd.set_option('display.max_columns', None)
#     print(len(df))
    
    while(while_key):
        raw_data = input("Do you want to see 5 liens of raw data ?")
        raw_data = raw_data.lower()  
        
        if raw_data == "yes":
            raw_promp = True
            if row_end_index > len(df):
                row_end_index = len(df)
                while_key = False
            sliced_df = df.iloc[row_start_index:row_end_index]
            print(sliced_df)
            row_start_index = row_start_index + 5
            row_end_index = row_end_index + 5


        if raw_data == "no":
            raw_promp = False
            while_key = False 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
#         print(df.head())        
#         print(df.columns)

        time_stats(df)
        
#         print(df.head())        
#         print(df.columns)
        
        station_stats(df)
        
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
