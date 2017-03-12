import os
import random

def init_lists(folder):
    a_list = []
    file_list = os.listdir(folder)
    for a_file in file_list:
        f = open(folder + a_file, 'r')
        a_list.append(f.read())
    f.close()
return a_list



spam = init_lists('enron1/spam/')
ham = init_lists('enron1/ham/')

all_emails = [(email, 'spam') for email in spam]
all_emails += [(email, 'ham') for email in ham]

random.shuffle(all_emails)