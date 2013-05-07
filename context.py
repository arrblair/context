import subprocess
import collections
import time
# import pdb; pdb.set_trace()


# TODO(arrblair): profile this script at somepoint & make it sing
# start = 


class Context():
    def __init__(self):
        self.whoami = self.get_user_name()

    # determine who you're using the device as
    def get_user_name(self):
        whoami = subprocess.Popen('whoami', stdin=None, stdout=subprocess.PIPE,
                                  shell=True, close_fds=True)
        whoami = whoami.communicate()[0]
        if '\n' in whoami:
            newline_index = whoami.find('\n')
            whoami = whoami[:newline_index]
            return whoami


    # determine how long the history file is
    def hist_line_counter(self):
        hist_line_count = subprocess.Popen('wc -l ~/.bash_history', stdin=None,
                                                stdout=subprocess.PIPE, shell=True,
                                                close_fds=True)
        hist_line_count = hist_line_count.communicate()[0]
        hist_line_count = hist_line_count.strip()
        hist_line_count = hist_line_count.split(' ')[0]
        print hist_line_count 

    # hist_text = subprocess.call('cat ~/.bash_history', shell=True)
    def read_history_file(self):
        # import pdb; pdb.set_trace()
        hist_text = []
        with open('/Users/%s/.bash_history' % self.whoami) as f:
            hist_text = f.readlines()
            i=1
            for element in hist_text:
                if element.startswith('#1'):
                    # print i
                    # print element
                    hist_text.remove(element)
                    i+=1
                else:
                    # print 'DOES NOT START WITH #1: VERY GOOOD'
                    # print i
                    # print element
                    i+=1
            return hist_text 


    # add element in hist_text to collection counter
    def create_collection_counter(self):
        c = collections.Counter()
        i=1
        print type(self.read_history_file)
        for element in self.read_history_file():
            print i
            print element
            c.update(element.split())
            i+=1
        return c


    # create a sorted list from hist_text 
    def sort_collection(self):
        sorted_tallies = []
        sorted = []
        collection_counter = self.create_collection_counter() 
        for k, v in collection_counter.iteritems():
            sorted_tallies.append((str(v) + ': ' + k))
        print sorted_tallies
        print 8*'\n', 100*'L'
        print 'PRINT SORTED TALLIES RAN (LINE 74)'
        for element in sorted_tallies:
            print element
        print 8*'\n', 100*'M'
        print 'PRINT ELEMENT IN SORTED TALLIES LOOP HAS RAN'
        return sorted_tallies 


    def sorter_dict(self):
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


contx = Context()


# whoami = get_user_name()
contx.get_user_name()


# hist_text = read_history_file()
contx.read_history_file()


# c = create_collection_counter()
contx.create_collection_counter()


# sorted_tallies = sort_collection()
contx.sort_collection()

print 'History contains ' + str(len(contx.read_history_file())) + ' entries.'


# if __name__ == '__main__':
    # main()
