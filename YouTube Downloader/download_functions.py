#!/usr/bin/python3

# LIBRERIAS UTILIZADAS
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import pytube


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

    def check_video_exists(self, link: str):
        '''
        FUNCIÓN:
        Verificar la existencia de un video.

        :param str link: Link del video de YouTube.

        :return my_video: Si el video existe o False si el video no se encontró
        '''
        # Se intentará crear un objeto de tipo YouTube.
        # Si se puede crear, entonces será retornado.
        try:
            my_video = YouTube(link)
            self.video = my_video
            return my_video
        # Si surge que el link no existe o no se encuentra
        # se retornará False.
        except pytube.exceptions.RegexMatchError:
            return False

    def sort_resolutions(self, resolutions: list):
        '''
        FUNCIÓN:
        Acomoda las resoluciones de mayor a menor.

        :param resolutions: Guarda en una lista de resoluciones

        :return sorted_resolutions: Retorna las resoluciones ordenadas.
        '''
        # En esta lista se guardarán las resoluciones de mayor a menor.
        sorted_resolutions = []
        # Se quita la 'p' de cada elemento para así trabajar con
        # números enteros.
        for i in range(len(resolutions)):
            my_resolution = int(resolutions[i][:-1])
            sorted_resolutions.append(my_resolution)
        # Se acomodan los números de mayor a menor con sorted.
        sorted_resolutions = sorted(sorted_resolutions, reverse=True)
        # Luego, se vuelve a poner la 'p' nuevamente en cada elemento
        # de la lista.
        for i in range(len(sorted_resolutions)):
            sorted_resolutions[i] = str(sorted_resolutions[i]) + 'p'
        # Se regresan todas las resoluciones una vez ya se encuentren
        # ordenadas.
        return sorted_resolutions

    def get_resolutions(self, video: YouTube):
        '''
        FUNCIÓN:
        Obtener las resoluciones disponibles dado como parámetro un
        video de Youtube.

        :param YouTube video: Guarda la información respectiva del video.

        :return resolutions: Lista ordenada de mayor a menor.
        '''
        # En esta lista se guardarán las resoluciones
        # disponibles para un video.
        resolutions = []
        # Con este ciclo se identificarán cuáles son las
        # resoluciones disponibles.
        for i in video.streams:
            # Puede suceder que una resolución se repita o que aparezca como
            # 'None', si alguno de estos dos casos sucede
            # simplemente se ignorará y se procederá con el siguiente elemento.
            if str(i.resolution) in resolutions or str(i.resolution) == 'None':
                pass
            # De no presentarse el error mencionado anteriormente entonces se
            # agregará a la lista de resoluciones disponibles para un video.
            else:
                resolutions.append(str(i.resolution))
        # Se acomodan las resoluciones de menor a mayor.
        resolutions = self.sort_resolutions(resolutions)
        # Se acomodan en orden numérico las resoluciones, desde la más baja
        # hasta la más alta.
        return resolutions
