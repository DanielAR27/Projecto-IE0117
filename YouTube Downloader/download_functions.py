#!/usr/bin/python3

# LIBRERIAS UTILIZADAS
import tkinter as tk
from tkinter import messagebox


class Messages():
    def __init__(self, misc: tk.Tk):
        '''
        INICIALIZADOR:
        Se inicializa la clase Messages.

        :param tkinter misc: El root principal de la ventana en Tkinter.
        '''
        self.misc = misc

    def advice_choose_location(self):
        '''
        FUNCIÓN:
        Mensaje de aviso de elegir una dirección.
        '''
        messagebox.showinfo('Advertencia', ('Debe elegir una dirección'
                                            ' donde guardar su video.'))

    def advice_nonexistent_location(self):
        '''
        FUNCIÓN:
        Mensaje de aviso si una dirección no existe.
        '''
        messagebox.showinfo('Advertencia', ('La dirección no se ha '
                                            'encontrado,'
                                            'intente otra dirección.'))

    def successful_download(self):
        '''
        FUNCIÓN:
        Mensaje de aviso de descarga completada.
        '''
        messagebox.showinfo('Descarga Completada',
                            'Su descarga ha sido exitosa.')

    def no_audio_download(self):
        """
        FUNCIÓN:
        Mensaje de aviso de descarga completada, pero con posible
        error de audio.
        """
        messagebox.showinfo('Descarga Completada',
                            'La resolución pudo haber afectado el audio, '
                            'se recomienda elegir otra resolución.')

    def error_download(self):
        """
        FUNCIÓN:
        Mensaje de aviso de descarga no exitosa (Si el video es muy largo
        puede dar problemas con la descarga).
        """
        messagebox.showinfo('Advertencia',
                            'Hubo un problema con su descarga, intente '
                            'de nuevo más tarde.')

    def advice_chose_type(self):
        """
        FUNCIÓN:
        Mensaje de aviso para elegir un tipo de formato general.
        """
        messagebox.showinfo('Advertencia', 'Debe elegir un formato de video.')

    def advice_chose_resolution(self):
        """
        FUNCIÓN:
        Mensaje de aviso para elegir una resolución.
        """
        messagebox.showinfo('Advertencia',
                            'Debe elegir una resolución.')

    def advice_chose_file_type(self):
        """
        FUNCIÓN:
        Mensaje de aviso para elegir un formato de archivo.
        """
        messagebox.showinfo('Advertencia',
                            'Debe eligir un formato de archivo.')

    def advice_nonexistent_link(self):
        """
        FUNCIÓN:
        Mensaje de aviso para corregir el link.
        """
        messagebox.showinfo('Advertencia', ('Ha ocurrido un error, '
                                            'verifique que puso bien su '
                                            'link.'))


class Functions():
    def __init__(self, misc: tk.Tk):
        """
        INICIALIZADOR:
        Se inicializa la clase Functions.

        :param tkinter misc: El root principal de la ventana en Tkinter.
        """
        # Nombre del video / archivo
        # por defecto, este se encontrará vacío.
        self.file_name = ''
        # Nombre de la dirección, por defecto
        # este se encontrará vacío.
        self.location = ''
        # Nombre del tipo de formato (Video/Audio)
        # por defecto, este se encontrará vacío.
        self.type = ''
        # Nombre de la resolución, por defecto
        # este se encontrará vacío.
        self.resolution = ''
        # Nombre del tipo de archivo, por defecto
        # este se encontrará vacío.
        self.file_type = ''
        # Se debe guardar la root.
        self.misc = misc
        # Se debe crear un objeto de tipo "YouTube", por defecto
        # este será el valor de NOne.
        self.video = None
        # Se crea un notificador de mensajes con la ayuda de la clase Messages.
        self.notifier = Messages(misc)
