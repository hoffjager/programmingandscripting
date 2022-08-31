# This program creates a tuple storing the months of the year.
# From this tuple, we will create another tuple within.
# This will display the summer months, one at a time.
# Author: Jonathon Grealish

months = ("January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
)

summer = months[4:7] # Index 4 will begin with May, and display all below Index 7 (August)
for month in summer:
    print(month)