import os
from shutil import copyfile
import re

# this script copy all sub foldered manga (volume by volume or chapter by chapter)
# and merge all manga in one file. Note that each file should be image to run


manga_source_path = "D-Frag"
manga_release_path = "release"
folder_splitter = "."  # for example ch.001 ch.002
chapter_index = 1 # ch 001 -> 001 index is 1




if __name__ == "__main__":
    
    # get folders in given directory
    wp_list = os.listdir(manga_source_path)  # returns list
    manga_index = 1
    sorted_array = list()
    
    # no need for this
    # update sub forder name (japanese letter in this case)
    for i in range(len(wp_list)):
        number = re.split(folder_splitter, wp_list[i])[chapter_index]
        new_number = number
        if len(number) == 1:
            new_number = "00" + number
        elif len(number) == 2:
            new_number = "0" + number
        replaced = wp_list[i].replace(number, new_number)
        sorted_array.append(replaced)
    
    #sorted_array.sort()  # array sorted

    index_list = [x for x in range(len(sorted_array))]
    i = 0
    min_index = 0
    
    # some sort algorith runs on parallel arrays
    while i < len(sorted_array):
        min_index = i
        j = i + 1
        while j < len(sorted_array):
            if sorted_array[index_list[min_index]] > sorted_array[index_list[j]]:
                min_index = j
            j += 1

        temp_index = index_list[i]
        index_list[i] = index_list[min_index]
        index_list[min_index] = temp_index
        i += 1
    
    # here is magic
    
    print(wp_list, "\n")
    for i in range(len(index_list)):
        chapter_path = manga_source_path + "/" + wp_list[index_list[i]]
        chapter = os.listdir(chapter_path)
        content_path = manga_source_path + "/" + wp_list[index_list[i]] + "/" + chapter[0]
        
        content_path = chapter_path
        content = chapter
        
        #content = os.listdir(content_path)
        print("content path: ", content_path)
        for j in content:
            if j != ".nomedia":
                manga_number = str(manga_index).zfill(5)
                source_path = content_path + "/" + j
                destination_path = manga_release_path + "/" + manga_number + ".jpg"
                copyfile(source_path, destination_path)
                manga_index += 1






