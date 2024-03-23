from most_active_cookie import CLIParser, date_validation, main, returnMostActiveCookie,fileValidation, readFile

main(['cookie_log.csv', '--date', '2018-12-09'])

# Date Validation
def test_date_check():
    array = [[2222,12,20], [1001,9,20], [2222,15,45]]
    expectedOutput = [True, True, False]
    for i in range(len(array)):
        isValid = date_validation(array[i])
        assert isValid==expectedOutput[i], "Failed for date {} ".format(array[i])

# File Validation
def test_check_file():
    files=['cookie_csv', 'cookie.csv', 'cookie.txt', ' .csv', ' .txt']
    expectedOutput = [False, True, False, True, False]
    for i in range(len(files)):
       checkFileName=fileValidation(files[i])
       assert checkFileName==expectedOutput[i], "Failed for file {} ".format(files[i])

# Invalid File Entries
def test_invalid_entries():
    openFile=readFile('cookie_log_invalid.csv', '2021-12-09')
    assert openFile==False, "This file does not have the entries in correct format. The entries should be as follows: cookie,timestamp"

# No active cookies exists for provided date
def test_no_active_cookie():
    activeCookie=readFile('cookie_log.csv', '2021-12-09')
    assert activeCookie==False, "No active cookie exists for the provided date"

# Positive test case
def test_positive():
    assert readFile('cookie_log.csv', '2018-12-08') == True


       
   