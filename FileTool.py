"""
This script created to apply CRUD operations on CSV files.
Hasan Özdemir 2021
"""

from csv import reader
from os import path

class FileOperations:
    
    def __init__(self,file_path:str,fields:list) -> None:
        """
        This is a FileOperations class constructor and created to initialize important methods.
        """
        self.path=file_path
        self.fields=fields
        # seperate file name and extension
        self.file_name,self.file_extension=path.splitext(file_path)


    def read_data(self):
        """
        This method is used to read all data from csv files.
        """
        # read csv file
        if str(self.file_extension)=='.csv':
            # open csv data in read mood
            # always better to use context manager for file operations.
            with open(self.path, newline='', mode="r") as csv_file:
                csv_data = reader(csv_file, delimiter=' ', quotechar='|')
                # print line by line
                for row in csv_data:
                    print(row)
        # read txt file
        elif str(self.file_extension)=='.txt':
            with  open(self.path,mode="r",encoding="utf-8") as file:
                for line in file:
                    print(line,end='')
        # other types
        else:
            print('Other data types is not supported for current version.')
    
    def search_data(self,search_text:str,row_number:str=0):
        """
        This method is used to search in csv file and return the all data if there is match
        """
        # read data
        csv_data = reader(open(self.path,mode="r",encoding="utf-8"),delimiter=' ', quotechar='|')
        # search and print if data is found
        for row in csv_data:
            if row[0]==search_text:
                print(row)

if __name__=='__main__':
    file_obj=FileOperations('hasan.csv',[1,'Hasan','Özdemir','Computer Engineering'])
    #file_obj.read_data()
    file_obj.search_data('Red')
