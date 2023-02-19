#!/usr/bin/python3

# LIBRERIAS UTILIZADAS
import tkinter as tk
import download_functions as df


class Window():
    def __init__(self):
        # Se crea un objeto de tipo Tkinter, este será por así decirlo nuestro
        # root en donde guardaremos todas las posibles configuraciones.
        self.root = tk.Tk()
        # Se crea un objeto de tipo Download Functions para posteriormente
        # utilizar algunas funciones útiles dentro del root.
        utilities = df.Functions(self.root)
        # Se le otorga una geometría en específico.
        self.root.geometry('600x350')
        # Se aplica este comando para que el tamaño no sea modificable.
        self.root.resizable(0, 0)
        # Se otorga un título a la ventana.
        self.root.title('YouTube Video Downloader for Ubuntu')
        # Se carga la foto de la aplicación.
        app_logo = tk.PhotoImage(file='app_logo.png')
        # Establecer la imagen de icono de la aplicación.
        self.root.iconphoto(False, app_logo)
        # Se agregan algunos textos dentro de la ventana.
        tk.Label(self.root, text='YouTube Downloader',
                 font='roboto 22 bold').pack()
        tk.Label(self.root, text=('ADVERTENCIA: Desactive el antivirus '
                                  'para que la descarga se de'
                                  ' correctamente.'),
                 font='roboto 9').place(x=50, y=157)
        tk.Label(self.root, text='Inserte el enlace aquí: ',
                 font='roboto 15').place(x=175, y=102)
        # Se cree una ventana de texto en donde escribir el link del video.
        link = tk.Entry(self.root, width=70,
                        highlightthickness=3,
                        highlightbackground='#ff0068',
                        highlightcolor='#ff0068')
        link.place(x=15, y=130)
        # Se crea un botón para comenzar la descarga.
        start_button = tk.Button(self.root, text='Comenzar', font='roboto 15',
                                 bg='#ff0068', foreground='white', padx=2,
                                 command=lambda:
                                 utilities.start_download(link))
        start_button.place(x=230, y=190)
        # El root debe encontrarse en un loop para así correr el programa.
        self.root.mainloop()
