import time
from web_scraper import *

n = int(input('How many time do you want to press more: '))
for i in range(n):
    time.sleep(3)
    more_posts()


input('Everything is ready\nPress Enter to view the results')
view_posts()
