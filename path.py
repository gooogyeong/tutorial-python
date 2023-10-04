from pathlib import Path
import os

# print(Path.cwd()) # /Users/minkyunglee/Desktop/code/python-tutorial

os.chdir('../')
# print(Path.cwd()) # /Users/minkyunglee/Desktop/code

os.chdir('python-tutorial')
# print(Path.cwd()) # /Users/minkyunglee/Desktop/code/python-tutorial

home=Path.home()
# print(home) # /Users/minkyunglee

path_a=Path('span', 'bacon', 'eggs')
# print(path_a) # span/bacon/eggs

path_b=Path('spam') / 'bacon' / 'eggs'
# print(path_b) # spam/bacon/eggs

path_c=Path('spam') / Path('bacon/eggs')
# print(path_c) # spam/bacon/eggs

path_d=Path('spam') / Path('bacon', 'eggs')
# print(path_d) # spam/bacon/eggs

# print(home.is_absolute()) # True
# print(path_b.is_absolute()) # False

path_e=Path.cwd() / 'path.py'
# print(path_e) # /Users/minkyunglee/Desktop/code/python-tutorial/path.py
# print(path_e.anchor) # /
# print(path_e.parent) # /Users/minkyunglee/Desktop/code/python-tutorial
# print(path_e.name) # path.py
# print(path_e.stem) # path
# print(path_e.suffix) # .py

# print(path_e.drive) # prints nothing (empty string?)

# print(path_e.parents[0]) # /Users/minkyunglee/Desktop/code/python-tutorial
# print(path_e.parents[1]) # /Users/minkyunglee/Desktop/code
# print(path_e.parents[2]) # /Users/minkyunglee/Desktop
# print(path_e.parents[3]) # /Users/minkyunglee
# print(path_e.parents[4]) # /Users
# print(path_e.parents[5]) # /

# print(os.path.getsize(path_e)) # 1398 (byte)
# print(os.listdir(Path.cwd())) # ['pyproject.toml', 'path.py']

# print(list(Path.cwd().glob('*'))) # [PosixPath('/Users/minkyunglee/Desktop/code/python-tutorial/pyproject.toml'), PosixPath('/Users/minkyunglee/Desktop/code/python-tutorial/path.py')]

# path=Path('hello_world.txt')
# write_result=path.write_text('Hello, World!')
# print(write_result) # 13 (characters)
# read_result=path.read_text()
# print(read_result) # Hello, World!

sonnet_file = open(Path('sonnet.txt'))
# print(sonnet_file) # <_io.TextIOWrapper name='sonnet.txt' mode='r' encoding='UTF-8'>
# print(sonnet_file.read()) 
# When, in disgrace with fortune and men's eyes,
# I all alone beweep my outcast state,
# And trouble deaf heaven with my bootless cries,
# And look upon myself and curse my fate,
# print(sonnet_file.readlines()) 
# ["When, in disgrace with fortune and men's eyes,\n", 'I all alone beweep my outcast state,\n', 'And trouble deaf heaven with my bootless cries,\n', 'And look upon myself and curse my fate,']

baconFile = open('bacon.txt', 'w')   
baconFile.write('Hello, world!\n')

baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
# print(content)
# Hello, world!
# Bacon is not a vegetable.

baconFile = open('bacon.txt', 'w')
baconFile.write('France is bacon')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
# print(content) # France is bacon

import shelve

shelfFile = shelve.open('mydata')
# print(type(shelfFile)) # <class 'shelve.DbfilenameShelf'>
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
# print(shelfFile['cats']) # ['Zophie', 'Pooka', 'Simon']s

# os.makedirs('./delicious/walnut/waffles')

# Path('new_folder/subfolder').mkdir()

print(os.path.abspath('.')) # /Users/minkyunglee/Desktop/code/python-tutorial

print (os.sep)