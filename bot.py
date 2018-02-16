import datetime
import pi
import tweepy


todays_date = datetime.datetime.now().strftime('%y-%m-%d')
today_str = datetime.datetime.now().strftime('%y%m%d')

index = pi.str.index(today_str)
before = pi.str[index-8:index]
after = pi.str[index+6:index+14]

CONSUMER_KEY = '***'
CONSUMER_SECRET = '***'
ACCESS_TOKEN = '***'
ACCESS_TOKEN_SECRET = '***'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twit = 'Today\'s Date, %s, is found at %dth number after the decimal part of the π.\nHere it is 3.1415...%s_%s_%s...\nHave a good day y\'all (✿◠‿◠)✌ #PiDate' %(todays_date, index-1, before,today_str,after)
api.update_status(twit)
