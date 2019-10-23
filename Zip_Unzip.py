import os
import zipfile
import time

lst=[]
def __zip__():
    print('1-ZIP or 2-Unzip')
    x=input()
    if x == '1':#ZIP
        print('1-File or 2-Folder')
        y=input()
        if y=='1':#FILE
            
            print('ZIP FILE path & name')
            __zip_path__ = input()

            print('Path file?')
            __file__ = input()
            
            print('1-Synchronize or 2-Add - Update Mode')
            __Update__Mode__ = input()

            if __Update__Mode__ == '1':#Synhronize
                lst.append(time.time())
                zf=zipfile.ZipFile(r''+__zip_path__+'.zip','w')
                zf.write(r''+__file__)
                zf.close()
                lst.append(time.time())
                print('{:.2f}'.format(lst[1]-lst[0])+' seconds')
                lst.clear()
                
            elif __Update__Mode__ == '2':#ADD
                lst.append(time.time())
                zf=zipfile.ZipFile(r''+__zip_path__+'.zip','a')
                zf.write(r''+__file__)
                zf.close()
                lst.append(time.time())
                print('{:.2f}'.format(lst[1]-lst[0])+' seconds')
                lst.clear()

        elif y=='2':#FOLDER
            print('ZIP path?')
            __zip_path__ = input()

            print('Folder path?')
            __zip_folder__ = input()

            lst.append(time.time())
            for r,d,f in os.walk(r''+__zip_folder__):
                for  file in f:
                    zf=zipfile.ZipFile(r''+__zip_path__+'.zip','w')
                    __path__=os.path.join(r,file)
                    try:
                        print(str(os.path.join(r,file)))
                        zf.write(__path__)
                    except:
                        print(str(os.path.join(r,file))+' ADD ZIP - NO')
                    zf.close()
            lst.append(time.time())
            print('{:.2f}'.format(lst[1]-lst[0])+' seconds')
            lst.clear()
                    
    elif x == '2':#UNZIP

        print('ZIP FILE path & name?')
        __zip__name=input()

        print('Output path from ZIP?')
        __file_output_path_from_zip__=input()

        lst.append(time.time())
        zf=zipfile.ZipFile(r''+__zip__name+'.zip')
        try:
            zf.extractall(r''+__file_output_path_from_zip__)
        except:
            print(__filename_from_zip__+' UNZIP - NO')
        zf.close()
        lst.append(time.time())
        print('{:.2f}'.format(lst[1]-lst[0])+' seconds')
        lst.clear()
__zip__()
