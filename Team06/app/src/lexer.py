keywords={"int","for","if","bool","true","false"}
operators={"+","-","*","/","=","<",">"}
punctuations={".",'"',",",";",":","(",")","{","}"}

from gui import GUI
import tkinter as tk
from tkinter import filedialog

    
def lexer(file_path):
    countKeywords=0
    countOperators=0
    countIdentificators=0
    countConstants=0
    countPunctuation=0
    file=open(file_path,"r")
    lines=file.readlines()
    message=""
    lineCounter=0
    for line in lines:
        lineCounter=lineCounter+1
        lineLexer=""
        currentToken=""
        line=line.strip()
        for i,char in enumerate(line):
            if char==" ":
               continue
            if char in operators:
                countOperators=countOperators+1
                lineLexer=lineLexer+"Operator "
                currentToken=""
                continue
            if char in punctuations:
                countPunctuation=countPunctuation+1
                lineLexer=lineLexer+"Punctuation "
                currentToken=""
                continue
            currentToken=currentToken+char
            if currentToken in keywords:
                countKeywords=countKeywords+1
                lineLexer=lineLexer+"Keyword "
                currentToken=""
                continue
            elif i+1<len(line):
                if line[i+1] in operators or line[i+1] in punctuations or line[i+1]==" ":
                    if currentToken.isnumeric():
                        countConstants=countConstants+1
                        lineLexer=lineLexer+"Constant "
                        currentToken="" 
                    else:
                        countIdentificators=countIdentificators+1
                        lineLexer=lineLexer+"Identificator "
                        currentToken="" 
        message=message+f'Line {lineCounter}: {line}\nAnalysis:{lineLexer}\n\n' 
        print(line, " ",lineLexer)
    message=message+f'\nTokens:\nKeywords: {countKeywords}\nIdenticators: {countIdentificators}\nConstants: {countConstants}\nOperators: {countOperators}\nPunctuation: {countPunctuation}\n\nTotal: {countPunctuation+countConstants+countIdentificators+countKeywords+countOperators}'
    GUI.mensaje("Lexer",message)


def main():
    gui=GUI()
    opcion=gui.elegir()
    if opcion==1:
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        if file_path.endswith(".c"):
            print(file_path)
            lexer(file_path)
        elif file_path=="":
            gui.mensaje("Error","Archivo no seleccionado")
            main()
        else:
            gui.mensaje("Error","Archivo no soportado")
            main()
main()