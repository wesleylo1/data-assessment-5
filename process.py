log_file = open("um-server-01.txt") # open up a file, saved to a variable


def sales_reports(log_file): # create a function named sales_reports
    for line in log_file: # for every line in the file
        line = line.rstrip() # remove any trailing characters/space between strings
        day = line[0:3] # the first 3 items of line is saved to variable called day. Index 0 up to 3, not including 3.
        if day == "Mon": # if the day is equal to Tuesday, changed to Monday.
            print(line) # print out the line


sales_reports(log_file) # invoking the function sales_report
