import subprocess
# import pdb; pdb.set_trace()


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

# TODO: accomplish this task by reading each line from a file object

# hist_text = subprocess.call('cat ~/.bash_history', shell=True)
with open('/Users/arrblair/.bash_history') as f:
    hist_text = f.readlines()

# hist_text = open('/Users/arrblair/.bash_history', 'r+')

print hist_text
print len(hist_text)


if __name__ == '__main__':
    main()
