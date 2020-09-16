import time
import pandas as pd
import numpy as np
CITY_DATA= { 'chicago': 'chicago.csv',
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Please select a city (Chicago, New York City, or Washington):  ').lower()
        print('\nYou entered ' + city) 
        # check if input is valid, if it is not, request new input
        if city in CITY_DATA:
            break
        else:
            print('This is not a valid answer')

    # get user input for month (all, january, february, ... , june)
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    while True:
        month = input('\nPlease select a month from the following options \n All, January, February, March, April, May, June:  ').title()
        print('\nYou entered ' + month) 
        # check if input is valid, if it is not, request new input
        if month in months:
            break
        elif month == 'All':
            break
        else:
            print('This is not a valid answer')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nPlease select a day from the following options \n All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday:  ').title()
        print('\nYou entered ' + day)
        daylist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        # check if input is valid, if it is not, request new input
        if day in daylist:
            break
        elif day == 'All':
            break
        else:
            print('This is not a valid answer')

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
    # read in csv from user selection
    df = pd.read_csv(CITY_DATA[city])
    
    #define start time as date, and create new columns for month and day
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.strftime('%B')
    df['Day'] = df['Start Time'].dt.strftime('%A')
    # washington is missing 2 columns, create and fill below
    if city == "washington":
        df['Gender'] = np.nan
        df['Birth Year'] = np.nan

    
    # filter month
    if month != 'All':
       df= df[df['Month']==month]

    
    # filter day
    if day !='All':
        df=df[df['Day']==day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # calculate and display the most common month
    commmth = df['Month'].value_counts().idxmax()
    
    print("The most common month is " + commmth)

    # calculate and display the most common day of week
    commday=df['Day'].value_counts().idxmax()
    
    print("The most common month is " + commday)

    # calculate and display the most common start hour
    commstarthr = df['Start Time'].dt.strftime('%H').value_counts().idxmax()
    print ("The most common start time is " + commstarthr)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # calculate and display most commonly used start station
    commonstart = df['Start Station'].value_counts().idxmax()
    print('The most common starting station is: ' + commonstart)
    
    # TO DO: display most commonly used end station
    commonend = df['End Station'].value_counts().idxmax()
    print('The most common end station is: ' + commonend)
    # calculate and display most frequent combination of start station and end station trip
   
    trip = df['Start Station'].str.cat(df['End Station'],sep=" to ").value_counts().idxmax()
    print('The most common full trip is ' + trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # calculate and display total travel time
    travelsum=df['Trip Duration'].sum()
    travelmin = travelsum/60
    travelhr = travelmin/60
    travelday = int(travelhr/24)
    modmin = int(travelmin%60)
    modsec = int(travelsum%60)
    modhr = int(travelhr%24)
    print(('Total travel time is {} days, {} hrs, {} min, {} sec').format(travelday, modhr, modmin, modsec))

    # calculate and display mean travel time
    travelmean=df['Trip Duration'].mean()
    travelmin = travelmean/60
    travelhr = travelmin/60
    modmin = int(travelmin%60)
    modsec = int(travelmean%60)
    modmin = int(travelmin%60)
    print(('Average travel time is {} min, {} sec').format(modmin, modsec))
    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
#
    print('\nCalculating User Stats...\n')
    start_time = time.time()
#
    # calculate and Display counts of user types
    ut = df['User Type'].value_counts()
    print('Counts of User Types in your selection')
    print(ut)
   
    # handle missing gender
    if df['Gender'].isnull().all():
        print('\nGender is undefined')
     # calculate and Display counts of gender    
    else:
        gendercounts = df['Gender'].value_counts()
        print('\nCounts of Gender in your selection')
        print(gendercounts)

    # handle missing birth year
    if df['Birth Year'].isnull().all():  
        print('\nBirth Year is undefined')
    # calculate and Display earliest, most recent, and most common year of birth
    else:
        earliestyear=int(df['Birth Year'].min())
        mostrecent=int(df['Birth Year'].max())
        commonyear=int(df['Birth Year'].value_counts().idxmax())
        print(('\nThe earliest birth year is {}, the most recent birth year is {}, and the most common birth year is {}').format(earliestyear, mostrecent, commonyear))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    #print dataframe header if requested
    while True:
        datasnap = input("Would you like to see a snapshot of the rawdata? ").lower()
        if datasnap == 'yes' or datasnap == 'y':
            print(df.head())
            break
        else:
            break
                         
#run program
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
