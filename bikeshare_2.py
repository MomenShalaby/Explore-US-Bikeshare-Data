import numpy as np
import pandas as pd
import time
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities=["chicago", "new york city","washington"]
    months=["all","january","february","march","april","may","june"]
    days=["all","sunday",'monday',"tuesday","wednesday",'thursday',"friday","saturday"]
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try :
            city=input("Enter the city name ,choose from:" +str(cities) +" : ").lower().strip()
            if city in cities:
                break
            else:
                print("Please enter one of those cities: "+str(cities)+" : ")
        except ValueError:
            print("Invalid Input")
    # get user input for month (all, january, february, ... , june)
    while True:
        try :
            month=input("Enter month in alphabet(choose from: {} : ".format(str(months))).lower().strip()
            if month in months:
                break
            else:
                print("Please enter one of those months: "+str(months)+" : ")
        except ValueError:
            print("Invalid Input")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try :
            day=input("Enter day in alphabet  (choose from:{}) : ".format(str(days))).lower().strip()
            if day in days:
                break
            else:
                print("Please enter one of those days:  "+str(days)+" : ")
        except ValueError:
            print("Invalid Input")

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    
    
    return df

def time_stats(df,month,day):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June"}
    # display the most common month 
    if month =='all':

        print("The most common month is: ",months[df['month'].mode()[0]])
    else:
        print('you picked this month: ',month)
    # display the most common day of week
    if day=="all":

        print("The most common day of week is: ",df['day_of_week'].mode()[0])
    else:
        print("you picked only this day: ",day)
    # display the most common start hour
    print("The most common start hour is: ",df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station: ",df["Start Station"].mode()[0])

    # display most commonly used end station
    print("The most common end station: ",df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    print("The most frequent start station and end station are: ",df[["Start Station", "End Station"]].mode().iloc[0,:].to_string(index=False,header=False))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is: " ,df["Trip Duration"].sum())

    # display mean travel time
    print("The mean travel time is: " ,df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print(df["User Type"].value_counts().to_string())
    # Display counts of gender
    print(df["Gender"].value_counts().to_string())

    # Display earliest, most recent, and most common year of birth
    print("The earliest year of birth",df['Birth Year'].min())
    print("The most recent year of birth",df['Birth Year'].max())
    print("The most common year of birth",df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        if city != "washington":
            user_stats(df)
        while True:
            viewData = input("Would you like to 5 lines of the raw data? Type 'yes' or 'no'.")
            if viewData == "yes":
                print(df.sample(5))
            else:
                break
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    


if __name__ == "__main__":
    main()

