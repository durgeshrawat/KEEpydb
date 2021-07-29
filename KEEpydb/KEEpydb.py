import openpyxl
from openpyxl import load_workbook        
import os


#CORE CLASS FOR KEEpydb DATABASE
class core:
    def create_database(self,dbname,username,password):
        self.db=openpyxl.Workbook()
        os.system('mkdir '+dbname)
        self.db.save(f'{dbname}/{username}.KEEpydb.xlsx')
        with open(f'{dbname}/dbsetups.KEEpydb','w') as f:
            f.write('0')
        with open(f'{dbname}/__configs__','w') as g:
            data=f'status=active,{username},{password}'
            g.write(data)
        return True
        
class tools:
    def CE(self,dbname,username,password):
        with open(f'{dbname}/dbsetups.KEEpydb','r') as f:
            ff=f.readlines()
            ff=ff[0]
            if ff == '0':
                os.rename(f'{dbname}/{username}.KEEpydb',f'{dbname}/{username}.KEEpydb.xlsx')
                with open(f'{dbname}/dbsetups.KEEpydb','w') as g:
                    g.write('1')
            elif ff == '1':
                os.rename(f'{dbname}/{username}.KEEpydb.xlsx',f'{dbname}/{username}.KEEpydb')
                with open(f'{dbname}/dbsetups.KEEpydb','w') as g:
                    g.write('0')

class query:
    def __init__(self,dbname,username,password):
        self.dbname=dbname
        self.username=username
        self.password=password
        self.workbook = load_workbook(filename=f'{self.dbname}/{self.username}.KEEpydb.xlsx')

    def update(self,columnANDrow,value): #append new data
        sheet = self.workbook.active
        sheet[columnANDrow] = value

    def get_cell(self,cell_no): # get perticular cell
        sheet = self.workbook.active
        return sheet[cell_no].value
        
    def get_all(self): #show whole database
        l=[]
        sheet = self.workbook.active
        for i in sheet.iter_rows(values_only=True):
            l.append(i)        
        return l

    def save(self): #save update after all updation
        self.workbook.save(filename=f'{self.dbname}/{self.username}.KEEpydb.xlsx')
          
        
                