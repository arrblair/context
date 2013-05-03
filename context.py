import subprocess
import collections
import time
# import pdb; pdb.set_trace()


# start = 


# determine who you're using the device as
whoami = subprocess.Popen('whoami', stdin=None, stdout=subprocess.PIPE,
                          shell=True, close_fds=True)
whoami = whoami.communicate()[0]
print whoami

# determine how long the history file is
hist_file_line_count = subprocess.Popen('wc -l ~/.bash_history', stdin=None,
                                        stdout=subprocess.PIPE, shell=True,
                                        close_fds=True)
hist_file_line_count = hist_file_line_count.communicate()[0]
hist_file_line_count = hist_file_line_count.strip()
hist_file_line_count = hist_file_line_count.split(' ')[0]
print hist_file_line_count 

hist_text = []


# hist_text = subprocess.call('cat ~/.bash_history', shell=True)
with open('/Users/arrblair/.bash_history') as f:
   hist_text = f.readlines()

i=1
for element in hist_text:
    if element.startswith('#1'):
        # print i
        # print element
        hist_text.remove(element)
        # i+=1


# hist_text = open('/Users/arrblair/.bash_history', 'r+')

# add element in hist_text to collection counter
c = collections.Counter()
i=1
for element in hist_text:
    print i
    print element
    c.update(element.split())
    i+=1


# create a sorted list from hist_text 
sorted_tallies = []
for k, v in c.iteritems():
    sorted_tallies.append((str(v) + ': ' + k))
    sorted = sorted_tallies.sort()

print sorted_tallies

print sorted

for element in sorted_tallies:
    print element

for element in sorted:
    print element

print 'History contains ' + str(len(hist_text)) + ' entries.'


# if __name__ == '__main__':
    # main()
