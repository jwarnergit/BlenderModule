'''
-- Saved Blender Commands
sys.path.append(os.path.dirname(bpy.data.filepath))
import sys, os; sys.path.append(os.path.dirname(bpy.data.filepath)); import texture_painter
import importlib; importlib.reload(texture_painter)
import importlib; importlib.reload(texture_painter); texture_painter.go()
texture_painter.go()

'''
import csv
import os
import codecs

def get_backers(csv_filename):
    with codecs.open(csv_filename, 'r', 'utf-8-sig') as stream:
        iterable = csv.reader(stream)
        header = next(iterable)
        for row in iterable:
            backer = dict(zip(header, row))
            yield backer;

def go():
    print(os.getcwd())
    filename = '..\\..\\..\\dev\\repos\\blender\\BlenderModule\\dat\\backers_10.csv'
    print(filename);
    for backer in get_backers(filename):
        print(backer)
