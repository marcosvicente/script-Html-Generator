#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

def createPathHtml(name):
    os.mkdir(name)
    return print("Create Path "+name+" ........ok")

def createPathCss(name):
    os.mkdir(name +"/css/")
    return print("Create Path "+name+"/css/ ...ok")


def createPathJs(name):
    os.mkdir(name +"/js/")
    return print("Create Path "+name+"/js/ ....ok")

def createFile(name, type, file):
    if type == 'css':
        f = open(name +'/'+ '/'+type+'/' + file+'.css',  "a")
        f.write('// create file' + file)
        f.close()
        print(name + '/'+type+'/' + file+'.css ........ ok')

    elif type == 'js':
        f = open(name +'/'+ '/'+type+'/' + file+'.js',  "a")
        f.write('// create file' + file)
        f.close()
        print(name + '/'+type+'/' + file+'.js ........ ok')
    else:
        print('It is happend a problem')

def main():
    name = sys.argv[1]
    type = sys.argv[2]
    file = sys.argv[3]
    if (type == 'css') or (type == 'js'):
        createFile(name, type, file)

    else:
        if os.path.exists(name):
            return print("Path exists")
        else:
            createPathHtml(name)
            createPathCss(name)
            createPathJs(name)

if __name__ == '__main__':
    main()
