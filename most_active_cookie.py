#!/usr/bin/env python
import sys
from collections import defaultdict
import argparse

# Function for validating the date provided by user
def date_validation(date_split):
    if len(date_split) != 3:
        print("Incorrect Date Format. Date to find most active cookie should be in the format 'YYYY-MM-DD'")
        exit()

    year = int(date_split[0])
    month = int(date_split[1])
    day = int(date_split[2])

    is_leap_year = ((year % 400 == 0) and (year % 100 == 0)) or (
        (year % 4 == 0) and (year % 100 != 0))

    if is_leap_year:
        feb_days = 29
    else:
        feb_days = 28

    month_to_days_map = {1: 31, 2: feb_days, 3: 31, 4: 30,
                        5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    # Validating the year, month and day
    if year < 1000 or year > 9999: 
        print("Incorrect Year")
        #exit()
        return False

    elif month > 12: 
        print("Incorrect Month")
        #exit()
        #pass
        return False
    
    elif day > month_to_days_map[month]:
        print("Incorrect Day")
        #exit()
        #pass
        return False
    
    return True

def readFile(csv_file, provided_date):
    # Checking for file I/O errors
    try:
        cookie_file = open(csv_file, 'r')
    except IOError:
        print("Error: could not read file {}. No file with this name exists.".format(csv_file))
        return False
    # Since file exists, the contents are read and parsed
    contents = cookie_file.readlines()
    cookie_file.close()
    flag = returnMostActiveCookie(contents, provided_date)
    if not flag:
        print("No active cookie exists for the provided date")
    return flag

def returnMostActiveCookie(contents, provided_date):
    # Creating a hashmap to count the occurrence for a cookie in a day based on the date entered by the user in the command line
    hashMap = defaultdict(int)
    for cookies in contents[1:]:
        #print(len(cookies.split(',')))
        if len(cookies.split(','))!=2:
            return False
        cookie, timestamp = cookies.split(',')
        date, time = timestamp.split('T')
        if date == provided_date:
            hashMap[cookie] += 1
        elif date < provided_date:
            break

    # The cookies with the highest frequency are returned on separate lines
    if len(hashMap)==0:
        return False
    
    maximum = max(hashMap.values())
    for i in hashMap:
        if hashMap[i] == maximum:
            print(i)
    return True

def CLIParser(args):
    csv_file = args.filename

    isFileValid = fileValidation(csv_file)
    provided_date = args.date

    date_split = provided_date.split('-')

    if date_validation(date_split) and isFileValid:
        readFile(csv_file, provided_date)

def fileValidation(csv_file):
    # File validation. Only accepting files with .csv format
    file_split = csv_file.split('.')
    if len(file_split) != 2 or file_split[-1] != 'csv':
        print("Unable to parse file. Incorrect or no extension provided. The file should be a CSV.")
        return False
    return True

def main(argv=None):
    parser = argparse.ArgumentParser(
    description='Most active cookie for a specified day.')
    parser.add_argument('filename')
    parser.add_argument('-d', '--date', help="Date to find most active cookie should be in the format 'YYYY-MM-DD'")
    args = parser.parse_args(argv)
    CLIParser(args)

if __name__== '__main__':
    main()




