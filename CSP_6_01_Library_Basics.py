#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)

import analytics
# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    return analytics.apply_markup(rawPrices, 15)

    pass


# Modify the below function such that it asks the user for n scores
# and then returns the highest score and the average score of the list.
def analyze_scores(n):
    highest=analytics.get_highest(n)
    average = analytics.get_average(n)
    return highest and average
    pass

# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
#and all letters lower case.
def sanitize_usernames(n):
    return analytics.clean_text(n)

    pass


# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(n):
    return analytics.filter_threshold(n,100)
    pass


# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
#Sanitize the list to only be lower case word with no extra spaces
#Then return the location of the word using binary search if the list is in order and linear search if it is not.
#example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(nlist):
    x = 0
    y = x+1
    length = len(nlist)
    search = input("enter what to search for")
    new = analytics.clean_text(nlist)
    for i in range (length):
        if nlist[x] < nlist[y]:
            x = x+1
        else:
            listquality = "not sorted" #test if sorted or not
            break

    if listquality == "not sorted":
        return analytics.linear_search(nlist, search)
    else:
        return analytics.binarySearch(nlist, search)


