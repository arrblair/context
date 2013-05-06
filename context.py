import subprocess
import collections
import time
# import pdb; pdb.set_trace()

# TODO(arrblair): profile this script at somepoint & make it sing
# start = 


# determine who you're using the device as
def get_user_name():
    whoami = subprocess.Popen('whoami', stdin=None, stdout=subprocess.PIPE,
                              shell=True, close_fds=True)
    whoami = whoami.communicate()[0]
    if '\n' in whoami:
        newline_index = whoami.find('\n')
        whoami = whoami[:newline_index]
        return whoami

whoami = get_user_name()

# determine how long the history file is
def hist_line_counter():
    hist_line_count = subprocess.Popen('wc -l ~/.bash_history', stdin=None,
                                            stdout=subprocess.PIPE, shell=True,
                                            close_fds=True)
    hist_line_count = hist_line_count.communicate()[0]
    hist_line_count = hist_line_count.strip()
    hist_line_count = hist_line_count.split(' ')[0]
    print hist_line_count 

# hist_text = subprocess.call('cat ~/.bash_history', shell=True)
def read_history_file():
    # import pdb; pdb.set_trace()
    hist_text = []
    with open('/Users/%s/.bash_history' % whoami) as f:
        hist_text = f.readlines()
        i=1
        for element in hist_text:
            if element.startswith('#1'):
                print i
                print element
                hist_text.remove(element)
                i+=1
            else:
                print 'DOES NOT START WITH #1: VERY GOOOD'
                print i
                print element
                i+=1
        return hist_text 

hist_text = read_history_file()

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
sorted = []
for k, v in c.iteritems():
    sorted_tallies.append((str(v) + ': ' + k))

print sorted_tallies

# this is just printing the unordered elements in sorted_tallies, 1 per line
for element in sorted_tallies:
    print element

# this takes sorted tallies and makes them sortable
sorter_dict = {}
for element in sorted_tallies:
    colon_index = element.find(':')
    # slice_number = colon_index - 1
    slice_number = colon_index
    if slice_number == 0:
        number = int(element[0])
    else:
        number = int(element[0:slice_number])
    slice_number = slice_number + 2
    element = element[slice_number:]
    sorter_dict[number] = element

print 'History contains ' + str(len(hist_text)) + ' entries.'

#
# if __name__ == '__main__':
    # main()
