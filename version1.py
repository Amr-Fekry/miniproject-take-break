# this program reminds the user to take a break every 2 hours by playing a song in the browser

# always remember to import modules before using functions in them
import time # ctime() gets the current time, sleep(n) makes the program hold for n number of seconds.
import webbrowser # open() opens a link in the default webbrowser

total_breaks = 3 # it is preffered to write descriptive variable names
break_count = 0
# print start time
print "program started on " + time.ctime()

while break_count < total_breaks:
    time.sleep(5) # 2*60*60 is the number of seconds in two hours
    # print time of openning the link
    print "link opened for time " + str(break_count+1) + " in " + time.ctime()
    # open the link to the song in the webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=Eox2qAjrf0U", 1)
    break_count += 1
# print program end time
print "program ended on " + time.ctime()
