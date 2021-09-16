from datetime import date, time, datetime
import pandas as pd

date(year=2020, month=1, day=31)

date_string = "01-31-2020 14:45:37"
format_string = "%m-%d-%Y %H:%M:%S"

"""
Component	                                        Code	Value
Year (as four-digit integer )	                    %Y	    2020
Month (as zero-padded decimal)	                    %m	    01
Date (as zero-padded decimal)	                    %d	    31
Hour (as zero-padded decimal with 24-hour clock)	%H	    14
Minute (as zero-padded decimal)	                    %M	    45
Second (as zero-padded decimal)	                    %S	    37
"""

datetime = datetime.strptime(date_string, format_string)

# Controlling formats:
format(datetime)
format(datetime, format_string)

# Datetime in pandas dataframe
print(date_string)
date_string1 = date_string
date_string2 = "03-25-2020 14:45:37"
test = pd.DataFrame({"timestamp": [date_string1, date_string2]})

var = test.dtypes
var
