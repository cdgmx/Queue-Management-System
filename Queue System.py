from tkinter import *
import datetime
import threading
import time
from tkinter import messagebox

from tkinter import messagebox


class Main_Page:

    def __init__(self, master):

        self.master = master


        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self.master.grid_rowconfigure(2, weight=1)




        Title_Frame(self.master)
        Department_Choice_Frame(self.master)
        Input_Frame(self.master,1)






        output_obj = Output_Frame(self.master)

        output_obj.access_frame()


        output_obj.output(self.master)
        output_obj.num_label_disp()

        send_notif_obj = Send_Notif(root)
        t1 = threading.Thread(target=send_notif_obj.send_text_ten)
        t2 = threading.Thread(target=send_notif_obj.send_text_twenty)
        t1.start()
        t2.start()



















        # self.toplevel_obj = Output_Frame(self.out_toplevel)
        # self.toplevel_obj.output(self.out_toplevel)









class Clock_Frame:

    def __init__(self, master):
        self.master = master
        # self.Clock_Frame = Frame(master, background="Red")
        # self.Clock_Frame.grid(row=1, column=0,sticky = "nsew")
        # self.Clock_Frame.grid_columnconfigure(0,weight= 1)
        # self.Clock_Frame.grid_rowconfigure(0, weight=1)
        #

    def clock_disp(self):


        self.clock = Label(self.master, font=("times", 10, "bold"), bg="white", relief=RIDGE)
        self.clock.grid(row=2)

        self.tick()


    def tick(self):
        tday = datetime.datetime.today()
        time = str(tday.strftime('%H:%M:%S%f')[:-6])
        time_string =tday.strptime(time, "%H:%M:%S").strftime("%H:%M:%S %p")

        self.clock.config(text=time_string)
        self.clock.after(10, self.tick)


class Title_Frame():

    def __init__(self,master):


        self.master = master

        self.queue_title_frame = Frame(self.master, background="Blue")
        self.queue_title_frame.grid(row=0, column=0, columnspan = 2, sticky ="nsew")



        self.queue_title_frame.grid_columnconfigure(0, weight = 1)

        #
        #
        # self.Title_Frame.grid_rowconfigure(1, weight = 1)
        #
        # test_label = Label(self.queue_title_frame, text ="This is title Frame", relief = RIDGE)
        # test_label.grid(sticky ="ew")

        welcomelbl = Label(self.queue_title_frame, text="San Agustin Queue System", font = "VERDANA, 20",fg= "White", bg= "Black")
        welcomelbl.grid(column=0, row=1, sticky = "new")

        self.clock_obj = Clock_Frame(self.queue_title_frame)
        self.clock_obj.clock_disp()
    #     self.menubar()
    #
    # def menubar(self):
    #
    #     menubar = Menu(root)
    #
    #     filemenu = Menu(menubar, tearoff=0)
    #     menubar.grid(sticky ="ew")
    #     #
    #     # filemenu.add_command(label="New")



class Department_Choice_Frame:

    def __init__(self, master):



        self.master = master


        self.choice_frame = Frame(master, background="Red")
        self.choice_frame.grid(row=1, column=0, columnspan = 2, sticky ="nsew")

        self.choice_frame.grid_columnconfigure(0, weight=1)
        self.choice_frame.grid_columnconfigure(1, weight=1)
        self.choice_frame.grid_columnconfigure(2, weight=1)
        self.choice_frame.grid_columnconfigure(3, weight=1)

        test_label = Label(self.choice_frame, text="This is Department Choice", relief=RIDGE)
        test_label.grid(sticky="ew", columnspan = 4)
        # self.obj = Control_Button_Frame(self.master)

        # labeltest = Label(self.Choice_Frame, text="this is choice Frame", relief = RIDGE)
        # labeltest.grid(row=0, column=0, columnspan = 4,  sticky ="new")

        self.cot_button = Button(self.choice_frame, text = "COT", command = lambda:
        [
           self.enable_labelframe(1),
           self.disable_choiceframe()
        ])
        self.cot_button.grid(row = 1, column = 0, sticky = "new")

        self.clase_button = Button(self.choice_frame, text="CLASE", command = lambda:
        [
           self.enable_labelframe(2),
            self.disable_choiceframe()
        ])
        self.clase_button.grid(row=1, column=1, sticky="ew")

        self.coc_button = Button(self.choice_frame, text="COC", command = lambda:
        [
           self.enable_labelframe(3),
            self.disable_choiceframe()
        ])
        self.coc_button.grid(row=1, column=2, sticky="ew")

        self.champ_button = Button(self.choice_frame, text="CHAMP", command = lambda:
        [
           self.enable_labelframe(4),
            self.disable_choiceframe()
        ])
        self.champ_button.grid(row=1, column=3, sticky="ew")



    def enable_labelframe(self,choice):
        self.inp_obj = Input_Frame(self.master,choice)
        self.inp_obj.enable_labelframe()


    def disable_choiceframe(self):
        for child in self.choice_frame.winfo_children():
            child.configure(state='disable')

    def enable_choiceframe(self):
        for child in self.choice_frame.winfo_children():
            child.configure(state='normal')



class Input_Frame:


    def __init__(self, master, choice):

        self.CheckVar1 = IntVar()
        self.CheckVar2 = IntVar()
        self.master = master
        #access department choice

        # self.choiceobj = Department_Choice_Frame(self.master)

        #access data holder
        self.access_data_obj = Data_Holder()


        self.choice = choice

        self.input_data_frame = Frame(self.master, background="Pink")
        self.input_data_frame.grid(row=2, column=0, sticky="nsew")
        self.input_data_frame.grid_columnconfigure(0, weight = 1)
        self.input_data_frame.grid_rowconfigure(1, weight =1)

        test_label = Label(self.input_data_frame, text="This is Input Frame", relief=RIDGE)
        test_label.grid(row =0, sticky="ew")

        self.labelframe = LabelFrame(self.input_data_frame, text="This is a LabelFrame")
        self.labelframe.grid(row = 1, column = 0, sticky = "nsew")

        self.labelframe.grid_columnconfigure(0 ,weight =1)
        self.labelframe.grid_columnconfigure(1, weight=1)


        self.name_label = Label(self.labelframe, text="Name:")
        self.name_label.grid(row = 2, column =0, sticky = "ew")

        self.name_entry = Entry(self.labelframe)
        self.name_entry.grid(row =2, column =1, sticky ="ew")

        self.contactnum_label = Label(self.labelframe, text="Contact:")
        self.contactnum_label.grid(row=3, column=0, sticky="ew")




        self.contactnum_entry = Entry(self.labelframe)
        self.contactnum_entry.grid(row=3, column=1, sticky="ew")

        self.check_button_receive = Checkbutton(self.labelframe, text="Receive Notification", variable=self.CheckVar1, onvalue=1, offvalue=0,
                                                command = lambda:[
                                                    self.checkbutton_state(),
                                                    self.notif_interval_scale()

                                                ])
        self.check_button_receive.grid(row=4, column=0, sticky="w")

        self.check_button_display_name = Checkbutton(self.labelframe, text="Send Queue Number", variable=self.CheckVar2,onvalue=1,offvalue=0,
                                                command=lambda: [
                                                self.checkbutton_state(),
                                                     ])
        self.check_button_display_name.grid(row=4, column=1, sticky="w")




        self.back_button = Button (self.labelframe, text = "Back",command = lambda:
        [
            self.enable_choiceframe(),
            self.disable_labelframe()

        ])
        self.back_button.grid(row= 6, column = 0,  sticky ="ew")

        self.back_button = Button(self.labelframe, text="Submit", command= lambda:


        [

            # self.access_data_obj.cot_append(self.retrieve_data()),
            self.check_submit(choice)
            # self.queue_number(),
            # self.data_append(choice),
            # self.access_send_notif(choice)

        ])

        self.back_button.grid(row=6, column=1, sticky="ew")



        for child in self.labelframe.winfo_children():
            child.configure(state='disable')

    def checkbutton_state(self):
        print("pass check button state")
        print(self.CheckVar1.get())
        if self.CheckVar1.get() == 1:
            self.check_button_display_name.configure(state = DISABLED)
        else:
            self.check_button_display_name.configure(state=NORMAL)
        if self.CheckVar2.get() == 1:
            self.check_button_receive.configure(state= DISABLED)
        else:
            self.check_button_receive.configure(state=NORMAL)


    #check if entered details is correct
    def check_submit(self,choice):
        print(self.contactnum_entry.get(), len(self.contactnum_entry.get()))
        if self.CheckVar1.get() == 1:
            if len(self.contactnum_entry.get()) == 11 and  (self.contactnum_entry.get()).isnumeric() == True:

                self.queue_number(),
                self.data_append(choice),
                self.access_send_notif(choice)
            else:
                messagebox.showwarning("Error", "you should enter 11 digit number or integer")
        else:
            if str(self.contactnum_entry.get()) == "":
                self.queue_number(),
                self.data_append(choice),
                self.access_send_notif(choice)

            else:
                if len(self.contactnum_entry.get()) == 11 and (self.contactnum_entry.get()).isnumeric() == True:
                    self.queue_number(),
                    self.data_append(choice),
                    self.access_send_notif(choice)
                else:
                    messagebox.showwarning("Error", "you should enter 11 digit number")



    def access_send_notif(self,choice):
        self.send_notif_obj = Send_Notif(self.master)
        self.send_notif_obj.sort_notif(choice)

    def notif_interval_scale(self):

        self.var = IntVar()




        if self.CheckVar1.get() == 1:
            # self.time_scale.configure(state=ACTIVE)
            self.time_scale = Scale(self.labelframe, variable=self.var, orient=HORIZONTAL, from_=10, to=30,
                                    tickinterval=10, showvalue=0, resolution=10)
            self.time_scale.grid(row=5, column=0, sticky="ew", )

        if self.CheckVar1.get() == 0:
                self.time_scale.destroy()



    def queue_number(self):

        self.your_num_label = Label(self.labelframe, text="Your Queue Number")
        self.your_num_label.grid(row=7, columnspan=2, sticky="ew")

        self.your_num_out = Label(self.labelframe, text=str(len(self.count_dept_data(self.choice))+1))
        self.your_num_out.grid(row=8, columnspan=2, sticky="ew")

        self.user_queue_number = len(self.count_dept_data(self.choice))+1



    def disable_labelframe(self):

        for child in self.labelframe.winfo_children():
            child.configure(state='disable')

    def enable_labelframe(self):
        for child in self.labelframe.winfo_children():
            child.configure(state='normal')


    def enable_choiceframe(self):

        self.choiceobj = Department_Choice_Frame(self.master)

        self.choiceobj.enable_choiceframe()

    def retrieve_data(self,choice):
        #reference of retrieved Data [Name, Contact, Notif interval, Queue number, department choice
        # (1=COT, 2 = CLASE, 3 = COC, 4 = CHAMP)]
        if choice == 1:
            self.department_choice = "COT"
        if choice == 2:
            self.department_choice = "CLASE"
        if choice == 3:
            self.department_choice = "COC"
        if choice == 4:
            self.department_choice = "CHAMP"

        if self.CheckVar1.get() == 0:
            self.name_retrieved = self.name_entry.get()
            self.contact_retrieved = str(self.contactnum_entry.get())
            self.queue_number_retrieved =  self.user_queue_number

            return (self.name_retrieved, self.contact_retrieved,0, self.queue_number_retrieved,self.department_choice)

        if self.CheckVar1.get() ==1 :
            self.name_retrieved = self.name_entry.get()
            self.contact_retrieved = self.contactnum_entry.get()
            self.notif_interval_retrieved = self.time_scale.get()
            self.queue_number_retrieved =  self.user_queue_number
            return (self.name_retrieved, self.contact_retrieved, self.notif_interval_retrieved, self.queue_number_retrieved,self.department_choice)


    def data_append(self, choice):
        if choice == 1:
            self.access_data_obj.cot_append(self.retrieve_data(choice))

        if choice == 2:
            self.access_data_obj.clase_append(self.retrieve_data(choice))

        if choice == 3:
            self.access_data_obj.coc_append(self.retrieve_data(choice))
        if choice == 4:
            self.access_data_obj.champ_append(self.retrieve_data(choice))





    #this will print the current number of a que in each dept

    def count_dept_data(self, choice):
        if choice == 1:
            return self.access_data_obj.return_count_cot_data()
        if choice == 2:
            return self.access_data_obj.return_count_clase_data()

        if choice == 3:
            return self.access_data_obj.return_count_coc_data()
        if choice == 4:
            return self.access_data_obj.return_count_champ_data()














class Output_Frame:

    cot_number_control = 0
    cot_number_disp = []

    clase_number_control = 0
    clase_number_disp = []

    coc_number_control = 0
    coc_number_disp = []

    champ_number_control = 0
    champ_number_disp = []


    for x in range(1000):
            x += 1
            cot_number_disp.append(x)
            clase_number_disp.append(x)
            coc_number_disp.append(x)
            champ_number_disp.append(x)




    def __init__(self, master):
        self.master = master

    def access_frame(self):
        # self.output(self.master)
        self.output(self.master)
        # self.num_label_disp()



        #
        # self.master_obj = Output_Frame(self.master)
        # self.master_obj.output(self.master)
        # self.master_obj.num_label_disp()







        # self.out_obj = Output_Frame(self.out_toplevel)
        # self.out_obj.output(self.out_toplevel)
        # self.out_obj.num_label_disp()






    # def output_frame_toplevel(self):
    #     out = Toplevel()
    #     cotserving_num_label = Label(out, relief=RIDGE)
    #     cotserving_num_label.grid(row=3, column=0, columnspan=2, sticky="ew")
    #
    #     self.tick()




    def output(self,master):


        self.output_data_frame = Frame(master, background="White")
        self.output_data_frame.grid(row=2, column=1, sticky="nsew")

        self.output_data_frame.grid_columnconfigure(0, weight=1)
        self.output_data_frame.grid_rowconfigure(1, weight=1)
        test_label = Label(self.output_data_frame, text="This is Output Frame", relief=RIDGE)
        test_label.grid(sticky="ew")

        self.labelframe = LabelFrame(self.output_data_frame, text="This is a LabelFrame")
        self.labelframe.grid(row=1, column=0, sticky="nsew")

        self.labelframe.grid_columnconfigure(0, weight=1)
        self.labelframe.grid_columnconfigure(1, weight=1)
        self.labelframe.grid_columnconfigure(2, weight=1)


        # COT
        self.cotserving_label = Label(self.labelframe, text="COT Serving Number:")
        self.cotserving_label.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.cotserving_backbutton = Button(self.labelframe, text="<<", relief=RIDGE,command=lambda:
        [
            self.cot_count_sub(1),

            self.access_send_notif(0,int(self.cot_number_disp[self.cot_number_control]))

        ])
        self.cotserving_backbutton.grid(row=4, column=0, sticky="ew")

        self.cotserving_nextbutton = Button(self.labelframe, text=">>", relief=RIDGE,command=lambda:
        [
            self.cot_count_add(1),
            self.access_send_notif(0, int(self.cot_number_disp[self.cot_number_control])),

        ])
        self.cotserving_nextbutton.grid(row=4, column=1, sticky="ew")

        #CLASE
        self.claseserving_label = Label(self.labelframe, text="CLASE Serving Number:")
        self.claseserving_label.grid(row=5, column=0, columnspan=2, sticky="ew")
        self.claseserving_backbutton = Button(self.labelframe, text="<<", relief=RIDGE,command=lambda:
        [
            self.cot_count_sub(2),

            self.access_send_notif(1, int(self.clase_number_disp[self.clase_number_control]))
        ])
        self.claseserving_backbutton.grid(row=7, column=0, sticky="ew")

        self.claseserving_nextbutton = Button(self.labelframe, text=">>", relief=RIDGE,command=lambda:
        [
            self.cot_count_add(2),
            self.access_send_notif(1, int(self.clase_number_disp[self.clase_number_control]))
        ])
        self.claseserving_nextbutton.grid(row=7, column=1, sticky="ew")


        #COC
        self.cocserving_label = Label(self.labelframe, text="COC Serving Number:")
        self.cocserving_label.grid(row=8, column=0, columnspan=2, sticky="ew")
        self.cocserving_backbutton = Button(self.labelframe, text="<<", relief=RIDGE,command=lambda:
        [
            self.cot_count_sub(3),
            self.access_send_notif(2, int(self.coc_number_disp[self.coc_number_control]))
        ])
        self.cocserving_backbutton.grid(row=10, column=0, sticky="ew")

        self.cocserving_nextbutton = Button(self.labelframe, text=">>", relief=RIDGE,command=lambda:
        [
            self.cot_count_add(3),
            self.access_send_notif(2, int(self.coc_number_disp[self.coc_number_control]))
        ])
        self.cocserving_nextbutton.grid(row=10, column=1, sticky="ew")


        #CHAMP
        self.champserving_label = Label(self.labelframe, text="CHAMP Serving Number:")
        self.champserving_label.grid(row=11, column=0, columnspan=2, sticky="ew")
        self.champserving_backbutton = Button(self.labelframe, text="<<", relief=RIDGE,command=lambda:
        [
            self.cot_count_sub(4),
            self.access_send_notif(3, int(self.champ_number_disp[self.champ_number_control]))
        ])
        self.champserving_backbutton.grid(row=13, column=0, sticky="ew")

        self.champserving_nextbutton = Button(self.labelframe, text=">>", relief=RIDGE,command=lambda:
        [

            self.cot_count_add(4),
            self.access_send_notif(3, int(self.champ_number_disp[self.champ_number_control]))
        ])
        self.champserving_nextbutton.grid(row=13, column=1, sticky="ew")




        labeltest = Label(self.output_data_frame, text="this is Input Frame", relief=RIDGE)
        labeltest.grid(row=0, column=0, columnspan=4, sticky="ew")





    def num_label_disp(self):
        # text=str(self.cot_number_disp[self.cot_number_control]),

        self.cotserving_num_label = Label(self.labelframe,
                                          relief=RIDGE)
        self.cotserving_num_label.grid(row=3, column=0, columnspan=2, sticky="ew")

        self.claseserving_num_label = Label(self.labelframe, text=str(self.clase_number_disp[self.clase_number_control]), relief=RIDGE)
        self.claseserving_num_label.grid(row=6, column=0, columnspan=2, sticky="ew")

        self.cocserving_num_label = Label(self.labelframe, text=str(self.coc_number_disp[self.coc_number_control]),
                                          relief=RIDGE)
        self.cocserving_num_label.grid(row=9, column=0, columnspan=2, sticky="ew")

        self.champserving_num_label = Label(self.labelframe, text=str(self.champ_number_disp[self.champ_number_control]), relief=RIDGE)
        self.champserving_num_label.grid(row=12, column=0, columnspan=2, sticky="ew")





        self.tick()

    def tick(self):

        self.cotserving_num_label.config(text = str(self.cot_number_disp[self.cot_number_control]))
        self.cotserving_num_label.after(10,self.tick)
        # print("testing return",self.cot_number_disp[self.cot_number_control])





    def cot_count_add(self,control_num):

        if control_num ==1:

            self.cot_number_control+=1
            # self.num_label_disp()

            print(self.cot_number_disp[self.cot_number_control])


        if control_num == 2:
            self.clase_number_control += 1
            # self.num_label_disp()

        if control_num == 3:
            self.coc_number_control += 1
            # self.num_label_disp()

        if control_num == 4:
            self.champ_number_control += 1
            # self.num_label_disp()



    def cot_count_sub(self,control_num):

        if control_num ==1:

            self.cot_number_control-=1
            self.num_label_disp()

        if control_num == 2:
            self.clase_number_control -= 1
            self.num_label_disp()

        if control_num == 3:
            self.coc_number_control -= 1
            self.num_label_disp()

        if control_num == 4:
            self.champ_number_control -= 1
            self.num_label_disp()

    # def return_current_serving_cot(self):
    #     print("this is current serving", self.cotserving_num_label.cget("text"))
    #     return str(self.cot_number_disp[self.cot_number_control])

    def access_send_notif(self,department,current_number):

        send_notif_obj = Send_Notif(self.master)
        send_notif_obj.current_serving_replace(department,current_number)


class Send_Notif:

    ten_min_notif = []

    twenty_min_notif = []
    retarr = []
    thirty_min_notif = []
    current_serving = [1,1,1,1]
    retarr_twenty = []


    # currentserving [0] = COT, currentserving [1] = clase, currentserving [2] = coc
    # currentserving [3] = champ

    def __init__(self,master):


        self.master = master

        # self.compare_num_obj = Phone(self.master)

        self.access_data_obj = Data_Holder()

        self.accessed_data_cot = self.access_data_obj.return_count_cot_data()

        self.accessed_data_clase = self.access_data_obj.return_count_clase_data()

        self.accessed_data_coc = self.access_data_obj.return_count_coc_data()

        self.accessed_data_champ = self.access_data_obj.return_count_champ_data()



    def current_serving_replace(self,department,current_number):
        self.current_serving[department] = current_number


    def access_current_serving(self):
        pass

    def receive_data_cot(self):
        pass

    def sort_notif(self, choice):

        if choice == 1:

            if self.accessed_data_cot[-1][2] == 10:

                self.ten_min_notif.append(self.accessed_data_cot[-1])



            elif self.accessed_data_cot[-1][2] == 20:
                self.twenty_min_notif.append(self.accessed_data_cot[-1])

            elif self.accessed_data_cot[-1][2] == 30:
                self.thirty_min_notif.append(self.accessed_data_cot[-1])

            print("10 min notif users", self.ten_min_notif)
            print("20 min notif users", self.twenty_min_notif)
            print("30 min notif users", self.thirty_min_notif)

            print("test")


        if choice == 2:

            if self.accessed_data_clase[-1][2] == 10:

                self.ten_min_notif.append(self.accessed_data_clase[-1])

            elif self.accessed_data_clase[-1][2] == 20:
                self.twenty_min_notif.append(self.accessed_data_clase[-1])

            elif self.accessed_data_clase[-1][2] == 30:
                self.thirty_min_notif.append(self.accessed_data_clase[-1])

            print("10 min notif users", self.ten_min_notif)
            print("20 min notif users", self.twenty_min_notif)
            print("30 min notif users", self.thirty_min_notif)
        if choice == 3:

            if self.accessed_data_coc[-1][2] == 10:

                self.ten_min_notif.append(self.accessed_data_coc[-1])

            elif self.accessed_data_coc[-1][2] == 20:
                self.twenty_min_notif.append(self.accessed_data_coc[-1])

            elif self.accessed_data_coc[-1][2] == 30:
                self.thirty_min_notif.append(self.accessed_data_coc[-1])

            print("10 min notif users", self.ten_min_notif)
            print("20 min notif users", self.twenty_min_notif)
            print("30 min notif users", self.thirty_min_notif)

        if choice == 4:

            if self.accessed_data_champ[-1][2] == 10:

                self.ten_min_notif.append(self.accessed_data_champ[-1])

            elif self.accessed_data_champ[-1][2] == 20:
                self.twenty_min_notif.append(self.accessed_data_champ[-1])

            elif self.accessed_data_champ[-1][2] == 30:
                self.thirty_min_notif.append(self.accessed_data_champ[-1])

            print("10 min notif users", self.ten_min_notif)
            print("20 min notif users", self.twenty_min_notif)
            print("30 min notif users", self.thirty_min_notif)

        # self.send_notif_interval_10()
        # self.send_text_cot()




    # def send_notif_interval_10(self):
    #
    #
    #
    #     for numcontroll in range(len(self.ten_min_notif)):
    #         # if self.ten_min_notif[numcontroll][4] == "COT":
    #         #     self.current_serving = self.department_current_serving_obj.return_current_serving_cot()
    #
    #         print(
    #             "Good Day!" + str(self.ten_min_notif[numcontroll][0]),
    #             "Your Queue number is: " + str(self.ten_min_notif[numcontroll][3]),
    #             self.ten_min_notif[numcontroll][4] + " is now serving " +
    #                 self.department_identifier(numcontroll)
    #              )


    def department_identifier_ten(self,numcontrol):
        if self.ten_min_notif[numcontrol][4] == "COT":
            return str(self.current_serving[0])
        elif self.ten_min_notif[numcontrol][4] == "CLASE":
            return str(self.current_serving[1])
        elif self.ten_min_notif[numcontrol][4] == "COC":
            return str(self.current_serving[2])
        elif self.ten_min_notif[numcontrol][4] == "CHAMP":
            return str(self.current_serving[3])

    def department_identifier_twenty(self, numcontrol):

        if self.twenty_min_notif[numcontrol][4] == "COT":
            return str(self.current_serving[0])
        elif self.twenty_min_notif[numcontrol][4] == "CLASE":
            return str(self.current_serving[1])
        elif self.twenty_min_notif[numcontrol][4] == "COC":
            return str(self.current_serving[2])
        elif self.twenty_min_notif[numcontrol][4] == "CHAMP":
            return str(self.current_serving[3])


    def send_text_once(self):

        pass

    def send_text_ten(self):

        #
        print("passing here send text")

        while 1 == 1:


            print("range of tenmin notif", len(self.ten_min_notif))

            for numcontroll in range(len(self.ten_min_notif)):
                # print("range of compare num", len(self.compare_num_obj.set_number))

                ret = ("Good Day!" + str(self.ten_min_notif[numcontroll][0]) +
                       "Your Queue number is: " + str(self.ten_min_notif[numcontroll][3]) +

                       str(self.ten_min_notif[numcontroll][4]) + " is now serving " +
                       str(self.department_identifier_ten(numcontroll)))



                self.retarr.append([ret, 0, W, str(self.ten_min_notif[numcontroll][1])])



            # used ten secs instead of 10 minutes
            print("len of rearr",len(self.retarr))
            print(self.retarr)
            print("waiting")
            time.sleep(10)
            del self.retarr[:]
            self.delete_notif_ten()






    def delete_notif_ten(self):
        print("passing del;ete nmotif")
        if not len(self.ten_min_notif) == 0:
            print("len",len(self.ten_min_notif))
            for numcontroll in range(len(self.ten_min_notif)):
                print("passomg")

                if int(self.ten_min_notif[numcontroll][3]) < int(self.department_identifier_ten(numcontroll)):
                    print("passss")
                    del self.ten_min_notif[numcontroll]
                    self.delete_notif_ten()
                else:
                    self.send_text_ten()


        else:
            self.send_text_ten()

    def send_text_twenty(self):

        #
        print("passing here send text twenty")

        while 1 == 1:


            print("range of rwenty notif", len(self.twenty_min_notif))

            for numcontroll in range(len(self.twenty_min_notif)):
                # print("range of compare num", len(self.compare_num_obj.set_number))
                print("pass in twenty")
                ret = ("Good Day!" + str(self.twenty_min_notif[numcontroll][0]) +
                       "Your Queue number is: " + str(self.twenty_min_notif[numcontroll][3]) +

                       str(self.twenty_min_notif[numcontroll][4]) + " is now serving " +
                       str(self.department_identifier_twenty(numcontroll)))



                self.retarr_twenty.append([ret, 0, W, str(self.twenty_min_notif[numcontroll][1])])



            # used ten secs instead of 10 minutes
            print("len of rearr",len(self.retarr_twenty))
            print(self.retarr_twenty)
            print("waiting")
            time.sleep(20)
            del self.retarr_twenty[:]
            self.delete_notif_twenty()






    def delete_notif_twenty(self):
        print("passing del;ete nmotif")
        if not len(self.twenty_min_notif) == 0:
            print("len",len(self.twenty_min_notif))
            for numcontroll in range(len(self.twenty_min_notif)):
                print("passomg")

                if int(self.twenty_min_notif[numcontroll][3]) < int(self.department_identifier_twenty(numcontroll)):
                    print("passss")
                    del self.twenty_min_notif[numcontroll]
                    self.delete_notif_twenty()
                else:
                    self.send_text_twenty()


        else:
            self.send_text_twenty()





class Data_Holder:


    #data contains (NAME, Phone Number, Notif Interval, User Queue Number, Department)
    cot_data = []
    clase_data = []
    coc_data = []
    champ_data = []


    def cot_current(self):
        pass


    def cot_append(self, data):
        self.cot_data.append(data)
        print("cot recieve", self.cot_data)

    def clase_append(self, data):
        self.clase_data.append(data)
        print("clase recieve",self.clase_data)

    def coc_append(self, data):
        self.coc_data.append(data)
        print("coc recieve", self.coc_data)

    def champ_append(self, data):
        self.champ_data.append(data)
        print("champ recieve",self.champ_data)


    def return_count_cot_data(self):
        return (self.cot_data)
    def return_count_clase_data(self):
        return (self.clase_data)
    def return_count_coc_data(self):
        return (self.coc_data)
    def return_count_champ_data(self):
        return (self.champ_data)







class Phone(Send_Notif):

    set_number = []

    event = []
    event_label = []

    arr = []
    arr2 = []

    delete_button_arr = []

    messages = []
    unique_number = 0

    def phone_frame(self,master):

        self.top = Toplevel()
        self.master = master

        self.top.title(self.unique_name)
        self.top.geometry("500x450")
        self.top.grid_columnconfigure(0, weight=1)
        self.top.grid_rowconfigure(0, weight=1)

        self.main_frame = Frame(self.top, bg="Red", relief=SUNKEN)
        self.main_frame.grid(row=0, sticky="nsew", pady=20, padx=20)

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)




        #
        self.main_label_frame = LabelFrame(self.main_frame, bg="Red", relief=RIDGE)
        self.main_label_frame.grid(row=0, sticky="nsew")

        self.main_label_frame.grid_rowconfigure(0, minsize=50)
        self.main_label_frame.grid_columnconfigure(1, weight=1)
        self.main_label_frame.grid_columnconfigure(0, minsize=50)
        self.main_label_frame.grid_columnconfigure(2, minsize=50)

        self.main_label_frame.grid_rowconfigure(1, weight = 1)



        #entry number area


        #recieve area

        self.recieve_label_frame = LabelFrame( self.main_label_frame, bg="Blue", relief=RIDGE)
        self.recieve_label_frame.grid(row=1,columnspan = 3, sticky="nsew")

        #messages

        self.list_box()



        #reply

        self.reply_entry = Entry( self.recieve_label_frame, relief=RIDGE, )
        self.reply_entry.grid(row=2, column=0, sticky="nsew", pady=5, )



        self.send_button = Button( self.recieve_label_frame, relief=RIDGE, text="SEND", command=lambda:
        [

            self.messages.append([self.getmessage(),3,E]),
            self.eventplacement()
        ])

        self.send_button.grid(row=2, column=2, sticky="nsew", pady=5, )

        #identify the phone
    def phone_name_identifier(self, name):
        self.unique_name = name

    def phone_number_identifier(self):

        self.unique_number = str(self.sim_num_entry.get())

    def reset_phone_identifier(self):
        self.unique_number = 0

    def getmessage(self):

        return (str(self.reply_entry .get()))

    def num_entry_frame(self):
        self.arr_alarm = []

        self.sim_num_entry = Entry(self.main_label_frame, relief=RIDGE, )
        self.sim_num_entry.grid(row=0, column=1, sticky="nsew", pady=5, )

        self.delete_button = Button(self.main_label_frame, relief=RIDGE, text="X", command=lambda:
        [
            self.delete_number(),
            self.enable_entry_submit(),
            self.listframe.destroy(),
            self.reset_phone_identifier(),
            self.list_box(),
            print(self.unique_number)


        ])
        self.delete_button.grid(row=0, column=0, sticky="nsew", pady=5, )

        self.submit_button = Button(self.main_label_frame, relief=RIDGE, text="SET", command=lambda:
        [

            # self.delete_number(),
            self.set_number.append([self.sim_num_entry.get(),self.unique_name]),
            print("Current number", self.set_number),
            self.phone_number_identifier(),
            self.disable_entry_submit(),
            print(self.unique_number)
        ])

        self.submit_button.grid(row=0, column=2, sticky="nsew", pady=5, )
    def return_phone_num(self,setnumcontroll):
        # print("this is the set num", self.set_number[0])

        return str(self.set_number[setnumcontroll][0])

    def list_box(self):


        self.recieve_label_frame.grid_columnconfigure(0, weight=1)

        self.listframe = Frame(self.recieve_label_frame, background="Green")
        self.listframe.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.labelevent = Label(self.listframe, text="This is Event Frame")
        self.labelevent.grid(row=0, column=0, )

        self.listframe.grid_rowconfigure(1, weight=1)
        self.listframe.grid_columnconfigure(0, weight=1)

        self.canvas = Canvas(self.listframe, borderwidth=0, background="Yellow")
        self.canvas.grid(row=1, column=0, sticky="nsew")

        self.canvas.grid_columnconfigure(0, weight=1)

        self.vsb = Scrollbar(self.listframe, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=1, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.widgetframe = Frame(self.canvas, bg = "yellow")
        self.widgetframe.grid(column=0, row=0, sticky="nsew")

        self.widgetframe.grid_columnconfigure(0, weight=1)

        self.xx = self.canvas.create_window((1, 1), window=self.widgetframe, anchor="nw")

        self.widgetframe.bind("<Configure>", lambda event, canvas=self.canvas:
        self.onFrameConfigure(self.canvas))

        self.canvas.bind('<Configure>', self.FrameWidth)
    #disable the entry for num and submit after submitting
    def disable_entry_submit(self):
        self.sim_num_entry.configure(state = "disable")
        self.submit_button.configure(state = "disable")

    def enable_entry_submit(self):
        self.sim_num_entry.configure(state = "normal")
        self.submit_button.configure(state = "normal")

    def delete_number(self):

        for x in range(len(self.set_number)):

            if self.set_number[x][1] == self.unique_name:
                del(self.set_number[x])
            else:
                pass
            print(self.set_number)

    def FrameWidth(self,e):

        self.canvas.itemconfig(self.xx, width = e.width )

    def onFrameConfigure(self, canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))




    def eventplacement(self):



        self.event_label.append(0)
        self.len_message = (len(self.messages)-1)

        # print("arr message", self.messages[0])
        # print("this is the lenght of message arr", self.len_message)
        # print("this is the x[0] of arr message",self.messages[self.len_message][0])

        self.event_label[self.len_message] = Label(self.widgetframe, text = str(self.messages[self.len_message][0]))
        self.event_label[self.len_message].grid(row = self.len_message, column = self.messages[self.len_message][1],
        sticky =self.messages[self.len_message][2] ,pady = 10, padx = 10)



        # print(Send_Notif.retarr)




    def tick_eventplacement(self):

            while self.top.winfo_exists() == 1:

                time.sleep(1)
                # print("retarr ",Send_Notif.retarr)
                # print("range retarr ",len(Send_Notif.retarr))
                if not Send_Notif.retarr == []:
                    for search_control_num in range(len(Send_Notif.retarr)):

                        if str(Send_Notif.retarr[search_control_num][3]) ==  str(self.unique_number):
                            self.messages.append(Send_Notif.retarr[search_control_num])
                            self.eventplacement()
                            Send_Notif.retarr[search_control_num][3] = 1


            print("thread of ", self.unique_name, "End")

    def tick_eventplacement_twenty(self):

            while self.top.winfo_exists() == 1:

                time.sleep(1)
                # print("retarr ",Send_Notif.retarr)
                # print("range retarr ",len(Send_Notif.retarr))
                if not Send_Notif.retarr_twenty == []:
                    for search_control_num in range(len(Send_Notif.retarr_twenty )):

                        if str(Send_Notif.retarr_twenty [search_control_num][3]) ==  str(self.unique_number):
                            self.messages.append(Send_Notif.retarr_twenty [search_control_num])
                            self.eventplacement()
                            Send_Notif.retarr_twenty [search_control_num][3] = 1



def donothing(phonename):
    phone_obj = Phone(root)
    phone_obj.phone_name_identifier(phonename)
    phone_obj.phone_frame(root)
    phone_obj.num_entry_frame()

    t1 = threading.Thread(target=phone_obj.tick_eventplacement)
    t1.start()
    t2 = threading.Thread(target=phone_obj.tick_eventplacement_twenty)
    t2.start()



#set the new phone obj a name
def set_phone_name():
    set_phone_name_top = Toplevel()
    set_name_label = Entry(set_phone_name_top)
    set_name_label.grid()
    confirm_button = Button(set_phone_name_top, text = "Confirm" ,command = lambda:
    [
        donothing(set_name_label.get()),
        set_phone_name_top.destroy()
    ])
    confirm_button.grid()


root = Tk()
x = Main_Page(root)

menubar = Menu(root)



filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Create Phone", command=set_phone_name)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
