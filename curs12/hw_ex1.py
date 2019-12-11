#1. Calculate when python course ends. Start date (28.10.2019) + 15 weeks + 8 days of vacation.

from datetime import datetime, timedelta

start_date = datetime.strptime('28.10.2019', '%d.%m.%Y')

print(start_date + timedelta(days=10) + timedelta(weeks=15))