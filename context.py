import os

hist_file_line_count = os.system('wc -l .bash_history')
print hist_file_line_count 

hist_text = os.system('cat .bash_history')
print hist_text
