import os
import glob
import time

def countLines(path,extension) -> dict:
    numberOfLines : int = 0
    numberOfFiles : int = 0
    for file in glob.glob(os.path.join(path, '*.%s' %(extension))):
        with open( file, 'r') as f:
            numberOfFiles += 1
            content : str = f.read()
            contentList = content.split('\n')
            for i in contentList :
                if i:
                    numberOfLines += 1
    return {"numberOfLines" : numberOfLines, "numberOfFiles" : numberOfFiles,}
def main():
    inputPath = str(input('Enter the path : '))
    fileExtension :str = str(input('Enter the extension(eg: js , py etc) : ')) 
    counter : int = 0
    numberOfFiles : int = 0
    if(inputPath != None):
        allPath : list = os.listdir(path=inputPath)
        if(allPath is not None):
            for path in allPath:
                fileData :dict = countLines('%s/%s' %(inputPath,path),fileExtension)
                counter = fileData['numberOfLines']
                numberOfFiles = fileData['numberOfFiles']
            os.system('cls')
            print('Your code has : %s lines of code'%(counter))
            print('There are %s *.%s files' %(numberOfFiles,fileExtension))
            time.sleep(5)
    else:
        print('Incorrect path!!!')
        time.sleep(5)

main()




