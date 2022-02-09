from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw() # Added so Tk window doesn't appear on opening the dialog

choice=input('Enter choice\n1 for Decode\n2 for Encode \n')
path= askopenfilename() #open file select dialog from tkinter

if(path==''):
    print("err: no file selected!")
elif(not(path.endswith('.jpg'))):
    print("not jpg file")
else:
    try:
        img=open(path,'rb+')
        img.seek(0)
        byteVal=img.read()
        endSequence=b'\xff\xd9' #for png: 49 45 4e 44 ae 42 60 82
        if (choice=='1'):
            #read hidden text
            offset=(byteVal).find(endSequence) 
            if(offset!=-1):
                msgInBytes=byteVal[offset+2:]
                msg=msgInBytes.decode()
                if(msg!=''):
                    print(msg)
                else:
                    print("NOTE:-NO MESSAGE FOUND!")
        elif (choice=='2'):
            #write hidden text
            offset=(byteVal).find(endSequence)
            img.seek(offset+2)
            msg=input("Enter hidden message\n")
            byteMsg=bytes(msg,'utf-8')
            img.write(byteMsg)
            img.truncate(offset+len(endSequence)+len(byteMsg))
        else:
            print("err: bad argument!")
        img.close()
    except IOError as e:
        print(f"err:{e.strerror}")
    except Exception as e:
        print(e)