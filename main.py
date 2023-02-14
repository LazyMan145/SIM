import random
import tkinter
import customtkinter as CTk
import pyperclip as pyperclip
from package.Creatin_file import creating_file
#lj,fdb=fdkngfvieaslkrngio
CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("blue")


class klass_of_worck(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x600")
        self.title("Классификатор работы")
        self.minsize(300, 200)

        tab_objects = {
            "Tab 1": str("Вкладка 1"),
            "Tab 2": str("Вкладка 2")
        }

        self.top_Klass_of_worck = CTk.CTkFrame(self, width=140, corner_radius=0)
        self.top_Klass_of_worck.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.tabview = CTk.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        for i in tab_objects:
            self.tabview.add(i)
        tab_1 = self.tabview.tab("Tab 1")
        self.top_Klass_of_worck_top_frame = CTk.CTkFrame(tab_1, width=140, corner_radius=0)
        self.top_Klass_of_worck_top_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")
        tab_1_context = self.top_Klass_of_worck_top_frame

        self.label_1 = CTk.CTkLabel(tab_1_context, text="Код")
        self.label_1.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.text_field_1 = CTk.CTkEntry(tab_1_context, placeholder_text="Код")
        self.text_field_1.grid(row=0, column=1, rowspan=4, sticky="NSEW")
        self.button_1 = CTk.CTkButton(tab_1_context, text="", width=30)
        self.button_1.grid(row=0, column=2, rowspan=4, sticky="nsew")

        self.label_2 = CTk.CTkLabel(tab_1_context, text="Значение")
        self.label_2.grid(row=20, column=0, rowspan=4, sticky="nsew")
        self.text_field_2 = CTk.CTkEntry(tab_1_context, placeholder_text="Значение")
        self.text_field_2.grid(row=20, column=1, rowspan=4, sticky="NSEW")
        self.button_2 = CTk.CTkButton(tab_1_context, text="", width=30)
        self.button_2.grid(row=20, column=2, rowspan=4, sticky="nsew")

        self.label_3 = CTk.CTkLabel(tab_1_context, text="Описание")
        self.label_3.grid(row=40, column=0, rowspan=4, sticky="nsew")
        self.text_field_3 = CTk.CTkEntry(tab_1_context, placeholder_text="Описание", height=50)
        self.text_field_3.grid(row=40, column=1, rowspan=4, sticky="NSEW")
        self.button_3 = CTk.CTkButton(tab_1_context, text="", width=30)
        self.button_3.grid(row=40, column=2, rowspan=4, sticky="nsew")

        self.record_list_title_frame = CTk.CTkFrame(tab_1, width=140, corner_radius=0)
        self.record_list_title_frame.grid(row=45, column=0, columnspan=3, sticky="nsew")

        self.record_list_title = CTk.CTkLabel(self.record_list_title_frame,
                                              text=f"{12} entries returned - {12} entries matched")
        self.record_list_title.grid(row=15, column=2)

        self.record_list_refresh_button = CTk.CTkButton(self.record_list_title_frame, text="Refresh")
        self.record_list_refresh_button.grid(row=18, column=0)

        self.record_list = CTk.CTkScrollableFrame(self.record_list_title_frame,
                                                  width=800,
                                                  height=600)
        self.record_list.grid(row=20, column=2, padx=(10, 0), pady=(10, 0), sticky="nsew", rowspan=10)

        self.button_record_1 = CTk.CTkButton(self.record_list_title_frame, text="Ok", width=30)
        self.button_record_1.grid(row=100, column=0, rowspan=4, sticky="nsew")


# TODO создание класса Верхнее меню для выборки объекта
class Object_of_line(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("350x666")
        self.title("Объект сети")
        self.minsize(300, 200)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.top_object_frame = CTk.CTkFrame(self, width=140, corner_radius=0)
        self.top_object_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.label_tab_2 = CTk.CTkLabel(self.top_object_frame, text="Выберете объект сети")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        self.optionmenu_region = CTk.CTkOptionMenu(self.top_object_frame, dynamic_resizing=False,
                                                   values=["Регион 1",
                                                           "Регион 2",
                                                           "Регион 3",
                                                           "Регион 4",
                                                           "Регион 5"
                                                           ])
        self.optionmenu_region.grid(row=1, column=0, padx=20, pady=(20, 10))

        CheckBoxname = CTk.CTkCheckBox(master=self.top_object_frame, text="Название")
        CheckBoxname.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n", )

        self.entry = CTk.CTkEntry(self.top_object_frame, placeholder_text="%")
        self.entry.grid(row=2, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        CheckBoxadres = CTk.CTkCheckBox(master=self.top_object_frame, text="Адрес")
        CheckBoxadres.grid(row=3, column=0, pady=(20, 0), padx=20, sticky="n", )

        self.entry = CTk.CTkEntry(self.top_object_frame, placeholder_text="%")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.textbox_objects = CTk.CTkTextbox(self.top_object_frame, width=250)
        self.textbox_objects.grid(row=4, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew", columnspan=2)
        self.textbox_objects.insert("0.0", "CTkTextbox")

        self.button_Ok_object = CTk.CTkButton(master=self.top_object_frame,
                                              width=120,
                                              height=32,
                                              border_width=0,
                                              corner_radius=8,
                                              text="Подтвердить")
        # command=)
        self.button_Ok_object.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.button_Ok_object.grid(row=5, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew", columnspan=2)


# создание класса меню
class App(CTk.CTk):
    def __init__(self):

        #сбор данных (рабочая версия)
        #######################################################################################################
        def data():
            ddescription = description.get()
            CheckBox51 = CheckBox1.get()
            CheckBox11 = CheckBox3.get()
            CheckBox31 = CheckBox5.get()
            sstatus = status.get()
            ppriority = priority.get()
            sservice = service.get()
            iinfluence = influence.get()
            ttype_of_work = type_of_work.get()
            sstart_time_label_1 = start_time_field_1.get()
            sstart_plan_label_1 = start_plan_field_1.get()
            eend_plan_label_1 = end_plan_field_1.get()
            eend_time_label_1 = end_time_work_field_1.get()

            creating_file(ddescription, CheckBox51, CheckBox11, CheckBox31, sstatus, ppriority, sservice, iinfluence, ttype_of_work,
                          sstart_time_label_1, sstart_plan_label_1, eend_plan_label_1, eend_time_label_1)


        #######################################################################################################



        super().__init__()
        window_weight = 1280
        window_height = 720
        self.geometry(f"{window_weight}x{window_height}")
        self.title("SIM")
        self.minsize(300, 200)

        # создание сетки 4х4

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Создание списка сверху
        general_Kenobi = {
            "Главная": str("Главная"),
            "Remedy": str("Remedy"),
            "Бригады": str("Бригады"),
            "Мои работы": str("Мои работы"),
            "Мой профиль": str("Мой профиль"),
            "Обратная связь": str("Обратная связь"),
        }

        left_buttons = {
            "Работы": str("Работы"),
            "Единичные инцеденты": str("Единичные инцеденты"),
            "Массовые инцеденты": str("Массовые инцеденты"),
        }

        print()
        self.tabview = CTk.CTkTabview(self, width=window_weight, height=window_height)
        self.tabview.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        for i in general_Kenobi:
            self.tabview.add(i)

        self.left_buttons_tabview = CTk.CTkFrame(self.tabview.tab(general_Kenobi["Remedy"]), width=window_weight)
        self.left_buttons_tabview.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # Главная

        # списки

        self.general_option_1 = CTk.CTkOptionMenu(self.tabview.tab(general_Kenobi["Главная"]),
                                                  dynamic_resizing=False,
                                                  values=[
                                                      "функция1",
                                                      "функция2",
                                                      "функция3"
                                                  ])
        self.general_option_1.grid(row=1, column=0, padx=20, pady=(20, 10))

        self.general_option_2 = CTk.CTkComboBox(self.tabview.tab(general_Kenobi["Главная"]), values=[
            "функция1",
            "функция2",
            "функция3"
        ])
        self.general_option_2.grid(row=2, column=0, padx=20, pady=(10, 10))

        # кнопка

        self.string_input_button = CTk.CTkButton(self.tabview.tab(general_Kenobi["Главная"]), text="Кнопка")
        self.string_input_button.grid(row=3, column=0, padx=20, pady=(10, 10))

        # Remedy

        current_frame = {
            "Заведение работы": 3
        }

        # Центральное меню со скролбаром
        self.scrollable_frame_Remedy = CTk.CTkScrollableFrame(self.tabview.tab(general_Kenobi["Remedy"]),
                                                              label_text="Заведение работы",
                                                              width=900,
                                                              height=600)
        scrollable_frame_Remedy_grid = (0, 1, (10, 0), (10, 0), "nsew", 10)  # TODO в структуру
        self.scrollable_frame_Remedy.grid(row=scrollable_frame_Remedy_grid[0],
                                          column=scrollable_frame_Remedy_grid[1],
                                          padx=scrollable_frame_Remedy_grid[2],
                                          pady=scrollable_frame_Remedy_grid[3],
                                          sticky=scrollable_frame_Remedy_grid[4],
                                          rowspan=scrollable_frame_Remedy_grid[5])

        self.scrollable_frame_Remedy.grid_columnconfigure(0, weight=1)

        self.left_buttons_frame = CTk.CTkFrame(master=self.tabview)

        # заголовок

        self.label_tab_2 = CTk.CTkLabel(self.left_buttons_tabview, text="Вы перешли на страницу Remedy")
        self.label_tab_2.grid(row=1, column=0, padx=20, pady=20)

        # кнопки

        hiest_butt = 30
        width_butt = 160

        self.string_input_Worck = CTk.CTkButton(self.left_buttons_tabview,
                                                text="Работы",
                                                anchor=tkinter.W,
                                                width=width_butt,
                                                height=hiest_butt,
                                                command=lambda: self.rab_button_onClck(self.scrollable_frame_Remedy,
                                                                                       scrollable_frame_Remedy_grid))
        self.string_input_Worck.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.string_input_button3 = CTk.CTkButton(self.left_buttons_tabview, text="Еденичные инциденты",
                                                  anchor=tkinter.W, width=width_butt, height=hiest_butt)
        self.string_input_button3.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.string_input_button4 = CTk.CTkButton(self.left_buttons_tabview, text="Массовые инциденты",
                                                  anchor=tkinter.W, width=width_butt, height=hiest_butt)
        self.string_input_button4.grid(row=4, column=0, padx=20, pady=(10, 10))

        # № работы - выдаётся пользователю0

        nomer_raboti = str(f"{random.randint(0, 999999)}")
        otstupi = int(1)

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="№ работы")

        label.grid(row=0, column=0, padx=otstupi, pady=(0, 20), ipadx=otstupi)

        self.copy_button_nomer_raboti = CTk.CTkButton(self.scrollable_frame_Remedy,
                                                      text=nomer_raboti,
                                                      anchor=tkinter.W,
                                                      width=width_butt,
                                                      height=hiest_butt,
                                                      command=lambda: copy_button(nomer_raboti))

        self.copy_button_nomer_raboti.grid(row=0, column=1, padx=0, pady=(10, 10))

        # № инцидента - выдаётся пользователю1

        nomer_incindenta = str(random.randint(0, 9999999999999999))

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="№ инцидента")
        label.grid(row=1, column=0, padx=otstupi, pady=(0, 20), ipadx=otstupi)

        self.copy_button_nomer_incindenta = CTk.CTkButton(self.scrollable_frame_Remedy,
                                                          text=nomer_incindenta,
                                                          anchor=tkinter.W,
                                                          width=width_butt,
                                                          height=hiest_butt,
                                                          command=lambda: copy_button(nomer_incindenta))

        self.copy_button_nomer_incindenta.grid(row=1, column=1, padx=0, pady=(10, 10))

        # № ЕИ - выдаётся пользователю2

        nomer_EI = str(12324567456786)

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="№ ЕИ")
        label.grid(row=2, column=0, padx=otstupi, pady=(0, 20), ipadx=otstupi)

        self.copy_button_nomer_EI = CTk.CTkButton(self.scrollable_frame_Remedy,
                                                  text=nomer_EI,
                                                  anchor=tkinter.W,
                                                  width=width_butt,
                                                  height=hiest_butt,
                                                  command=lambda: copy_button(nomer_EI))

        self.copy_button_nomer_EI.grid(row=2, column=1, padx=0)

        # Тип работы - выборка пользователя3

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="Тип работы")
        label.grid(row=3, column=0, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        type_of_work = CTk.CTkOptionMenu(self.scrollable_frame_Remedy, dynamic_resizing=False, values=[
            "Ремонт",
            "Аудит",
            "Ремонт+Аудит"
        ])
        type_of_work.grid(row=3, column=1, padx=(otstupi, otstupi), pady=(10, 0), ipadx=(otstupi))

        # Тип работы (классификация). - ????4

        self.toplevel_window = None

        def open_klass_of_worck():
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = klass_of_worck(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it

        main_button_object_of_klasif = CTk.CTkButton(master=self.scrollable_frame_Remedy,
                                                     fg_color="transparent",
                                                     border_width=2,
                                                     text_color=("gray10", "#DCE4EE"),
                                                     text="Выбрать", command=open_klass_of_worck)

        main_button_object_of_klasif.grid(row=4, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        lable_object_of_klasif = CTk.CTkLabel(master=self.scrollable_frame_Remedy,
                                              text="вернуть значение выбранной класификации")
        lable_object_of_klasif.grid(row=4, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # "Тип работы (классификация)")
        #     "Ремонт",
        #     "Аудит",
        #     "Ремонт+Аудит"

        # Статус - выборка пользователя5

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="Статус")
        label.grid(row=5, column=0, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        status = CTk.CTkOptionMenu(self.scrollable_frame_Remedy, dynamic_resizing=False, values=[
            "Заведена",
            "Решёна",
            "Назначена"
        ])
        status.grid(row=5, column=1, padx=(otstupi, otstupi), pady=(10, 0), ipadx=(otstupi))

        # Приоритет - выборка пользователя6

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="Приоретет")
        label.grid(row=6, column=0, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        priority = CTk.CTkOptionMenu(self.scrollable_frame_Remedy, dynamic_resizing=False, values=[
            "Высокий",
            "Средний",
            "Низкий"
        ])
        priority.grid(row=6, column=1, padx=(otstupi, otstupi), pady=(10, 0), ipadx=(otstupi))

        # Описание - текстовое поле7

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="Описание")
        label.grid(row=7, column=0, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        description = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="Описание")
        description.grid(row=7, column=1, columnspan=1, padx=(otstupi, otstupi), pady=(10, 0), sticky="nsew")

        # Основание - текстовое поле8

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="Основание")
        label.place(relx=0, rely=0, anchor=tkinter.W, x=0)
        label.grid(row=8, column=0, padx=0, pady=(0, 0), ipadx=otstupi)
        foundation = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="Основание")
        foundation.grid(row=8, column=1, columnspan=1, padx=(otstupi, otstupi), pady=(10, 0), sticky="nsew")

        # Объект сети - текстовое поле9 необходимо сделать отдельное окно
        self.toplevel_window = None

        def open_object_of_networck():
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = Object_of_line(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it

        main_button_object_of_networck = CTk.CTkButton(master=self.scrollable_frame_Remedy,
                                                       fg_color="transparent",
                                                       border_width=2,
                                                       text_color=("gray10", "#DCE4EE"),
                                                       text="Выбрать", command=open_object_of_networck)

        main_button_object_of_networck.grid(row=9, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        lable_object_of_networck = CTk.CTkLabel(master=self.scrollable_frame_Remedy,
                                                text="вернуть значение выбранной площадки")
        lable_object_of_networck.grid(row=9, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Влияние на сервис - выборка пользователя10

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="Влияние на сервис")
        label.grid(row=10, column=0, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        service = CTk.CTkOptionMenu(self.scrollable_frame_Remedy, dynamic_resizing=False, values=[
            "Полное",
            "Частичное",
            "Без влияния"
        ])
        service.grid(row=10, column=1, padx=(otstupi, otstupi), pady=(10, 0), ipadx=(otstupi))

        # Тип Сервиса - выборка пользователя11

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="Тип Сервиса")
        label.grid(row=11, column=0, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        influence = CTk.CTkOptionMenu(self.scrollable_frame_Remedy, dynamic_resizing=False, values=[
            "Нет",
            "Сервис 1",
            "Сервис 2"
        ])
        influence.grid(row=11, column=1, padx=(otstupi, otstupi), pady=(10, 0), ipadx=(otstupi))

        # Код закрытия -выборка пользователя12

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="Код закрытия")
        # label.place(relx=0.5, rely=0.5, anchor=tkinter.SE)
        label.grid(row=12, column=0, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        closing_code = CTk.CTkOptionMenu(self.scrollable_frame_Remedy, dynamic_resizing=False, values=[
            "5y56y5yh45",
            "5gg45g54gt1",
            "45g45g4erg54g4w"
        ])
        closing_code.grid(row=12, column=1, padx=(otstupi, otstupi), pady=(10, 0), ipadx=(otstupi))

        # исполнитель -поле ввода13

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="Исполнитель")
        label.grid(row=13, column=0, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        description = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="Иванов И И")
        description.grid(row=13, column=1, columnspan=1, padx=(otstupi, otstupi), pady=(10, 0), sticky="nsew")

        # контролирующий -поле ввода14

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="Контролирующий")
        label.grid(row=14, column=0, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        description = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="Иванов И И")
        description.grid(row=14, column=1, columnspan=1, padx=(otstupi, otstupi), pady=(10, 0), sticky="nsew")

        # инициатор -поле ввода15

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="Инициатор")
        label.grid(row=15, column=0, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        description = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="Иванов И И")
        description.grid(row=15, column=1, columnspan=1, padx=(otstupi, otstupi), pady=(10, 0), sticky="nsew")

        # 16

        # кнопка продолжить

        self.continue_button = CTk.CTkButton(self.scrollable_frame_Remedy,
                                             text="Продолжить",
                                             anchor=tkinter.W,
                                             width=width_butt,
                                             height=hiest_butt,
                                             command=data)
        self.continue_button.grid(row=17, column=0, padx=20, pady=(10, 10))

        # -----------------------------------------------------
        # № внешний1 Не делать

        # № родительский2

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="родительский")
        # label.place(relx=0.5, rely=0.5, anchor=tkinter.SE)
        label.grid(row=2, column=2, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        self.entry = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="родительский")
        self.entry.grid(row=2, column=3, columnspan=2, padx=(otstupi, otstupi), pady=(0, 0), sticky="nsew")

        label = CTk.CTkLabel(master=self.scrollable_frame_Remedy, text="родительская")
        label.grid(row=2, column=2, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        # Доп.информация3 Не делать

        # Проект - выборка пользователя4 Не делать

        # TODO Необходимо сделать виджет для временных окон
        # датавремя и кнопка "сейчас"
        # ограниченная форма день, весяц, год, час, минута, секунда 08.02.2023 15:00:00

        # Планируемое начало - дата/время5
        self.start_time_label_1 = CTk.CTkLabel(self.scrollable_frame_Remedy, text="Планируемое начало")
        self.start_time_label_1.grid(row=5, column=2, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        start_time_field_1 = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="01.12.2017 10:00:00")
        start_time_field_1.grid(row=5, column=3, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        # Начало работ - дата/время6

        self.start_time_label_2 = CTk.CTkLabel(self.scrollable_frame_Remedy, text="Начало работ")
        self.start_time_label_2.grid(row=6, column=2, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        self.start_time_field_2 = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="")
        self.start_time_field_2.grid(row=6, column=3, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        # План.нач.погран.сервиса - дата/время7

        self.start_plan_label_1 = CTk.CTkLabel(self.scrollable_frame_Remedy, text="План.нач.огран.сервиса")
        self.start_plan_label_1.grid(row=7, column=2, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        start_plan_field_1 = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="02.12.2017 10:00:00")
        start_plan_field_1.grid(row=7, column=3, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        # План.оконч.огран.сервиса - дата/время8
        self.start_plan_label_1 = CTk.CTkLabel(self.scrollable_frame_Remedy, text="План.оконч.огран.сервиса")
        self.start_plan_label_1.grid(row=8, column=2, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        end_plan_field_1 = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="02.12.2017 22:00:00")
        end_plan_field_1.grid(row=8, column=3, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        # Время окончания работ - дата/время9

        self.end_time_work_1 = CTk.CTkLabel(self.scrollable_frame_Remedy, text="Время окончания работ")
        self.end_time_work_1.grid(row=9, column=2, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        self.end_time_work_field_1 = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="")
        self.end_time_work_field_1.grid(row=9, column=3, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        # Планируемое окончание - дата/время10
        self.end_time_work_1 = CTk.CTkLabel(self.scrollable_frame_Remedy, text="Планируемое окончание")
        self.end_time_work_1.grid(row=10, column=2, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        end_time_work_field_1 = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="03.12.2017 22:00:00")
        end_time_work_field_1.grid(row=10, column=3, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        # Время контроля - дата/время11
        self.control_time_1 = CTk.CTkLabel(self.scrollable_frame_Remedy, text="Время контроля")
        self.control_time_1.grid(row=11, column=2, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        self.control_time_field_1 = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="")
        self.control_time_field_1.grid(row=11, column=3, padx=otstupi, pady=(0, 0), ipadx=otstupi)
        # Период проведения - 2 временных контейнера12

        self.period_label = CTk.CTkLabel(self.scrollable_frame_Remedy, text="Период проведения")
        self.period_label.grid(row=12, column=2, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        self.period_field = CTk.CTkEntry(self.scrollable_frame_Remedy, placeholder_text="12.12.2022 - 15.12.2022")
        self.period_field.grid(row=12, column=3, padx=otstupi, pady=(0, 0), ipadx=otstupi)

        # чекбокс13-17

        CheckBox1 = CTk.CTkCheckBox(master=self.scrollable_frame_Remedy, text="Привлечение поставщика / подрядчика")
        CheckBox1.grid(row=13, column=2, pady=(20, 0), padx=20, sticky="n", )

        CheckBox2 = CTk.CTkCheckBox(master=self.scrollable_frame_Remedy, text="Тестовый инцидент")
        CheckBox2.grid(row=14, column=2, pady=(20, 0), padx=20, sticky="n", )

        CheckBox3 = CTk.CTkCheckBox(master=self.scrollable_frame_Remedy, text="Оповещение сервиса")
        CheckBox3.grid(row=15, column=2, pady=(20, 0), padx=20, sticky="n", )

        CheckBox4 = CTk.CTkCheckBox(master=self.scrollable_frame_Remedy, text="Проведение работ в период моратория")
        CheckBox4.grid(row=16, column=2, pady=(20, 0), padx=20, sticky="n", )

        CheckBox5 = CTk.CTkCheckBox(master=self.scrollable_frame_Remedy, text="Идёт в отчёт")
        CheckBox5.grid(row=17, column=2, pady=(20, 0), padx=20, sticky="n", )

    current_state = False  # TODO: заменить на текущую позицию и переделать rab_button_onClick

    def rab_button_onClck(self, event, grid):
        print(App.current_state)
        if App.current_state:
            event.grid_forget()
            App.current_state = False
        else:
            event.grid(row=grid[0], column=grid[1], padx=grid[2], pady=grid[3], sticky=grid[4], rowspan=grid[5])
            App.current_state = True


def copy_button(*context):
    print(context)
    pyperclip.copy(" ".join([str(i) for i in context]))

    # Бригады

    # Мои работы

    # Мой профиль

    # Обратная связь


# цикл обработки скрипта
if __name__ == "__main__":
    app = App()
app.mainloop()