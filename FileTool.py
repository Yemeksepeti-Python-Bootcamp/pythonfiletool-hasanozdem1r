"""
This script created to apply CRUD operations on CSV files.
Hasan Özdemir 2021
"""

import csv

class FileOperations:
    
    def __init__(self,path:str,fields:list) -> None:
        """
        This is a FileOperations class constructor and created to initialize important methods.
        """
        self.path=path
        self.fields=fields


    def read_csv(self):
        """
        This method is used to read all data from csv files.
        """
        # open data in read mood
        # always better to use context manager for file operations.
        with open(self.path,'r') as file:
            csv_file=csv.reader(file)
            data=list(csv_file)
        # print the data line by line
        for line in data:
            print(line)


if __name__=='__main__':
    file_obj=FileOperations('hasan.csv',[1,'Hasan','Özdemir','Computer Engineering'])
