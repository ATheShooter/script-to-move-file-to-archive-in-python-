import os
import shutil
import time 
import dateparser
import  datetime 
from dateutil.relativedelta import relativedelta


# the folder that  you want to move file out from
path_to_watch = os.path.abspath("\\Users\\looki\\Downloads")

# the folder you want to move the file into 
path_to_moveto = os.path.abspath("\\Users\\looki\\Downloads\\Archive")

# the period in month for the file that you want to move to archive 
_months = 3


class MovingFiles:
            def __init__(self,file_name = None,):
                if(file_name != None):
                    info = os.stat(file_name)
                    self.Mode = oct(info.st_mode)
                    self.Created = datetime.datetime.strptime(time.ctime(info.st_mtime),"%a %b %d %H:%M:%S %Y")
                    self.Accessesd = datetime.datetime.strptime(time.ctime(info.st_atime),"%a %b %d %H:%M:%S %Y")
                    self.Modified = datetime.datetime.strptime(time.ctime(info.st_mtime),"%a %b %d %H:%M:%S %Y")
            def moveFile(self,period = _months):
                three_month_ago = datetime.datetime.now() + relativedelta(months=-period)
                #print(three_month_ago)
                if (not(self.Accessesd  >= three_month_ago ) and not(self.Created >= three_month_ago)):
                    try:
                            shutil.move(file,path_to_moveto)
                            print(file)
                    except:
                            print("File with same name  already exist")
            def startMoving(self,path_to_watch, path_to_moveto):
                for root, dirs, files in os.walk(path_to_watch, topdown=False):
                    for name in files:
                        #print(name)
                        temp_move_file = MovingFiles(os.path.join(root, name))
                        temp_move_file.moveFile()
                    for name in dirs:
                        #print(name)
                        temp_move_file = MovingFiles(os.path.join(root, name))
                        temp_move_file.moveFile()

                    

def main():
    moving_files = MovingFiles() 
    moving_files.startMoving(path_to_watch, path_to_moveto)


if __name__ == "__main__":
    main()
