import os 

#where files are 
os.chdir(r"C:\Users\ND06381\Desktop\Test folder")

# what i want to be cut from the filename
chop = "-Viia7_export.csv"


# loop through directory 
for f in os.listdir():
    if f.endswith(chop):
        os.rename(f, f.replace(chop, '.csv'))
       
        
        
        
        
