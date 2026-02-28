# import datetime
# import time

# while True:
#     now = datetime.datetime.now()
#                  #for 24 hour format
#     # print(now.strftime("%H:%M:%S"), end="\r")       

#                 #for 12 hour format
#     print(now.strftime("%I:%M:%S"), end="\r")        
    
#     time.sleep(1)



# from tkinter import *
# import datetime

# root = Tk()
# root.geometry("400x300")
# root.config(bg="pink")

# # label = Label(root, font=("Arial", 30), bg="pink")
# # label.pack(pady=50)

# def clock():
#     now = datetime.datetime.now()
#     # current_time = now.strftime("%H:%M:%S")   # 24 hour format
#     current_time = now.strftime("%I:%M:%S %p")  # 12 hour format
#     label.config(text=current_time)
#     label.after(1000, clock)  # update every 1 second
   
# clock()
# # btn = Button(root, text="Press", command=clock)
# # btn.pack()
# root.mainloop()



from tkinter import *
import datetime

root = Tk()
root.geometry("400x400")
root.config(bg="black")
root.title("Digital Clock")


def clock():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    current_date=now.strftime(" %A \n%D")

    label.config(text=current_time)
    label.after(1000, clock)  # update every 1 second

    label_date.config(text=current_date)

label = Label(root, bg="black", fg="white",font=("arial",40))
label.pack()
label_date = Label(root, bg="black", fg="white",font=("arial",40))
label_date.pack()
clock()  

root.mainloop()