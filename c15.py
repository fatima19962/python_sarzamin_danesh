from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
import tkinter.ttk as ttk

root = Tk()
root.title("User Contact")

width = 700
height = 420
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height / 2))
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#0e0606")

# ---------------- متغیرهای فرم ----------------
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
CONTACT = StringVar()
ADDRESS = StringVar()

# شناسه رکورد انتخاب شده (مقدار اولیه)
mem_id = None

# ---------------- توابع دیتابیس ----------------
def Database():
    """بارگذاری و نمایش رکوردها در treeview"""
    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="pythontut")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS member(
                mem_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                firstname TEXT,
                lastname TEXT,
                gender TEXT,
                age TEXT,
                address TEXT,
                contact TEXT
            )
        """)
        cursor.execute("SELECT * FROM member ORDER BY lastname ASC")
        fetch = cursor.fetchall()
    except mysql.connector.Error as err:
        tkMessageBox.showerror("Database Error", f"اتصال به دیتابیس برقرار نشد:\n{err}")
        return
    finally:
        # بسته شدن cursor/conn اگر باز بودند (در except ممکن است قبلاً بسته نشده باشند)
        try:
            cursor.close()
            conn.close()
        except:
            pass

    # پاک کردن treeview قبل از درج
    tree.delete(*tree.get_children())
    for data in fetch:
        # data یک تاپل (mem_id, firstname, lastname, gender, age, address, contact)
        tree.insert('', 'end', values=data)


# --------- اعتبارسنجی ورودی‌ها ----------
def validate_inputs():
    """چک کند فیلدهای لازم پر شده باشند و سن/شماره تماس معتبر باشند"""
    if FIRSTNAME.get().strip() == "" or LASTNAME.get().strip() == "" or GENDER.get().strip() == "" or AGE.get().strip() == "" or CONTACT.get().strip() == "":
        tkMessageBox.showwarning("خطا", "لطفاً همه‌ی فیلدهای ضروری را پر کنید.")
        return False

    # سن باید عدد صحیح مثبت باشد
    if not AGE.get().isdigit() or int(AGE.get()) <= 0:
        tkMessageBox.showwarning("خطا", "سن باید یک عدد صحیح بزرگ‌تر از صفر باشد.")
        return False

    # شماره تماس: حداقل 7 و حداکثر 15 رقم (می‌توانید تغییر دهید)
    contact = CONTACT.get().strip()
    if not contact.isdigit() or not (7 <= len(contact) <= 15):
        tkMessageBox.showwarning("خطا", "شماره تماس باید فقط شامل ارقام باشد و طول آن بین 7 تا 15 رقم باشد.")
        return False

    return True


# ---------------- اضافه کردن رکورد ----------------
def SubmitData():
    if not validate_inputs():
        return

    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="pythontut")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO member(firstname,lastname,gender,age,address,contact) VALUES(%s,%s,%s,%s,%s,%s)",
            (FIRSTNAME.get().strip(), LASTNAME.get().strip(), GENDER.get().strip(), AGE.get().strip(), ADDRESS.get().strip(), CONTACT.get().strip())
        )
        conn.commit()
    except mysql.connector.Error as err:
        tkMessageBox.showerror("Database Error", f"خطا هنگام درج رکورد:\n{err}")
    else:
        ClearForm()
        Database()
        tkMessageBox.showinfo("موفق", "رکورد با موفقیت اضافه شد.")
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


# ---------------- انتخاب رکورد روی tree ----------------
def OnSelected(event):
    global mem_id
    # اطمینان از اینکه آیتمی انتخاب شده
    curItem = tree.focus()
    if not curItem:
        return
    contents = tree.item(curItem)
    selectedItem = contents.get('values', [])
    if not selectedItem:
        return

    # مقداردهی به فرم بر اساس سطر انتخاب شده
    mem_id = selectedItem[0]
    FIRSTNAME.set(selectedItem[1])
    LASTNAME.set(selectedItem[2])
    GENDER.set(selectedItem[3])
    AGE.set(selectedItem[4])
    ADDRESS.set(selectedItem[5])
    CONTACT.set(selectedItem[6])


# ---------------- بروزرسانی رکورد ----------------
def UpdateData():
    global mem_id
    if mem_id is None:
        tkMessageBox.showwarning("خطا", "هیچ رکوردی انتخاب نشده است!")
        return

    if not validate_inputs():
        return

    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="pythontut")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE member
            SET firstname=%s, lastname=%s, gender=%s, age=%s, address=%s, contact=%s
            WHERE mem_id=%s
        """, (FIRSTNAME.get().strip(), LASTNAME.get().strip(), GENDER.get().strip(), AGE.get().strip(), ADDRESS.get().strip(), CONTACT.get().strip(), mem_id))
        conn.commit()
    except mysql.connector.Error as err:
        tkMessageBox.showerror("Database Error", f"خطا هنگام به‌روزرسانی:\n{err}")
    else:
        ClearForm()
        Database()
        tkMessageBox.showinfo("موفق", "رکورد با موفقیت بروزرسانی شد.")
        mem_id = None
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


# ---------------- حذف رکورد ----------------
def DeleteData():
    global mem_id
    if mem_id is None:
        tkMessageBox.showwarning("خطا", "هیچ رکوردی انتخاب نشده است!")
        return

    result = tkMessageBox.askquestion("حذف", "آیا از حذف این رکورد مطمئن هستید؟", icon="warning")
    if result != "yes":
        return

    try:
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="pythontut")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM member WHERE mem_id=%s", (mem_id,))
        conn.commit()
    except mysql.connector.Error as err:
        tkMessageBox.showerror("Database Error", f"خطا هنگام حذف رکورد:\n{err}")
    else:
        ClearForm()
        Database()
        tkMessageBox.showinfo("موفق", "رکورد حذف شد.")
        mem_id = None
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


# ---------------- پاک کردن فرم ----------------
def ClearForm():
    global mem_id
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT.set("")
    mem_id = None


# ================== بخش رابط کاربری ===================
form = Frame(root, bg="#0e0606")
form.pack(side=TOP, pady=10, padx=10, anchor=W)

# ردیف‌ها و فیلدها
Label(form, text="First Name:", fg="white", bg="#0e0606").grid(row=0, column=0, sticky=W, padx=5, pady=2)
Entry(form, textvariable=FIRSTNAME, width=22).grid(row=0, column=1, padx=5, pady=2)

Label(form, text="Last Name:", fg="white", bg="#0e0606").grid(row=1, column=0, sticky=W, padx=5, pady=2)
Entry(form, textvariable=LASTNAME, width=22).grid(row=1, column=1, padx=5, pady=2)

Label(form, text="Gender:", fg="white", bg="#0e0606").grid(row=0, column=2, sticky=W, padx=5, pady=2)
ttk.Combobox(form, textvariable=GENDER, values=("Male", "Female"), state="readonly", width=18).grid(row=0, column=3, padx=5, pady=2)

Label(form, text="Age:", fg="white", bg="#0e0606").grid(row=1, column=2, sticky=W, padx=5, pady=2)
Entry(form, textvariable=AGE, width=22).grid(row=1, column=3, padx=5, pady=2)

Label(form, text="Address:", fg="white", bg="#0e0606").grid(row=2, column=0, sticky=W, padx=5, pady=2)
Entry(form, textvariable=ADDRESS, width=22).grid(row=2, column=1, padx=5, pady=2)

Label(form, text="Contact:", fg="white", bg="#0e0606").grid(row=2, column=2, sticky=W, padx=5, pady=2)
Entry(form, textvariable=CONTACT, width=22).grid(row=2, column=3, padx=5, pady=2)

# دکمه‌ها
btn_frame = Frame(root, bg="#0e0606")
btn_frame.pack(side=TOP, fill=X, padx=10, pady=5)

Button(btn_frame, text="Add", command=SubmitData, width=12).pack(side=LEFT, padx=6)
Button(btn_frame, text="Update", command=UpdateData, width=12).pack(side=LEFT, padx=6)
Button(btn_frame, text="Delete", command=DeleteData, width=12).pack(side=LEFT, padx=6)
Button(btn_frame, text="Clear", command=ClearForm, width=12).pack(side=LEFT, padx=6)

# ================== TreeView ===================
frame = Frame(root)
frame.pack(fill=BOTH, expand=True, padx=10, pady=(0,10))

scrollbary = Scrollbar(frame, orient=VERTICAL)
scrollbarx = Scrollbar(frame, orient=HORIZONTAL)

tree = ttk.Treeview(frame,
                    columns=("MemberID", "FirstName", "LastName", "Gender", "Age", "Address", "Contact"),
                    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set,
                    show="headings")

scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading("MemberID", text="ID", anchor=W)
tree.heading("FirstName", text="First Name", anchor=W)
tree.heading("LastName", text="Last Name", anchor=W)
tree.heading("Gender", text="Gender", anchor=W)
tree.heading("Age", text="Age", anchor=W)
tree.heading("Address", text="Address", anchor=W)
tree.heading("Contact", text="Contact", anchor=W)

tree.column("MemberID", width=50, anchor=W)
tree.column("FirstName", width=130, anchor=W)
tree.column("LastName", width=130, anchor=W)
tree.column("Gender", width=70, anchor=W)
tree.column("Age", width=60, anchor=W)
tree.column("Address", width=180, anchor=W)
tree.column("Contact", width=120, anchor=W)

tree.pack(fill=BOTH, expand=True)
tree.bind("<Double-1>", OnSelected)

# بارگذاری اولیه‌ی داده‌ها
Database()

root.mainloop()
