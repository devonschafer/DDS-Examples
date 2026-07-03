#DevonDataStructure
import os


class DDS():

    #reads entire file contents when 'all' as option
    #t = DDS.readFile('testdata.dds', 'all', None)
    def readFile(filename, option, values):
        openFile = open(filename, 'r')
        if option == 'all' and values == None:
            readFile = openFile.read()
            return readFile
        openFile.close()

    #return specific line, key and values, when line number as option, starting with 1
    #t = DDS.returnLine('testdata.dds', 3, None)
    def returnLine(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, int) and values == None:
            line = openFile.readlines()
            return line[option-1]
        openFile.close()

    #return a key when line number or 'value' as option
    #t = DDS.returnKey('testdata.dds', 3, 'key')
    #t = DDS.returnKey('testdata.dds', 'north', 'key')
    def returnKey(filename, option, values):
        openFile = open(filename, 'r')

        if isinstance(option, str) and values == 'key':
            line = openFile.readlines()
            for lines in line:
                if option in lines:
                    value = lines.split('::')
                    return value[0]
                
        elif isinstance(option, int) and values == 'key':
            line = openFile.readlines()
            line = line[option-1].split('::')
            return line[0]
        openFile.close()

    #return several keys when tuple of line numbers as option, starting with 1
    #t = DDS.returnMultipleKeys('testdata.dds', (1,3), 'key')
    #returns exact lines, can not be zero, starts at one, zero return None
    def returnMultipleKeys(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, tuple) and 0 not in option and values == 'key':
            i = []
            line = openFile.readlines()
            for k in range((option[0]-1), option[1]):
                skey = line[k].split('::')
                i.append(skey[0])
            return i
        openFile.close()

    #return a value when line number or 'key' as option
    #t = DDS.returnValue('testdata.dds', 3, 'value')
    def returnValue(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, str) and values == 'value':
            line = openFile.readlines()
            for lines in line:
                if lines.startswith(option):
                    value = lines.split('::')
                    return value[1]
        elif isinstance(option, int) and values == 'value':
            line = openFile.readlines()
            line = line[option-1].split('::')
            return line[1]
        openFile.close()

    #return a list of values when line number as option
    #t = DDS.valuesToList('testdata.dds', 3, 'value')
    def valuesToList(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, int) and values == 'value':
            line = openFile.readlines()
            line = line[option-1].split('::')
            v = line[1].split(',,')
            return v
        openFile.close()

    #if multiple values, return specific value when tuple as option (line number,value index)(starting with 1 not 0)
    #t = DDS.returnSpecificValue('testdata.dds', (3,2), 'value')
    def returnSpecificValue(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, tuple) and values == 'value':
            line = openFile.readlines()
            line = line[option[0]-1].split('::')
            opt = line[1].split(',,')
            return opt[option[1]-1]
        openFile.close()

    #append line to end of file when string::string as option
    #t = DDS.appendFile('testdata.dds', 'Hello::World', 'save')
    def appendFile(filename, option, values):
        saveFile = open(filename, 'a')
        if isinstance(option, str) and values == 'save':
            saveFile.write('%s\n' % option)
        saveFile.close()

    #make a append value to file specific line function
        
    '''#make a search key, return value function. option1=searched item, option2=tuple of line numbers(1,8)
    #t = DDS.searchByKey('testdata.dds', 'Hello', (1,8))
    def searchByKey(filename, option1, option2):
        openFile = open(filename, 'r')
        if isinstance(option1, str) and isinstance(option2, tuple):
            key = DDS.readMultipleKeys(filename, option2, 'key')
            print(option1)
            if option1 in key:
                print(key)
                #value = DDS.readValue(filename, 3, 'value')

                

    #make a search value, return key function'''
            
            
    
            
#t = DDS.readFile('testdata.dds', 'all', None)
#t = DDS.returnLine('testdata.dds', 3, None)
#t = DDS.returnKey('testdata.dds', 3, 'key')
#t = DDS.returnKey('testdata.dds', 'This works', 'key')
#t = DDS.returnMultipleKeys('testdata.dds', (1,8), 'key')
#t = DDS.returnValue('testdata.dds', 3, 'value')
#t = DDS.returnValue('testdata.dds', 'latte', 'value')
#t = DDS.valuesToList('testdata.dds', 3, 'value')
#t = DDS.returnSpecificValue('testdata.dds', (3,4), 'value')
#t = DDS.appendFile('testdata.dds', 'Testing Again::This is working', 'save')
#t = DDS.searchByKey('testdata.dds', 'Hello', (1,8))
#print(t)
    
