import os
import zipfile
import time

class __zip_unzip_files__():
    
    def __init__(self):
        self._zip_unzip_time_=[]
        self.__start__()

    def __start__(self):
        print('1-ZIP or 2-Unzip')
        x=input()
        if x == '1':#ZIP
            self.__zip__()
        if x == '2':#UNZIP
            self.__unzip__()

    def __zip__(self):
        print('1-File or 2-Folder')
        y=input()
        if y=='1':#FILE
            print('ZIP FILE path & name')
            __zip_path__ = input()

            print('Path file?')
            __file__ = input()
            
            print('1-Synchronize or 2-Add - Update Mode')
            _Update__Mode_ = input()

            if _Update__Mode_ == '1':#Synhronize
                self._zip_unzip_time_.append(time.time())
                zf=zipfile.ZipFile(r''+__zip_path__+'.zip',mode='w')
                zf.write(r''+__file__)
                zf.close()
                self._zip_unzip_time_.append(time.time())
                print('{:.2f}'.format(self._zip_unzip_time_[1]-self._zip_unzip_time_[0])+' seconds')
                self._zip_unzip_time_.clear()
                
            elif _Update__Mode_ == '2':#ADD
                self._zip_unzip_time_.append(time.time())
                zf=zipfile.ZipFile(r''+__zip_path__+'.zip',mode='a')
                zf.write(r''+__file__)
                zf.close()
                self._zip_unzip_time_.append(time.time())
                print('{:.2f}'.format(self._zip_unzip_time_[1]-self._zip_unzip_time_[0])+' seconds')
                self._zip_unzip_time_.clear()

        elif y=='2':#FOLDER
            print('ZIP path?')
            __zip_path__ = input()

            print('Folder path?')
            __zip_folder__ = input()

            self._zip_unzip_time_.append(time.time())
            
            for r,d,f in os.walk(r''+__zip_folder__):
                for  file in f:
                    zf=zipfile.ZipFile(r''+__zip_path__+'.zip',mode='a')
                    __path__=os.path.join(r,file)
                    try:
                        print(str(os.path.join(r,file)))
                        zf.write(__path__)
                    except:
                        print(str(os.path.join(r,file))+' ADD ZIP - NO')
                    zf.close()
                    
            self._zip_unzip_time_.append(time.time())
            
            print('{:.2f}'.format(self._zip_unzip_time_[1]-self._zip_unzip_time_[0])+' seconds')
            self._zip_unzip_time_.clear()
            
    def __unzip__(self):
        print('ZIP FILE path & name?')
        __zip__name=input()

        print('Output path from ZIP?')
        __file_output_path_from_zip__=input()

        self._zip_unzip_time_.append(time.time())
        zf=zipfile.ZipFile(r''+__zip__name+'.zip')
        try:
            zf.extractall(r''+__file_output_path_from_zip__)
        except:
            print(__filename_from_zip__+' UNZIP - NO')
        zf.close()
        self._zip_unzip_time_.append(time.time())
        print('{:.2f}'.format(self._zip_unzip_time_[1]-self._zip_unzip_time_[0])+' seconds')
        self._zip_unzip_time_.clear()
        
app = __zip_unzip_files__()
