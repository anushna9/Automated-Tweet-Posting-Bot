import tweepy
import fileinput
from time import sleep
CONSUMER_KEY='BRKe7wc1B3zB10h8tXyUoCToe'
CONSUMER_SECRET='PfU41s00ScIYS4gKQanSbEk8C2T1PKV11KNXXiVd95ACCAWmnT'
ACCESS_KEY='1603640872079626240-cuyzYa2oauAWrYEKCXYZXRWMBj6ix0'
ACCESS_SECRET='1YGpDRLZdktYBTN6Z41EASFMpfaJyw3Wt5iBuwwKKK8X'
auth = tweepy.OAuthHandler (CONSUMER_KEY, CONSUMER_SECRET)
auth. set_access_token (ACCESS _KEY, ACCESS_SECRET)
api = tweepy.API(auth)
my_file = open ('content. txt', 'r')
file_lines = my_file.readlines ()
my_file.close ()
for line in file lines:
  print(line)
    if line !='\n':
      api.update_status(line)
    else:
      pass
    sleep(20)
