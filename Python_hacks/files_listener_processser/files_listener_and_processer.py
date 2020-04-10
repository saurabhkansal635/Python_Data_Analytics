
import os
import datetime
import time
import random

dir_path = "folder path../.. "

sleep_time = 5

def check_new_files(dir_path, t_start):
    files_list = os.listdir(dir_path)
    new_files = []
    for file_name in files_list:
        file_path = os.path.join(dir_path, file_name)
        file_stat = os.stat(file_path)
        file_created_time = datetime.datetime.fromtimestamp(file_stat.st_atime)
        if file_created_time > t_start:
            new_files.append(file_name)
    return new_files


def func1(new_files):
    if len(new_files)>0:
        processing_time = random.randrange(1, 10 ,1)
        print("processing files, wait for %s" % processing_time)
        time.sleep(processing_time)
        print("files processsed")
    else:
        pass

time_start = datetime.datetime.strptime('01-01-2020 01:00:00', '%d-%m-%Y %H:%M:%S')
new_files = check_new_files(dir_path, time_start)
func1(new_files)

try:
    while True:
        time_start = datetime.datetime.now()
        print("Time is %s, Going to bed for %s seconds" % (time_start.strftime('%d-%m-%Y %H:%M:%S'), sleep_time))
        time.sleep(sleep_time)
        print("Hey, I am awake, let's check for new files")
        new_files = check_new_files(dir_path, time_start)
        if len(new_files)>0:
            print("found new files %s" % new_files)
            func1(new_files)
        else:
            print("No new files found.....")
except KeyboardInterrupt:
    pass
