import tweet 
import read_data
import sys

airport = sys.argv[1]

read_data.read_data(airport)
tweet.tweet(airport)

#line()
