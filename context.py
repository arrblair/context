import os
import pdb; pdb.set_trace()

hist_file_line_count = os.system('wc -l ~/.bash_history')
print hist_file_line_count 

hist_text = []
hist_text = os.system('cat ~/.bash_history')
print hist_text
print len(hist_text)
