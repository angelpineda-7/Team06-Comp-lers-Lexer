import PySimpleGUI as sg


class GUI:
    def elegir(self):
        opcion=0
        sg.theme("DarkGrey5")
        layout=[[sg.Text("Please select a file to perform a Lexical Analysis to.\nSupports int, bool, for and if structures")],[sg.Text()],[sg.Button("Select file")],[sg.Exit()]]
        ventana=sg.Window("Lexer",layout,finalize="true")
        while True:
            event,values=ventana.read()
            if event in (None, "Exit"):
                opcion=0
                break
            elif event in (None,"Select file"):
                opcion=1
                break
           
        ventana.close()
        return opcion
    
    def mensaje(titulo,mensaje):
        sg.theme("DarkGrey5")
        layout=[[sg.Text(mensaje)],[sg.Exit()]]
        ventana=sg.Window(titulo,layout,finalize="true")
        while True:
            event,values=ventana.read()
            if event in (None, "Exit"):
                break
        ventana.close()
