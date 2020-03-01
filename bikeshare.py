import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    print('-'*60)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        # print('Please Enter a number to select city \n0 for chicago\n1 for new york city\n2 for washington\n')
        citys = ['chicago','new york city','washington']
        num_in = input('Please Enter a number to select city \n0 for chicago\n1 for new york city\n2 for washington\nType Here: ')
        try:
            num_in = int(num_in)
            if num_in in range(3):
                city = citys[num_in].lower()
                print('\n{} is the city you select\n'.format(city).upper())
                print('City Enter Successful! Enter Next Step!')
                break
            else:
                print('The Number You Entered is NOT Among [0,1,2]!')
                continue
        except ValueError as verr:
            print('Getting a {} error \nPlease make sure you enter a integer number among [0,1,2]'.format(verr))

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        # print('Please Enter a number to select month\n1 for  january\n2 for  february\n3 for  march\n4 for  april\n5 for  may\n6 for  june\n0 for  all')
        months = ['all','january', 'february', 'march', 'april', 'may', 'june']
        num_in = input('Please Enter a number to select month\n1 for  january\n2 for  february\n3 for  march\n4 for  april\n5 for  may\n6 for  june\n0 for  all\nType Here: ')
        try:
            num_in = int(num_in)
            if (num_in in range(7)):
                month = months[num_in]
                print('\n{} is the month you select\n'.format(month).upper())
                print('month Enter Successful! Enter Next Step!')
                print('-'*60)
                break
            else:
                print('The number You Entered is NOT Among [0,1,2,3,4,5,6]!')
                continue
        except ValueError as verr:
            print('Getting a {} error \nPlease make sure you enter a integer number among [0,1,2,3,4,5,6]'.format(verr))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        # print('Please Enter a number to select a day of a week\n1 for  monday\n2 for  tuesday\n3 for  wednesday\n4 for  thursday\n5 for  friday\n6 for  saturday\n7 for  sunday\n0 for  all')
        dow = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        num_in = input('Please Enter a number to select a day of a week\n1 for  monday\n2 for  tuesday\n3 for  wednesday\n4 for  thursday\n5 for  friday\n6 for  saturday\n7 for  sunday\n0 for  all\nType Here: ')
        try:
            num_in = int(num_in)
            if (num_in in range(8)):
                day = dow[num_in]
                print('{} is the day of a week you select'.format(day))
                print('Day Enter Successful! Enter Next Step!')
                break
            else:
                print('The number You Entered is NOT Among [0,1,2,3,4,5,6,7]!')
                continue
        except ValueError as verr:
            print('Getting a {} error \nPlease make sure you enter a integer number among [0,1,2,3,4,5,6,7]'.format(verr))


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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df,city

def time_stats(df,city, month, day):
    """
    Displays statistics on the most frequent times of travel.
    input: df (pd.DataFrame)  of the selected city
           city(string) selected
           month(string) selected
           day(string) day of a week selected
    output:
    does not return anything but creat and save bar plot for frequency analysis under same directory
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common month
    most_common = df['month'].mode()
    if df['month'].unique().size == 1:
        print('Only Presenting the month you selected earlier: {}'.format(month.title()))
        # print('{} references available for this month'.format(df['month'].size))
    else:
        print('Top 3 popular months: \n{}'.format(df['month'].value_counts().head(3)))
        print('_'*30)
        print('LookUp Table:\n1 for  january\n2 for  february\n3 for  march\n4 for  april\n5 for  may\n6 for  june\n')
        print('_'*30)
        df['month'].value_counts().plot(kind='bar')
        plt.xlabel('Month')
        plt.ylabel('Number of visits')
        plot_name = city+'_popularity_versus_'+'month.png'
        plt.savefig(plot_name)
        print('The Most popular month is: {}\n'.format(most_common[0]))
    #print('-'*40)
    # TO DO: display the most common day of week
    most_common = df['day_of_week'].mode()
    if df['day_of_week'].unique().size == 1:
        print('Only Presenting the day of a week you selected earlier: {}'.format(day.title()))
        # print('{} references available for this day'.format(df['day_of_week'].size))
    else:
        print('Top 3 popular day of a week: \n{}\n'.format(df['day_of_week'].value_counts().head(3)))
        print('_'*30)
        print('LookUp Table:\n1 for  monday\n2 for  tuesday\n3 for  wednesday\n4 for  thursday\n5 for  friday\n6 for  saturday\n7 for  sunday')
        print('-'*30)
        df['day_of_week'].value_counts().plot(kind='bar')
        plt.xlabel('day_of_week')
        plt.ylabel('Number of visits')
        plot_name = city+'_popularity_versus_'+'day_of_week.png'
        plt.savefig(plot_name)
        print('The Most popular day of a week is: {}\n'.format(most_common[0]))
    print('-'*40)
    # TO DO: display the most common start hour
    most_common = df['hour'].mode()
    print('Top 3 popular time of a day is: \n{}'.format(df['hour'].value_counts().head(3)))
    print('_'*30)
    df['hour'].value_counts().plot(kind='bar')
    plt.xlabel('hour')
    plt.ylabel('Number of visits')
    plot_name = city+'_popularity_versus_'+'hour.png'
    plt.savefig(plot_name)
    print('The Most popular time of a day is: {}'.format(most_common[0]))
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    num=0
    while True:
        print('Do you want to view the row data?')
        raw = input('Type Here[y/n]: ').lower()
        if (raw == 'y' and num<df.shape[0]-1):
            print(df.iloc[num:min(num+5,df.shape[0])])
            num+=5
            continue
        elif (raw == 'n'):
            break
        else:
            print('please enter y or n only!')
            continue
    print('-'*40)


def station_stats(df,city):
    """Displays statistics on the most popular stations and trip.
        input: df (pd.DataFrame)  of the selected city
               city(string) selected
        output:
        does not return anything but creat and save bar plot for frequency analysis under same directory
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common = df['Start Station'].mode()
    print('The Most popular Start Station is: {}\n'.format(most_common[0]))
    print('The Top 3 popular Start Station is: \n{}\n\n'.format(df['Start Station'].value_counts().head(3)))
    df['Start Station'].value_counts().head(10).plot(kind='bar')
    plt.xlabel('Start Station')
    plt.ylabel('Number of visits')
    plot_name = city+'_popularity_versus_'+'Start Station_Top_10.png'
    plt.savefig(plot_name)

    # TO DO: display most commonly used end station
    most_common = df['End Station'].mode()
    print('The Most popular End Station is: {}\n'.format(most_common[0]))
    print('The Top 3 popular End Station is: \n{}\n\n'.format(df['End Station'].value_counts().head(3)))
    df['End Station'].value_counts().head(10).plot(kind='bar')
    plt.xlabel('End Station')
    plt.ylabel('Number of visits')
    plot_name = city+'_popularity_versus_'+'End Station_Top_10.png'
    plt.savefig(plot_name)
    # TO DO: display most frequent combination of start station and end station trip
    #combine = df['Start Station'] + df['End Station']
    df['Start_to_End'] = df[['Start Station', 'End Station']].apply(lambda x: ' --> '.join(x), axis=1)
    most_common = df['Start_to_End'].mode()
    print('The Most popular Start_to_End is: \n{}\n'.format(most_common[0]))
    print('The Top 3 popular Start_to_End is: \n{}\n'.format(df['Start_to_End'].value_counts().head(3)))
    df['Start_to_End'].value_counts().head(10).plot(kind='bar')
    plt.xlabel('Start_to_End')
    plt.ylabel('Number of visits')
    plot_name = city+'_popularity_versus_'+'Start_to_End_Top_10.png'
    plt.savefig(plot_name)

    print("\nThis took %s seconds." % (time.time() - start_time))
    num=0
    while True:
        print('Do you want to view the row data?')
        raw = input('Type Here[y/n]: ').lower()
        if (raw == 'y' and num<df.shape[0]-1):
            print(df.iloc[num:min(num+5,df.shape[0])])
            num+=5
            continue
        elif (raw == 'n' or num>=df.shape[0]-1):
            break
        else:
            print('please enter y or n only!')
            continue
    print('-'*40)


def trip_duration_stats(df,city):
    """Displays statistics on the total and average trip duration.
    input: df (pd.DataFrame)  of the selected city
           city(string) selected
    output:
    does not return anything but creat and save bar plot for frequency analysis under same directory
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is:   {}\n '.format(df['Trip Duration'].sum()))
    # TO DO: display mean travel time
    print('Average travel time is: {}\n'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))

    num=0
    while True:
        print('Do you want to view the row data?')
        raw = input('Type Here[y/n]: ').lower()
        if (raw == 'y' and num<df.shape[0]-1):
            print(df.iloc[num:min(num+5,df.shape[0])])
            num+=5
            continue
        elif (raw == 'n' or num>=df.shape[0]-1):
            break
        else:
            print('please enter y or n only!')
            continue
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users.
    input: df (pd.DataFrame)  of the selected city
           city(string) selected
    output:
    does not return anything but creat and save bar plot for frequency analysis under same directory
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of User Type:\n.{}\n\n'.format(df['User Type'].value_counts()))
    df['User Type'].value_counts().plot(kind='bar')
    plt.xlabel('User Type')
    plt.ylabel('Number of visits')
    plot_name = city+'_popularity_versus_'+'User Type.png'
    plt.savefig(plot_name)
    # TO DO: Display counts of gender
    try:
        print('Counts of User Gender:\n.{}\n\n'.format(df['Gender'].value_counts()))
        df['Gender'].value_counts().plot(kind='bar')
        plt.xlabel('User Gender')
        plt.ylabel('Number of visits')
        plot_name = city+'_popularity_versus_'+'Gender.png'
        plt.savefig(plot_name)
    except KeyError as err:
        print('Attempt to get Gender info')
        print('{} Error Occur! No Gender Info find'.format(err))
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        stats = df['Birth Year'].describe()
        print('User Ealiest Year of Birth: {}'.format(stats['min']))
        print('User Most Recent Year of Birth: {}'.format(stats['max']))
        print('User Most Common Year of Birth: {}'.format(df['Birth Year'].mode()[0]))
    except KeyError as err:
        print('Attempt to get Year of Birth info\n{} Error Occur! No Year of Birth Info find'.format(err))


    print("\nThis took %s seconds." % (time.time() - start_time))
    num=0
    # section = 5
    while True:
        print('Do you want to view the row data?')
        raw = input('Type Here[y/n]: ').lower()
        if (raw == 'y' and num<df.shape[0]-1):
            print(df.iloc[num:min(num+5,df.shape[0])])
            num+=5
            continue
        elif (raw == 'n' or num>=df.shape[0]-1):
            break
        else:
            print('please enter y or n only!')
            continue

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df,city = load_data(city, month, day)
        time_stats(df,city, month, day)
        station_stats(df,city)
        trip_duration_stats(df,city)
        user_stats(df,city)
        print('*'*40)
        print('PLEASE GO UNDER THE SAME DIRECTORY FOR DATA ANALYSIS BAR PLOT')
        print('*'*40)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
