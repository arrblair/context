import subprocess
import pdb; pdb.set_trace()

subprocess.call(['whoami'])
hist_file_line_count = subprocess.Popen('wc -l ~/.bash_history', stdin=None,
                                        stdout=subprocess.PIPE, shell=True,
                                        close_fds=True)
hist_file_line_count = hist_file_line_count.communicate()[0]
hist_file_line_count = hist_file_line_count.strip()
hist_file_line_count = hist_file_line_count.split(' ')[0]
print hist_file_line_count 

hist_text = []

# TODO: accomplish this task by reading each line from a file object
hist_text = subprocess.call('cat ~/.bash_history', shell=True)
print hist_text
print len(hist_text)


if __name__ == '__main__':
    main()
