import os
import time
path = input('Enter the path of the file:  ')
days = int(time.time_ns() * 2.7778e-13 * 0.0416667)
path_exist = os.path.exists(path)

if path_exist == True:
    files = os.listdir(path)
    for docs in files:
        name, ext = os.path.splitext(docs)
        path_of_doc = path + '/' + name + ext
        ctime = int(os.stat(path_of_doc).st_ctime_ns * 2.7778e-13 * 0.0416667)

        if days - ctime == 30 or days > ctime:
            print('file name: ' + name, ext)
            print('Are you sure you want to delete this? Type yes or no')
            delete_input = input(': ')
            if delete_input == 'YES' or delete_input == 'yes':
                os.remove(path_of_doc)
            else:
                print('Alright')
        else:
            print('You have created this file today and - ' + name + ext)   
else:
    print(' The path does not exist ')