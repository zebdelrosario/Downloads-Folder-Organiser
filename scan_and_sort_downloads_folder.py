import shutil
from os import walk, listdir
import datetime
import sys
import os.path
import glob


def scan_and_send_to_be_sorted():
    #   Defining all variables
    downloads_folder = r'E:\User Profile\Downloads'
    destination_audio = r'E:\Download (Auto-Sorted)\Audio'
    destination_video = r'E:\Download (Auto-Sorted)\Video Files'
    destination_images = r'E:\Download (Auto-Sorted)\Image Files'
    destination_pdf = r'E:\Download (Auto-Sorted)\PDF Files'
    destination_tobesorted = r'E:\TO BE SORTED'
    audio = '.mp3'
    video = '.mp4'
    pdf = '.pdf', '.PDF'
    image = '.jpeg', '.png', '.bmp', '.jpg'
    file_type_list = (audio, video, pdf, image)

    count = 0
    x = sorted([])
    test = 'fileName'

    #   this loop goes through downloadsFolder and check every file for the following:
    #   if it matches the list of file extensions provided
    #   if True, adds 1 to the total count for each file extension of that type
    #   then the file extension gets appended to the end of the fileName (filename + .pdf > filename.pdf)
    #   this then gets printed to the screen for every file that ends with that specified extension
    downloads_list = os.listdir(downloads_folder)
    for items in downloads_list:
        for names in file_type_list:
            if items.endswith(names):
                count += 1
                x.append(items)
    if count <= 0:
        print('No files detected; exiting...')
        exit()
    print(f'''===| {count} total items found |===
    --------------------------------------''')
    file_request = input(f'''
    ===| What files would you like to display? |===
    A)udio  files
    V)ideo  files
    P)DF    files
    I)mage  files
    X) All  files
    --------------------------------------
    ''').lower()

    #   the below for-loop is to set the fileRequest variable to a specified extension (e.g. '.pdf')
    file_count = 0
    for fileCheckRequest in file_request:
        if file_request == 'a':
            file_request = audio
        elif file_request == 'v':
            file_request = video
        elif file_request == 'p':
            file_request = pdf
        elif file_request == 'i':
            file_request = image

    #    the above for-loop will determine what files get 'selected' and printed to the screen
    #    e.g.: if a .pdf extension (user input == 'p'):
    #       the for-loop adds a 'file_count' for every .pdf-extension found within the folder
    #       the specified extension then gets set as the 'items'-variable and used for the below code
    if file_request != 'x':
        print(f'''=====| {file_request} file type selected |=====
    --------------------------------------
    ''')
        for items in downloads_list:
            if items.endswith(file_request):
                print(items)
                file_count += 1
        print(f'''
    --------------------------------------
     ==========| END OF LIST |=========
                {file_count} ITEMS FOUND''')

    elif file_request == 'x':
        print("""
    ========| ALL FILES SELECTED |========
    --------------------------------------""")
        for items in downloads_list:
            for names in file_type_list:
                if items.endswith(names):
                    print(items)
                    file_count += 1
        print(f'''
    --------------------------------------
     ==========| END OF LIST |=========
                {file_count} ITEMS FOUND''')

    user_prompt = input(f'''
    ========| What would you like to do? |========
    S)ort {file_count} items into corresponding folders
    E)xit
    ''').lower()
    if user_prompt == 's'.lower():
        for items in downloads_list:
            for names in file_type_list:
                if items.endswith(names):
                    tb_items = os.path.join(downloads_folder, items)
                    shutil.move(tb_items, destination_tobesorted)
        print(f'Sending {file_count} files to ( {destination_tobesorted} ) folder...')

    elif user_prompt == 'e':
        print('Cancelled.')
    elif user_prompt != 'e' or 's'.lower():
        print('Please input a valid command.')


def sort_to_be_sorted_folder():
    origin_folder = r'E:\TO BE SORTED'
    destination_audio = r'E:\TO BE SORTED\Audio'
    destination_video = r'E:\TO BE SORTED\Video Files'
    destination_images = r'E:\TO BE SORTED\Image Files'
    destination_pdf = r'E:\TO BE SORTED\PDF Files'
    destination_other = r'E:\TO BE SORTED\Other files'
    destination_list = [destination_images, destination_audio, destination_video, destination_pdf, destination_other]
    audio = '.mp3'
    video = '.mp4'
    pdf = '.pdf', '.PDF'
    image = '.jpeg', '.png', '.bmp', '.jpg'
    file_type_list = (audio, video, pdf, image)
    origin_list = os.listdir(origin_folder)

    for files in origin_list:
        for file_list in file_type_list:
            try:
                destination_path = os.path.join(origin_folder, files)
                if files.endswith(pdf):
                    pdf_path = destination_path
                    shutil.move(pdf_path, destination_pdf)
                if files.endswith(video):
                    video_path = destination_path
                    shutil.move(video_path, destination_video)
                elif files.endswith(audio):
                    audio_path = destination_path
                    shutil.move(audio_path, destination_audio)
                elif files.endswith(image):
                    image_path = destination_path
                    shutil.move(image_path, destination_images)
                if os.path.isdir(destination_path):
                    break
                elif files.endswith(''):
                    other_path = destination_path
                    shutil.move(other_path, destination_other)
                print(f'Files successfully sorted.')
            except:
                if WindowsError:
                    break


scan_and_send_to_be_sorted()
sort_to_be_sorted_folder()