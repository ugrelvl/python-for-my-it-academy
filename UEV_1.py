# Используя библиотеки os и sys напишите функцию, которая будет искать указанный файл в указанной директории
import os
import sys

def find_files(dir, f):
    found = []
    for root, dirs, files in os.walk(dir):
        found += [f_name for f_name in files if f_name == f]
    if len(found)>0:
        print(f + ' есть в папке ' + dir)

# find_files('E:\hobby\_best','Part 1.avi')
# cd 'M:\YandexDisk\YandexDisk\_ИМиФ\Повышение квалификации\Python'
# python GorokhovSB_Tasks_5_1.py dir='E:\hobby\_best' f='Part 1.avi'
# python GorokhovSB_Tasks_5_1.py 'E:\hobby\_best' 'Part 1.avi'

