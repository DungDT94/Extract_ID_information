import uuid
import os


folder_path = "/home/dungdinh/Documents/prj_tach_chu_cccd/data_ro/"
file_jpg = [f for f in os.listdir(folder_path) if ".jpg" in f]

for file in os.listdir(folder_path):
    absolute_file_path_jpg = folder_path + file
    file_txt = file.split('.')[0] + '.txt'
    absolute_file_path_txt = folder_path + file_txt
    name_uuid = uuid.uuid4().hex
    name_jpg = name_uuid + ".jpg"
    #name_txt = name_uuid + ".txt"
    absolute_file_path_jpg_uuid = folder_path + name_jpg
    #absolute_file_path_txt_uuid = folder_path + name_txt
    os.rename(absolute_file_path_jpg, absolute_file_path_jpg_uuid)
    #os.rename(absolute_file_path_txt, absolute_file_path_txt_uuid)

