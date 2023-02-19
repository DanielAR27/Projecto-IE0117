#!/usr/bin/python3

# LIBRERIAS UTILIZADAS
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from pytube import YouTube
import pytube
from PIL import Image, ImageTk
import urllib.request
import io
import os


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

    def get_thumbnail(self, link):
        """
        FUNCIÓN:
        Obtener el thumbnail de una imagen en base a su link sin tener
        que descargarla.
        :param link: Link de la imagen del video de YouTube.
        :return picture: La imagen del video.
        """
        # Se lee la información de la imagen con la librería url lib requist.
        with urllib.request.urlopen(link) as my_request:
            raw_data = my_request.read()
        # Se abre la imagen en base a la data recolectada.
        link_thumbnail = Image.open(io.BytesIO(raw_data))
        # Se hace la imagen más pequeña para que esta pueda
        # caber en la ventana.
        link_thumbnail = link_thumbnail.resize((160, 130))
        # Se transforma la imagen en el formato adecuado.
        picture = ImageTk.PhotoImage(link_thumbnail)
        return picture

    def title_fits(self, video_title):
        """
        FUNCIÓN:
        Con esta función se verifica que el texto pueda alcanzar el
        espacio para así poder acomodarlo según su longitud.

        :param video_title: Título del video.

        :return: True si el título se excede y False si no se excede.
        """
        # Lista donde se despliegará el texto según los espacios.
        list_texto = video_title.split(' ')
        # String que será usado como prueba para medir los caracteres.
        str_measure = ''
        # Variable donde se guardará el index de donde se
        # debe separar el texto.
        max_index = 0

        for i in range(len(list_texto)):
            # Si es la primer palabra, no se debe agregar espacio.
            if i == 0:
                str_measure = str_measure + list_texto[i]
            # Cualquier otra palabra sí debe tener espacio.
            else:
                str_measure = str_measure + ' ' + list_texto[i]

            # Si la longitud del texto supera los 70 caracteres entonces se
            # ejecutará el siguiente bloque de código.
            if len(str_measure) > 70:
                # Se debe separar el texto en donde existan espacios.
                nuevo_texto = str_measure.split(' ')
                # La última palabra es la que está causando el problema, por
                # que la longitud quedará hasta la penúltima palabra.
                max_index = len(nuevo_texto) - 1
                break

        # Si la variable cambia es por que el texto supera el número máximo de
        # caracteres permitidos.
        if max_index != 0:
            first_list = list_texto[:max_index]
            second_list = list_texto[max_index:]
            tk.Label(self.misc, text=' '.join(first_list),
                     font='arial 10').place(x=52, y=140)
            tk.Label(self.misc, text=' '.join(second_list),
                     font='arial 10').place(x=10, y=160)
            return True
        # De no ser así, simplemente se pondrá el título por defecto.
        else:
            tk.Label(self.misc, text=video_title,
                     font='arial 10').place(x=55, y=140)
            return False

    def set_file_type(self, event):
        """
        FUNCIÓN:
        Se escoge el tipo de formato de archivo.

        :param event: Guarda el tipo de formato en una variable.
        """
        # Se obtiene la respuesta del tipo de formato.
        self.file_type = event.widget.get()

    def erase_widgets(self, maximum: int):
        """
        FUNCIÓN:
        Borrar todos los widgets después de cierto número.

        :param int maximum: número máximo de widgets.
        """
        # Se obtienen todos los elementos dentro del root.
        wlist = self.misc.winfo_children()
        # Si la longitud de elementos es mayor al máximo que se busca,
        # entonces se van a eliminar
        if len(wlist) != maximum:
            # Se guarda en una variable la cantidad de veces a iterar por cada
            # elemento adicional que exista.
            ite_var = len(wlist) - maximum
            wlist.reverse()
            for i in range(ite_var):
                wlist[i].destroy()
        return wlist

    def type_choice(self, event, resolutions: list, exceeding: bool):
        """
        FUNCIÓN:
        Se escoge el tipo de formato de video.

        :param list resolutions: lista de resoluciones.
        :param bool exceeding: booleano que indica si se sobrepasó.
        """
        # Se obtiene la respuesta del tipo de formato.
        self.type = event.widget.get()
        # Estos datos deben ser vaciados para que no haya
        # problemas luego al descargar.
        self.file_type = ''
        self.resolution = ''
        # Si el título del video se excedió de caracteres, los elementos en la
        # ventana serán un total de 12.
        if exceeding is True:
            elements = 13
        # Si el título no se excedió, los elementos en la
        # ventana serán un total de 11.
        else:
            elements = 12
        # Si el formato es de video entonces se ejecutará todo el siguiente
        # bloque de código.
        if self.type == 'Video':
            # Si hay más de 11 o 12 widgets, todas las añadidas recientemente
            # serán eliminadas.
            # Esto se hace debido a que se crean varias copias y esto puede
            # sobrecargar la aplicación.
            self.erase_widgets(elements)
            # Se crea una caja para decidir la resolución de
            # video que se quiere.
            resolutions_cb = ttk.Combobox(self.misc, values=resolutions)
            tk.Label(self.misc, text='Resolución').place(x=200, y=10)
            resolutions_cb.place(x=200, y=40)
            resolutions_cb.bind('<<ComboboxSelected>>', lambda event:
                                self.resolution_choice(event, exceeding))
        # Si el formato es de audio entonces se ejecutará todo el siguiente
        # bloque de código.
        else:
            # Si hay más de 11 widgets, todas las añadidas
            # recientemente serán eliminadas.
            # Esto se hace debido a que se crean varias copias y esto puede
            # sobrecargar la aplicación.
            self.erase_widgets(elements)
            # Se crea una variable en donde guardar el formato de archivo.
            file_types_cb = ttk.Combobox(self.misc, values='mp3')
            tk.Label(self.misc, text='Formato de archivo').place(x=200, y=10)
            file_types_cb.place(x=200, y=40)
            file_types_cb.bind('<<ComboboxSelected>>', lambda event:
                               self.set_file_type(event))

    def resolution_choice(self, event, exceeding: bool):
        """
        FUNCIÓN:
        Se escoge el tipo de formato de resolución.

        :param event: Guarda el tipo de formato en una variable
        :param bool exceeding: booleano que indica si se sobrepasó.
        """
        # Se obtiene la respuesta de la resolución.
        self.resolution = event.widget.get()
        # Estos datos deben ser vaciados para que no haya
        # problemas luego al descargar.
        self.file_type = ''
        # Si el título del video se excedió de caracteres, los elementos en la
        # ventana serán un total de 14.
        if exceeding is True:
            elements = 15
        # Si el título del video se excedió de caracteres, los elementos en la
        # ventana serán un total de 13.
        else:
            elements = 14
        # Si el formato de resolución es de 144p entonces se ejecutará todo el
        # siguiente bloque de código.
        if self.resolution == '144p':
            # Si hay más de 13 widgets, todas las añadidas recientemente
            # serán eliminadas.Esto se hace debido a que se crean varias
            # copias y esto puede sobrecargar la aplicación.
            self.erase_widgets(elements)
            # Se crea una caja para decidir el formato de archivo.
            file_types_cb = ttk.Combobox(self.misc, values=['3gp', 'mp4'])
            tk.Label(self.misc, text='Formato de archivo').place(x=10, y=70)
            file_types_cb.place(x=10, y=100)
            file_types_cb.bind('<<ComboboxSelected>>', lambda event:
                               self.set_file_type(event))
        # Si el formato de resolución es cualquier otro entonces se ejecutará
        # todo el siguiente bloque de código.
        else:
            # Si hay más de 13 widgets, todas las añadidas recientemente
            # serán eliminadas.Esto se hace debido a que se crean varias
            # copias y esto puede sobrecargar la aplicación.
            self.erase_widgets(elements)
            # Se crea una caja para decidir el formato de archivo, en este
            # caso solo habrá formato mp4.
            file_types_cb = ttk.Combobox(self.misc, values='mp4')
            tk.Label(self.misc, text='Formato de archivo').place(x=10, y=70)
            file_types_cb.place(x=10, y=100)
            file_types_cb.bind('<<ComboboxSelected>>', lambda event:
                               self.set_file_type(event))

    def directoryLocation(self):
        """
        FUNCIÓN:
        Preguntar por la dirección.
        """
        # Es una función estática.
        # Se pregunta por la dirección del archivo.
        filename = filedialog.askdirectory()
        return filename

    def insertPath(self, entry: tk.Entry):
        """
        FUNCIÓN:
        Insertar la dirección y su path.

        :param tk.Entry entry: Entrada del path.
        """
        # Se borra el texto que contenga
        # y se introduce la dirección anterior.
        entry.delete(0, 'end')
        entry.insert(0, self.directoryLocation())

    def check_direction(self):
        """
        FUNCIÓN:
        Revisar si la dirección se encuentra vacía.

        :return self.location.get(): Si la dirección existe,
        o False si está vacía o si no existe.
        """
        # Se obtiene el nombre de la dirección.

        # Si la dirección está vacía, surge un mensaje de advertencia para
        # que se solicite una dirección.
        if self.location.get() == '':
            self.notifier.advice_choose_location()
            return False
        # De no ser así, se regresará el valor de True.
        else:
            # Se debe verificar que la dirección exista.
            path_existance = os.path.exists(self.location.get())
            # Si la dirección no existe entonces surge un mensaje
            # de advertencia para que se ponga dirección que exista.
            if path_existance is False:
                # ARREGLAR ESTO.
                self.notifier.advice_nonexistent_location()
                return False
            # Si la dirección existe entonces se retornará
            # la dirección como valor.
            else:
                return self.location.get()

    def set_name(self, name, extension):
        """
        FUNCIÓN:
        Se escoge el nombre para el archivo que se va a descargar.

        :param name: Guarda el nombre del archivo.
        :param extension: Guarda el formato del archivo a descargar.

        :return video_name: Si no está vacío o False si está vacío o
        """
        # Si el nombre está vacío, se retorna False.
        if name == '':
            return False
        # Si el nombre no está vacío se devolverá el nombre más la extensión.
        else:
            video_name = str(name) + '.' + str(extension)
            return video_name
