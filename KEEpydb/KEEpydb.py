import openpyxl
from openpyxl import load_workbook        
import os


#CORE CLASS FOR KEEpydb DATABASE
class core:
    def create_database(self,dbname,username,password):
        self.db=openpyxl.Workbook()
        os.system('mkdir '+dbname)
        try:
            self.db.save(f'{dbname}/{username}.KEEpydb.xlsx')
            with open(f'{dbname}/dbsetups.KEEpydb','w') as f:
                f.write('0')
            with open(f'{dbname}/__configs__','w') as g:
                data=f'status=active,{username},{password}'
                g.write(data)
            return True
        except:
            self.db.save(f'{dbname}\\{username}.KEEpydb.xlsx')
            with open(f'{dbname}\\dbsetups.KEEpydb','w') as f:
                f.write('0')
            with open(f'{dbname}\\__configs__','w') as g:
                data=f'status=active,{username},{password}'
                g.write(data)
            return True
            
class tools:
    def CE(self,dbname,username,password):
        with open(f'{dbname}/dbsetups.KEEpydb','r') as f:
            ff=f.readlines()
            ff=ff[0]
            try:
                if ff == '0':
                    os.rename(f'{dbname}/{username}.KEEpydb',f'{dbname}/{username}.KEEpydb.xlsx')
                    with open(f'{dbname}/dbsetups.KEEpydb','w') as g:
                        g.write('1')
                elif ff == '1':
                    os.rename(f'{dbname}/{username}.KEEpydb.xlsx',f'{dbname}/{username}.KEEpydb')
                    with open(f'{dbname}/dbsetups.KEEpydb','w') as g:
                        g.write('0')
            except:
                if ff == '0':
                    os.rename(f'{dbname}\\{username}.KEEpydb',f'{dbname}\\{username}.KEEpydb.xlsx')
                    with open(f'{dbname}\\dbsetups.KEEpydb','w') as g:
                        g.write('1')
                elif ff == '1':
                    os.rename(f'{dbname}\\{username}.KEEpydb.xlsx',f'{dbname}\\{username}.KEEpydb')
                    with open(f'{dbname}\\dbsetups.KEEpydb','w') as g:
                        g.write('0')

class query:
    def __init__(self,dbname,username,password):
        self.dbname=dbname
        self.username=username
        self.password=password
        try:
            self.workbook = load_workbook(filename=f'{self.dbname}/{self.username}.KEEpydb.xlsx')
        except:
            self.workbook = load_workbook(filename=f'{self.dbname}\\{self.username}.KEEpydb.xlsx')
        self.sheet=self.workbook.active
        
    def update(self,columnANDrow,value): #append new data
        self.sheet[columnANDrow] = value

    def get_cell(self,cell_no): # get perticular cell
        return self.sheet[cell_no].value
        
    def get_all(self): #show whole database
        l=[]
        for i in self.sheet.iter_rows(values_only=True):
            l.append(i)        
        return l

    def get_from_columns(self,column): # example column = B
        l=[]
        for i in self.sheet[column]:
            l.append(i.value)
        return l

    def get_from_range_columns(self,column_range): # column_range is in form of str and as '2:6' means from 2 to 6
        l=[]
        for i in self.sheet[column_range]:
            l.append(i.value)
        return l
        
    def get_from_rows(self,row): #example row = 5
        l=[]
        for i in self.sheet[row]:
            l.append(i.value)
        return l

    def get_from_range_rows(self,ranged_row): # example of ranged row = '3:5'
        l=[]
        for i in self.sheet[ranged_row]:
            l.append(i.value)
        return l

    def add_columns(self,idx,amount=1): #idx = index no of column will be , amount = no of columns do you want to insert in database
        self.sheet.insert_cols(idx,amount)

    def add_rows(self,idx,amount=1): #insert rows
        self.sheet.insert_rows(idx,amount)

    def delete_cell(self,cell): # example cell = a2
        self.sheet[cell]=None

    def delete_columns(self,idx,amount=1): #delete columns
        self.sheet.delete_cols(idx,amount)
        
    def search(self,searchelement): #search for values
        l=[]
        for i in self.sheet.iter_rows(values_only=True):
            l.append(i)
        for i in l:
            for j in i:
                if searchelement in i:
                    return (searchelement,i[i.index(searchelement)+1])
                    
    def delete_rows(self,idx,amoumt=1): #delete row
        self.sheet.delete_rows(idx,amount)
        
    def save(self): #save update after all updation
        try:
            self.workbook.save(filename=f'{self.dbname}/{self.username}.KEEpydb.xlsx')
        except:
            self.workbook.save(filename=f'{self.dbname}\\{self.username}.KEEpydb.xlsx')
            
            
        
                
