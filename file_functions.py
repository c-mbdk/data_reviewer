from datetime import datetime
from review_functions import source_file_dir, lookup_file_dir
import os

event_logs_dir = 'event_logs/'

# retrieving source file to process from the subdirectory
def get_source_fname():
    list_of_files = os.listdir(source_file_dir)
    for fname in list_of_files:
        if fname.endswith('.csv'):
            source_filename = source_file_dir + fname
    
    return source_filename

# user input - identify relevant lookups
def get_lookup_filename():
    lookup_files = os.listdir(lookup_file_dir)
    for fname in lookup_files:
        user_lookup_input = input(f"Should the data review include this lookup file: {fname}? (yes/no) ").lower()
        if user_lookup_input == "yes":
            filename = lookup_file_dir + fname
        elif user_lookup_input == "no":
            pass
        else:
            print("Only yes or no answers are accepted")

    return filename

# separate function to get current timestamp
def get_current_timestamp():
    timestamp_format = '%Y-%m-%d %H:%M:%S.%f'
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)

    return timestamp

# format for log message
def log(message):
    timestamp_for_log = get_current_timestamp()
    with open(f"event_logs/logfile.txt","a+") as f: 
        f.write(timestamp_for_log + ' | ' + message + '\n')

# grab filenames to archive
def identify_files_for_archive(directory):
    list_of_files = os.listdir(directory)
    files_for_archive = {}
    for fname in list_of_files:
        location = directory + fname
        if fname in files_for_archive:
            files_for_archive[fname].append(location)
        else:
            files_for_archive[fname] = '/' + location
    
    return files_for_archive

# update logfile name
def update_fname_with_timestamp(directory):
    # take eventlogs file
    # add in the name of the source file
    # add in the name of the lookup file
    # add the timestamp to the name
    list_of_files = os.listdir(directory)
    timestamp_for_fname = get_current_timestamp()
    for fname in list_of_files:
        updated_fname = '_'.join([directory,timestamp_for_fname, fname])
        old_fname = directory + fname
        os.rename(old_fname, updated_fname)
    return updated_fname


# move files to archive
def update_archive(filenames_for_archive: dict):
    current_path = os.getcwd()
    path_for_archive = '/archive/'

    for fname, fname_location in filenames_for_archive.items():
        src_path = current_path + fname_location
        new_filename = current_path + path_for_archive + fname
        os.rename(src_path, new_filename)

