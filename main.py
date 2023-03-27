#libraries used
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3

#images used 
image1='1.jfif'
image2='1.jfif'
image3='1.jfif'
image5= 'bg.jpg'


#class menu
class menu:
    #menu constructor function
    def __init__(self):
        self.root=Tk()
        self.root.resizable(False, False)
        self.root.title('Menu')
        self.root.state('zoomed')
        conn=sqlite3.connect('test.db')
        conn.execute('''create table if not exists book_info
        (ID VARCHAR PRIMARY KEY NOT NULL,
        TITLE VARTEXT NOT NULL,
        AUTHOR VARTEXT NOT NULL,
        GENRE VARTEXT NOT NULL,
        COPIES VARINT NOT NULL,
        LOCATION VARCHAR NOT NULL);''')
        conn.commit()
        conn.execute('''create table if not exists book_issued
        (BOOK_ID VARCHAR NOT NULL,
        STUDENT_ID VARCHAR NOT NULL,
        ISSUE_DATE DATE NOT NULL,
        RETURN_DATE DATE NOT NULL,
        PRIMARY KEY (BOOK_ID,STUDENT_ID));''')
        conn.commit()
        conn.close()
        self.a=self.canvases(image1)

        # create a header frame
        # header_frame = Frame(self.a, bg='#2E8B57')
        # header_frame.grid(row=0, column=0, sticky='nsew')

        # create the header label
        header_label = Label(self.a, text='DASHBOARD\nWELCOME ADMIN', font=('Arial', 30), fg='#FFFFFF', bg='#373737', padx=30, pady=10, anchor='center', width=self.a.winfo_screenwidth())
        header_label.place(relx=0.5, anchor='center', rely=0.06)

        # create a frame to hold the buttons
        buttons_frame = Frame(self.a)
        buttons_frame.grid(row=1, column=0, sticky='nsew')
        buttons_frame.place(relx=0.5, rely=0.5, anchor='center')

        # create the manage book button
        manage_book_button = Button(buttons_frame,text='MANAGE BOOK',font='Arial 22 bold',fg='black',bg='white', bd=4 ,width=19,padx=10,borderwidth=0,command=self.book)
        manage_book_button.grid(row=0, column=0, padx=10, pady=10)

        # create the manage student button
        manage_student_button = Button(buttons_frame,text='MANAGE STUDENT',font='Arial 22 bold',fg='black',bg='white',width=19,padx=10,borderwidth=0,command=self.student)
        manage_student_button.grid(row=0, column=1, padx=10, pady=10)

        # configure the columns in the buttons frame to have equal weight
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        self.root.mainloop()

    #canvas function for displaying the background image
    def canvases(self,images):
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        #photo=PhotoImage(file=images)
        photo=Image.open(images)
        photo1=photo.resize((w,h),Image.ANTIALIAS)
        photo2=ImageTk.PhotoImage(photo1)

        #photo2 = ImageTk.PhotoImage(Image.open(images).resize((w, h)),Image.ANTIALIAS)
        self.canvas = Canvas(self.root, width='%d'%w, height='%d'%h)
        self.canvas.grid(row = 0, column = 0)
        self.canvas.grid_propagate(0)
        self.canvas.create_image(0, 0, anchor = NW, image=photo2)
        self.canvas.image=photo2
        return self.canvas
    
    #book function for displaying the manage books
    def book(self):
        self.a.destroy()
        self.a=self.canvases(image2)

        # create a frame to hold the buttons
        buttons_frame = Frame(self.a)
        buttons_frame.place(relx=0.5, rely=0.5, anchor='center')

        # create the add books button
        add_books_button = Button(buttons_frame,text='Add Books',font='Arial 22 bold',fg='black',bg='#B0E0E6',width=15,padx=10,pady=25,command=self.addbook)
        add_books_button.pack(side='left', padx=10, pady=10)

        # create the search books button
        search_books_button = Button(buttons_frame,text='Search Books',font='Arial 22 bold',fg='black',bg='#98FB98',width=15,padx=10,pady=25,command=self.search)
        search_books_button.pack(side='left', padx=10, pady=10)

        # create the all books button
        all_books_button = Button(buttons_frame,text='All Books',font='Arial 22 bold',fg='black',bg='#F0E68C',width=15,padx=10,pady=25,command=self.all)
        all_books_button.pack(side='left', padx=10, pady=10)

        # create the back to main menu button
        back_button = Button(self.a,text='Back to Main Menu',font='Arial 22 bold',fg='black',bg='white',width=15,padx=10,command=self.mainmenu)
        back_button.place(x=950,y=510)

    #book function for displaying the add book functionality
    def addbook(self):
        self.aid=StringVar()
        self.aauthor=StringVar()
        self.aname=StringVar()
        self.acopies=IntVar()
        self.agenre=StringVar()
        self.aloc=StringVar()
        self.f1=Frame(self.a,height=500,width=700,bg='white')
        self.f1.place(x=10,y=10)
        l1=Label(self.f1,text='Book ID ',font='Arial 12 bold',fg='black',bg='white',pady=1).place(x=100,y=50)
        e1=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.aid).place(x=310,y=50)
        l2=Label(self.f1,text='Book Title ',font='Arial 12 bold',fg='black',bg='white',pady=1).place(x=100,y=100)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.aname).place(x=310,y=100)
        l3=Label(self.f1,text='Book Author ',font='Arial 12 bold',fg='black',bg='white',pady=1).place(x=100,y=150)
        e3=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.aauthor).place(x=310,y=150)
        l4=Label(self.f1,text='Book Genre ',font='Arial 12 bold',fg='black',bg='white',pady=1).place(x=100,y=200)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.agenre).place(x=310,y=200)
        l4=Label(self.f1,text='No. Copies ',font='Arial 12 bold',fg='black',bg='white',pady=1).place(x=100,y=250)
        e2=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.acopies).place(x=310,y=250)
        l5=Label(self.f1,text='Location ',font='Arial 12 bold',fg='black',bg='white',pady=1).place(x=100,y=300)
        e3=Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.aloc).place(x=310,y=300)
        self.f1.grid_propagate(0)
        b1=Button(self.f1,text='ADD',font='Arial 10 bold',fg='black',bg='white',width=15,bd=3,command=self.adddata).place(x=200,y=400)
        b2=Button(self.f1,text='BACK',font='Arial 10 bold',fg='black',bg='white',width=15,bd=3,command=self.rm).place(x=400,y=400)
    #for removing and destroying the form pop up
    def rm(self):
        self.f1.destroy()
        
    #book function for displaying the main menu
    def mainmenu(self):
        self.root.destroy()
        a=menu()

    #book function for adding data
    def adddata(self):
        a=self.aid.get()
        b=self.aname.get()
        c=self.aauthor.get()
        d=self.agenre.get()
        e=self.acopies.get()
        f=self.aloc.get()
        conn=sqlite3.connect('test.db')
        try:
            if (a and b and c and d  and f)=="":
                messagebox.showinfo("Error","Fields cannot be empty.")
            else:
                conn.execute("insert into book_info \
                values (?,?,?,?,?,?)",(a.capitalize(),b.capitalize(),c.capitalize(),d.capitalize(),e,f.capitalize(),));
                conn.commit()
                messagebox.showinfo("Success","Book added successfully")
        except sqlite3.IntegrityError:
            messagebox.showinfo("Error","Book is already present.")


        conn.close()

    # unction for displaying the searching books
    def search(self):
        #self.search.state('zoomed')
        self.sid=StringVar()
        self.f1=Frame(self.a,height=500,width=650,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID/Title/Author/Genre: ',font=('Arial 10 bold'),bd=2, fg='white',bg='black').place(x=20,y=40)
        e1=Entry(self.f1,width=25,bd=5,bg='white',fg='black',textvariable=self.sid).place(x=260,y=40)
        b1=Button(self.f1,text='Search',bg='white',font='Arial 10 bold',width=9,bd=2,command=self.serch1).place(x=500,y=37)
        b1=Button(self.f1,text='Back',bg='white',font='Arial 10 bold',width=10,bd=2,command=self.rm).place(x=250,y=450)

    def create_tree(self,plc,lists):
        self.tree=ttk.Treeview(plc,height=13,column=(lists),show='headings')
        n=0
        while n is not len(lists):
            self.tree.heading("#"+str(n+1),text=lists[n])
            self.tree.column(""+lists[n],width=100)
            n=n+1
        return self.tree

    #book function for searching
    def serch1(self):
        k=self.sid.get()
        if k!="":
            self.list4=("BOOK ID","TITLE","AUTHOR","GENRE","COPIES","LOCATION")
            self.trees=self.create_tree(self.f1,self.list4)
            self.trees.place(x=25,y=150)
            conn=sqlite3.connect('test.db')

            c=conn.execute("select * from book_info where ID=? OR TITLE=? OR AUTHOR=? OR GENRE=?",(k.capitalize(),k.capitalize(),k.capitalize(),k.capitalize(),))
            a=c.fetchall()
            if len(a)!=0:
                for row in a:

                    self.trees.insert("",END,values=row)
                conn.commit()
                conn.close()
                self.trees.bind('<<TreeviewSelect>>')
                self.variable = StringVar(self.f1)
                self.variable.set("Select Action:")


                self.cm =ttk.Combobox(self.f1,textvariable=self.variable ,state='readonly',font='Arial 15 bold',height=50,width=15,)
                self.cm.config(values =('Add Copies', 'Delete Copies', 'Delete Book'))

                self.cm.place(x=50,y=100)
                self.cm.pack_propagate(0)


                self.cm.bind("<<ComboboxSelected>>",self.combo)
                self.cm.selection_clear()
            else:
                messagebox.showinfo("Error","Data not found")



        else:
            messagebox.showinfo("Error","Search field cannot be empty.")

    #function for displaying the combo box or the drop down actions
    def combo(self,event):
        self.var_Selected = self.cm.current()
        if self.var_Selected==0:
            self.copies(self.var_Selected)
        elif self.var_Selected==1:
            self.copies(self.var_Selected)
        elif self.var_Selected==2:
            self.deleteitem()

    #book function for displaying the deleting a book
    def deleteitem(self):
        try:
            self.curItem = self.trees.focus()

            self.c1=self.trees.item(self.curItem,"values")[0]
            b1=Button(self.f1,text='Update',font='Arial 10 bold',width=9,bd=3,command=self.delete2).place(x=500,y=97)

        except:
            messagebox.showinfo("Empty","Please select something.")
    def delete2(self):
        conn=sqlite3.connect('test.db')
        cd=conn.execute("select * from book_issued where BOOK_ID=?",(self.c1,))
        ab=cd.fetchall()
        if ab!=0:
            conn.execute("DELETE FROM book_info where ID=?",(self.c1,));
            conn.commit()
            messagebox.showinfo("Successful","Book Deleted sucessfully.")
            self.trees.delete(self.curItem)
        else:
            messagebox.showinfo("Error","Book is Issued.\nBook cannot be deleted.")
        conn.commit()
        conn.close()

    #function for displaying the copies of books
    def copies(self,varr):
        try:
            curItem = self.trees.focus()
            self.c1=self.trees.item(curItem,"values")[0]
            self.c2=self.trees.item(curItem,"values")[4]
            self.scop=IntVar()
            self.e5=Entry(self.f1,width=20,textvariable=self.scop)
            self.e5.place(x=310,y=100)
            if varr==0:
                b5=Button(self.f1,text='Update',font='Arial 10 bold',bg='white',fg='black',width=9,bd=3,command=self.copiesadd).place(x=500,y=97)
            if varr==1:
                b6=Button(self.f1,text='Update',font='Arial 10 bold',bg='white',fg='black',width=9,bd=3,command=self.copiesdelete).place(x=500,y=97)
        except:
            messagebox.showinfo("Empty","Please select something.")
            
    #book function for displaying adding the copies of the book
    def copiesadd(self):
        no=self.e5.get()
        if int(no)>=0:

            conn=sqlite3.connect('test.db')

            conn.execute("update book_info set COPIES=COPIES+? where ID=?",(no,self.c1,))
            conn.commit()

            messagebox.showinfo("Updated","Copies added sucessfully.")
            self.serch1()
            conn.close()

        else:
            messagebox.showinfo("Error","No. of copies cannot be negative.")

    #function for deleting the copies of the book
    def copiesdelete(self):
        no1=self.e5.get()
        if int(no1)>=0:
            if int(no1)<=int(self.c2):
                conn=sqlite3.connect('test.db')

                conn.execute("update book_info set COPIES=COPIES-? where ID=?",(no1,self.c1,))
                conn.commit()
                conn.close()

                messagebox.showinfo("Updated","Deleted sucessfully")
                self.serch1()

            else:
                messagebox.showinfo("Maximum","No. of copies to delete exceed available copies.")
        else:
            messagebox.showinfo("Error","No. of copies cannot be negative.")

    #function for displaying all the books
    def all(self):
        self.f1=Frame(self.a,height=500,width=650,bg='black')
        self.f1.place(x=500,y=100)
        b1=Button(self.f1,text='Back',bg='white' ,fg='black',width=10,bd=3,command=self.rm).place(x=250,y=400)
        conn=sqlite3.connect('test.db')
        self.list3=("BOOK ID","TITLE","AUTHOR","GENRE","COPIES","LOCATION")
        self.treess=self.create_tree(self.f1,self.list3)
        self.treess.place(x=25,y=50)
        c=conn.execute("select * from book_info")
        g=c.fetchall()
        if len(g)!=0:
            for row in g:
                self.treess.insert('',END,values=row)
        conn.commit()
        conn.close()
        
    #function for displaying the manage student menu
    def student(self):
        self.a.destroy()
        self.a=self.canvases(image2)
        l1=Button(self.a,text='Issue book',font='Arial 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.issue).place(x=12,y=100)
        l2=Button(self.a,text='Return Book',font='Arial 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.returnn).place(x=12,y=200)
        l3=Button(self.a,text='Student Activity',font='Arial 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.activity).place(x=12,y=300)
        l4=Button(self.a,text='Back to Menu',font='Arial 22 bold',fg='white',bg='Black',width=15,padx=10,command=self.mainmenu).place(x=12,y=600)

    #function for the issuing of the books
    def issue(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()
        self.f1=Frame(self.a,height=550,width=500,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='Arial 15 bold',bg='black',fg='white').place(x=50,y=100)
        e1=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.aidd).place(x=180,y=100)
        l2=Label(self.f1,text='Student Id : ',font='Arial 15 bold',bg='black',fg='white').place(x=50,y=150)
        e2=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=150)
        b1=Button(self.f1,text='Back',font='Arial 10 bold',fg='black',bg='white',width=10,bd=3,command=self.rm).place(x=50,y=250)
        b1=Button(self.f1,text='Issue',font='Arial 10 bold',fg='black',bg='white',width=10,bd=3,command=self.issuedbook).place(x=200,y=250)

    #function for displaying the manage student menu
    def issuedbook(self):
        bookid=self.aidd.get()
        studentid=self.astudentt.get()
        conn=sqlite3.connect('test.db')
        cursor=conn.cursor()
        cursor.execute("select ID,COPIES from book_info where ID=?",(bookid.capitalize(),))
        an=cursor.fetchall()
        if (bookid and studentid!=""):
            if an!=[]:
                for i in an:
                    if i[1]>0:
                        try:
                            conn.execute("insert into book_issued \
                            values (?,?,date('now'),date('now','+7 day'))",(bookid.capitalize(),studentid.capitalize(),));
                            conn.commit()
                            conn.execute("update book_info set COPIES=COPIES-1 where ID=?",(bookid.capitalize(),))
                            conn.commit()
                            conn.close()
                            messagebox.showinfo("Updated","Book Issued sucessfully.")
                        except:
                            messagebox.showinfo("Error","Book is already issued by student.")

                    else:
                        messagebox.showinfo("Unavailable","Book unavailable.\nThere are 0 copies of the book.")
            else:
                messagebox.showinfo("Error","No such Book in Database.")
        else:
            messagebox.showinfo("Error","Fields cannot be blank.")

    #function the return of books display
    def returnn(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()

        self.f1=Frame(self.a,height=550,width=500,bg='black')
        self.f1.place(x=500,y=100)
        l1=Label(self.f1,text='Book ID : ',font='Arial 15 bold',fg='white', bg='black').place(x=50,y=100)
        e1=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.aidd).place(x=180,y=100)
        l2=Label(self.f1,text='Student Id : ',font='Arial 15 bold',fg='white', bg='black').place(x=50,y=150)
        e2=Entry(self.f1,width=25,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=150)
        b1=Button(self.f1,text='Back',font='Arial 10 bold',bg='white',fg='black',width=10,bd=3,command=self.rm).place(x=50,y=250)
        b1=Button(self.f1,text='Return',font='Arial 10 bold',bg='white',fg='black',width=10,bd=3,command=self.returnbook).place(x=200,y=250)
        self.f1.grid_propagate(0)

    #function returning the book and connecting to the database 
    def returnbook(self):
        a=self.aidd.get()
        b=self.astudentt.get()

        conn=sqlite3.connect('test.db')

        fg=conn.execute("select ID from book_info where ID=?",(a.capitalize(),))
        fh=fg.fetchall()
        conn.commit()
        if fh!=None:
            c=conn.execute("select * from book_issued where BOOK_ID=? and STUDENT_ID=?",(a.capitalize(),b.capitalize(),))
            d=c.fetchall()
            conn.commit()
            if len(d)!=0:
                c.execute("DELETE FROM book_issued where BOOK_ID=? and STUDENT_ID=?",(a.capitalize(),b.capitalize(),));
                conn.commit()
                conn.execute("update book_info set COPIES=COPIES+1 where ID=?",(a.capitalize(),))
                conn.commit()

                messagebox.showinfo("Success","Book Returned sucessfully.")
            else:
                messagebox.showinfo("Error","Data not found.")
        else:
            messagebox.showinfo("Error","No such book.\nPlease add the book in database.")
        conn.commit()
        conn.close()

    #function for displaying the student activity
    def activity(self):
        self.aidd=StringVar()
        self.astudentt=StringVar()
        self.f1=Frame(self.a,height=550,width=500,bg='black')
        self.f1.place(x=500,y=80)
        self.list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE")
        self.trees=self.create_tree(self.f1,self.list2)
        self.trees.place(x=50,y=150)


        l1=Label(self.f1,text='Book/Student ID : ',font='Arial 15 bold',fg='white',bg='black').place(x=50,y=30)
        e1=Entry(self.f1,width=20,bd=4,bg='white',textvariable=self.aidd).place(x=280,y=35)
        #l2=Label(self.f1,text='Student Id : ',font='Arial 15 bold',fg='white',bg='black').place(x=50,y=80)
        #e2=Entry(self.f1,width=20,bd=4,bg='white',textvariable=self.astudentt).place(x=180,y=80)
        b1=Button(self.f1,text='Back',bg='white',font='Arial 10 bold',width=10,bd=3,command=self.rm).place(x=340,y=450)
        b1=Button(self.f1,text='Search',bg='white',font='Arial 10 bold',width=10,bd=3,command=self.searchact).place(x=40,y=450)
        b1=Button(self.f1,text='All',bg='white',font='Arial 10 bold',width=10,bd=3,command=self.searchall).place(x=190,y=450)
        self.f1.grid_propagate(0)

    #function for displaying the searched student activity
    def searchact(self):
        self.list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE")
        self.trees=self.create_tree(self.f1,self.list2)
        self.trees.place(x=50,y=150)
        conn=sqlite3.connect('test.db')
        bid=self.aidd.get()

        try:
            c=conn.execute("select * from book_issued where BOOK_ID=? or STUDENT_ID=?",(bid.capitalize(),bid.capitalize(),))
            d=c.fetchall()
            if len(d)!=0:
                for row in d:
                    self.trees.insert("",END,values=row)
            else:
                messagebox.showinfo("Error","Data not found.")
            conn.commit()

        except Exception as e:
            messagebox.showinfo(e)
        conn.close()

    #function for searching all in the student activity
    def searchall(self):
        self.list2=("BOOK ID","STUDENT ID","ISSUE DATE","RETURN DATE")
        self.trees=self.create_tree(self.f1,self.list2)
        self.trees.place(x=50,y=150)
        conn=sqlite3.connect('test.db')
        try:
            c=conn.execute("select * from book_issued")
            d=c.fetchall()
            for row in d:
                self.trees.insert("",END,values=row)

            conn.commit()

        except Exception as e:
            messagebox.showinfo(e)
        conn.close()

#===================START=======================
#canvas function for displaying the image in the login background
def canvases(images,w,h):
    photo=Image.open(images)
    photo1=photo.resize((w,h),Image.ANTIALIAS)
    photo2=ImageTk.PhotoImage(photo1)

    canvas = Canvas(root, width='%d'%w, height='%d'%h)
    canvas.grid(row = 0, column = 0)
    canvas.grid_propagate(0)
    canvas.create_image(0, 0, anchor = NW, image=photo2)
    canvas.image=photo2
    return canvas

# initializing the root of tkinter
root = Tk()
root.title("LOGIN")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
canvas=canvases(image5,w,h)

#creating the Login Text Display for the Login
canvas.create_text(w//2, 200, text="Library Management", fill="white", font=("TkDefaultFont", 35,"bold", ))
canvas.create_text(w//2, 250, text="System", fill="white", font=("Arial", 35,"bold", ))


#==============================METHODS========================================
#setting the database
def Database():
    global conn, cursor
    conn = sqlite3.connect("python1.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `login` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
    cursor.execute("SELECT * FROM `login` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `login` (username, password) VALUES('admin', 'admin')")
        conn.commit()

#function for displaying the Login
def Login(event=None):
    Database()


    if USERNAME.get() == "" or PASSWORD.get() == "":
        messagebox.showinfo("Error","Please complete the required field!")
    else:
        cursor.execute("SELECT * FROM `login` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            #HomeWindow()
            #Top.destroy()
            root.destroy()

            #print("hello logged in ")
            a=menu()
            #USERNAME.set("")
            #PASSWORD.set("")
            #lbl_text.config(text="")
        else:
            messagebox.showinfo("Error","Invalid username or password.")
            #lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()


#===============GLOBAL VARIABLES======================
USERNAME = StringVar()
PASSWORD = StringVar()


#===========================Layout=========================
#configuring root layout with columns
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create a frame for the login form
login_frame = tk.Frame(root, bg="#ffffff", bd=1, relief=tk.SOLID, padx=20, pady=20)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

# create a label for the login title
login_label = tk.Label(login_frame, bg="white",text="Login", font=("TkDefaultFont", 24), pady=10)
login_label.grid(row=0, column=0, columnspan=3, rowspan=1)

# create a label for the username field
username_label = tk.Label(login_frame, text="Username:", bg="#ffffff", font=20)
username_label.grid(row=1, column=0, padx=5, pady=5)

# create an entry widget for the username field
username_entry = tk.Entry(login_frame, textvariable=USERNAME, font=("TkDefaultFont", 16))
username_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
username_entry.insert(0, "")

# create a label for the password field
password_label = tk.Label(login_frame, text="Password:", bg="#ffffff", font=20)
password_label.grid(row=2, column=0, padx=5, pady=5)

# create an entry widget for the password field
password_entry = tk.Entry(login_frame, show="*", textvariable=PASSWORD, font=("TkDefaultFont", 16))
password_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
password_entry.insert(0, "")

# create a login button
login_button = tk.Button(login_frame, text="Login", bg="#ffffff", bd=0, highlightthickness=0, command=Login)
login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

# configure the login button to have a rounded shape
login_button.config(borderwidth=0, relief="solid", highlightthickness=0, bd=0)
login_button.config(bg="#ffffff", activebackground="#cccccc")
login_button.config(fg="#333333", activeforeground="#333333")
login_button.config(font=("TkDefaultFont", 14), width=20, height=2)
login_button.config(bd=2, highlightcolor="#333333")
login_button.bind('<Return>', Login)

# make the login form wider and taller
login_frame.config(width=800, height=400)

#setting resizability to false
root.resizable(False, False)
root.mainloop()

