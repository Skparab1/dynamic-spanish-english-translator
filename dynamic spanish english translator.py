import shelve
def shelvewrite(textfilename,towrite): #write to text file
    textfilenametxt = textfilename + '.txt'
    writer = shelve.open(str(textfilenametxt))
    writer[str(textfilename)] = towrite
    writer.close()
def shelveread(textfilename): # read form text file
    textfilenametxt = textfilename + '.txt'
    reader = shelve.open(str(textfilenametxt))
    text = reader[str(textfilename)]
    reader.close()
    return text

def string_splitter(toread):
    if True:
        fish = toread
        num = 0
        reader = 'start'
        first, second = '',''
        try:
            while True:
                reader = fish[num]
                while reader != ' ':
                    first = first + reader
                    num += 1
                    reader = fish[num]
                num += 1
                if first != '':
                    break
        except:
            print('')
        try:
            while True:
                reader = fish[num]
                while reader != ' ':
                    second = second + reader
                    num += 1
                    reader = fish[num]
                num += 1
                if second != '':
                    break
        except:
            print('')
            
    return first,second    
    
try:
    englishlist = shelveread('dynamictranslatorstorage-english')
    spanishlist = shelveread('dynamictranslatorstorage-spanish')
except:
    shelvewrite('dynamictranslatorstorage-english',[])
    shelvewrite('dynamictranslatorstorage-spanish',[])
    englishlist,spanishlist = [],[]

print('\n'*50)

while True:

    englishlist = shelveread('dynamictranslatorstorage-english')
    spanishlist = shelveread('dynamictranslatorstorage-spanish')

    print('\nTo retrive an entry, type it. to define an entry, type spanishword = englishword')
    inp = input('> ')
    if '=' in inp:
        
        inp = inp.replace(' = ',' ')
        inp = inp.replace(' =',' ')
        inp = inp.replace('= ',' ')
        inp = inp.replace('=',' ')

        spanishword, englishword = string_splitter(inp)

        spanishlist.append(spanishword)
        englishlist.append(englishword)

    else:
        
        if inp in englishlist:
            
            i = 0
            content = ''

            while content != inp:
                content = englishlist[i]
                i += 1
            
            print(spanishlist[i-1])

        elif inp in spanishlist:
            
            i = 0
            content = ''

            while content != inp:
                content = spanishlist[i]
                i += 1
            
            print(englishlist[i-1])
        
        else:
            print('entry not found')

    shelvewrite('dynamictranslatorstorage-english', englishlist)
    shelvewrite('dynamictranslatorstorage-spanish', spanishlist)
