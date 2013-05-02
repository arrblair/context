import subprocess
import pdb; pdb.set_trace()

subprocess.call(['whoami'])
hist_file_line_count = subprocess.call('wc -l ~/.bash_history', shell=True)
print hist_file_line_count 

hist_text = []
hist_text = subprocess.call(['cat ~/.bash_history'])
print hist_text
print len(hist_text)


if __name__ == '__main__':
    main()
