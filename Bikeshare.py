import time
import pandas as pd
import numpy as np

#Additional change to documentation

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
    #TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities= ['chicago','new york city','washington']
        city= input("\n Hey there! Please choose one of the following cities: Chicago, New york city, Washington \n>>>").lower()
        if city in cities:
            break
        else:
            print("\n Oops, Please enter a valid city name")    


    #TO DO: get user input for month (all, january, february, ... , june or none)
    while True:
      months= ['January','February','March','April','May','June','All']
      month=input("\n Thank you, Which month would you love to work on? (January, February, March, April, May, June)? Type 'All' for no month filter \n>>>").title()
      if month in months:
            break
      else:
           print("\n Oops, Please enter a valid month")    


    #TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
        day = input("\n Which day of the week would you like to consider? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? Type 'All' for no day filter \n>>>").title()         
        if day in days:
            break
        else:
            print("\n That seems not to be a known day, Please enter a valid day")    
    
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

    
    # loading data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding integers
        months = ['January', 'February', 'March', 'April', 'May', 'June','All']
        month = months.index(month)+1
    
        # filter by month to create new df (dataframe)
        df = df[df['month']==month] 

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day]

    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month =='All':
        most_popular_month= df['month'].mode()[0]
        months= ['January','February','March','April','May','June','All']
        most_popular_month= months[most_popular_month-1]
        print("The most common month is:",most_popular_month)


    # TO DO: display the most common day of week
    if day =='All':
        most_popular_day= df['day_of_week'].mode()[0]
        print("The most common day of the week is:",most_popular_day)


    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    most_popular_hour=df['Start Hour'].mode()[0]
    print("The common Start Hour: {}:00 hrs".format(most_popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station= df['Start Station'].mode()[0]
    print("The most commonly used Start Station: {}".format(common_start_station))


    # TO DO: display most commonly used end station
    common_end_station= df['End Station'].mode()[0]
    print("The most commonly used End Station: {}".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" "+"to"+" "+ df['End Station']
    most_freq_comb= df['combination'].mode()[0]
    print("The most frequent combination of Start and End Station is {} ".format( most_freq_comb))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("The total trip duration:", total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_duration=df['Trip Duration'].mean()
    print("The average trip duration:", mean_travel_duration)
                          
    # TO DO: display max travel time
    max_travel_duration=df['Trip Duration'].max()
    print("The maximum trip duration:", max_travel_duration)
                      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts= df['User Type'].value_counts()
    print("The user types are:\n",user_counts)


    # TO DO: Display counts of gender
    if city.title() == 'Chicago' or city.title() == 'New York City':
        gender_count= df['Gender'].value_counts()
        print("\nThe counts of each gender are: \n",gender_count)
    
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_YOB= int(df['Birth Year'].min())
        print("\nThe user with the earliest birth year was born in the year: ",earliest_YOB)
        most_recent_YOB= int(df['Birth Year'].max())
        print("The user with the most recent birth year was born in the year: ",most_recent_YOB)
        most_common_YOB= int(df['Birth Year'].mode()[0])
        print("The most common year of birth: ",most_common_YOB)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)         
def display_data(df):

    while True:
        response=['yes','no']
        question_option= input("Would you like to view individual trip data (6 entries)? Type 'yes' or 'no'\n").lower()
        if question_option in response:
            if question_option=='yes':
                start=0
                end=6
                data = df.iloc[start:end,:9]
                print(data)
            break     
        else:
            print("Oops, Please enter a valid response to the provided question")
    if  question_option=='yes':       
            while True:
                question_option_2= input("Would you like to view more trip data? Type 'yes' or 'no'\n").lower()
                if question_option_2 in response:
                    if question_option_2=='yes':
                        start+=6
                        end+=6
                        data = df.iloc[start:end,:9]
                        print(data)
                    else:    
                        break  
                else:
                    print("Oops, Please enter a valid response from the provided option")          

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
