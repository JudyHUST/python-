from asyncore import read
from html.entities import name2codepoint
from tkinter import *
from tkinter import messagebox
import numpy as np
import csv

def info_input(e):
    with open(filename, 'r+', newline='') as csvfile:
        info_list = [e]
        csv.reader(csvfile)
        # print(reader)
        writer = csv.writer(csvfile)
        writer.writerows(info_list)


def grade_rev(name_res,e):
    name_res = int(name_res)
    with open(filename,'r+',newline='') as csvfile:
        info_list = [[]]
        reader = list(csv.reader(csvfile))
    e = e+[reader[name_res+1][6]]
    #print(e)
    with open(filename,'w+',newline='') as csvfile:
        info_list[:name_res+1] = reader[:name_res+1]
        info_list = info_list + [e] + reader[name_res+2:]
        writer = csv.writer(csvfile)
        writer.writerows(info_list)

def info_query(name_res):
    name_res = int(name_res)
    with open(filename, 'r+', newline='') as csvfile:
        reader = list(csv.reader(csvfile))
    return reader[name_res+1]


def search(item,column):
    with open(filename,'r') as csvfile:
        reader = np.array(list(csv.reader(csvfile)))[1:,column]
        for _item in reader:
            if _item == item:
                return np.argwhere(reader == item)
        return -1

# 注册
def page_register():
    pr = Tk()
    pr.title('注册')
    pr.geometry('400x300')

    l1 = Label(pr,text='注册页面', bg='ghostwhite', fg='red', font=32)
    l1.place(x=150, y=50)
    l2 = Label(pr,text='姓名', bg='ghostwhite', fg='red', font=22)
    l2.place(x=50, y=100)
    l3 = Label(pr,text='学号', bg='ghostwhite', fg='red', font=22)
    l3.place(x=50, y=140)
    l3 = Label(pr,text='密码', bg='ghostwhite', fg='red', font=22)
    l3.place(x=50, y=180)


    e1 = Entry(pr, bg='white')
    e1.place(x=120, y=100)
    e2 = Entry(pr,bg='white')
    e2.place(x=120, y=140)
    e3 = Entry(pr,bg='white')
    e3.place(x=120, y=180)


    b1 = Button(pr, text="注册", height=1, width=5, command=lambda:reg(e1,e2,e3,pr), bg='azure')
    b1.place(x=130, y=220)
    b2 = Button(pr, text="清空", height=1, width=5, command=clr, bg='azure')
    b2.place(x=190, y=220)
    b3 = Button(pr, text="退出", height=1, width=5, command=lambda:pr.destroy(), bg='azure')
    b3.place(x=250, y=220)
    
def reg(e1,e2,e3,pr):
    name = e1.get()
    num = e2.get()
    password = e3.get()
    # print(name)
    name_res = search(name,0)
    num_res = search(num,1)
    # print(name_res)
    # print(num_res)
    if name_res >=0 and num_res == name_res:
        messagebox.showinfo(title='注册提示', message="账号已存在")
    elif name_res ==num_res and name_res <0:
        messagebox.showinfo(title='注册提示', message="注册成功")
        info_input([name,num,0,0,0,0,password])
        pr.destroy()
    else:
        messagebox.showinfo(title='注册提示', message="学号或姓名已存在")

# 登录
def login():
    name = ee1.get()
    password = ee2.get()
    name_res = search(name,0)
    password_res = search(password,6)
    # print(name_res)
    # print(password_res)
    if name_res == password_res and name_res >=0:
        messagebox.showinfo(title='登陆提示', message="登陆成功")
        page_manage(name_res)
    else:
        messagebox.showinfo(title='登陆提示', message="姓名或密码错误，请重新登录")


# 清空
def clr():
    ee1.delete('0', len(list(ee1.get())))
    ee2.delete('0', len(list(ee2.get())))


# 管理页面
def page_manage(name_res):
    root.destroy()
    pm = Tk()
    pm.title('学生信息管理系统')
    pm.geometry('400x300')

    b1 = Button(pm, text="个人成绩录入", command=page_save, bg='azure')
    b1.place(x=30, y=40)
    b2 = Button(pm, text="个人成绩查询", command=page_query, bg='azure')
    b2.place(x=30, y=100)
    b3 = Button(pm, text="个人成绩统计", command=lambda:page_stu(name_res), bg='azure')
    b3.place(x=30, y=160)
    b4 = Button(pm, text="班级成绩统计", command=lambda:page_class(name_res), bg='azure')
    b4.place(x=30, y=220)

    b5 = Button(pm, text="返回", height=1, width=5, command=lambda:pm.destroy(), bg='azure')
    b5.place(x=190, y=265)


def page_save():
    ps = Tk()
    ps.title('录入学生成绩')
    ps.geometry('400x300')


    l = Label(ps, text='请录入学生成绩', bg='ghostwhite', fg='red', font=32)
    l.place(x=130, y=15)

    l = Label(ps, text='姓名', width=6, bg='lightyellow')
    l.place(x=30, y=40)
    e1 = Entry(ps)
    e1.place(x=85, y=40)

    l = Label(ps, text='学号', width=6, bg='lightyellow')
    l.place(x=30, y=80)
    e2 = Entry(ps)
    e2.place(x=85, y=80)

    l = Label(ps, text='C语言', width=6, bg='lightyellow')
    l.place(x=30, y=120)
    e3 = Entry(ps)
    e3.place(x=85, y=120)

    l = Label(ps, text='python', width=6, bg='lightyellow')
    l.place(x=30, y=160)
    e4 = Entry(ps)
    e4.place(x=85, y=160)

    l = Label(ps, text='微积分', width=6, bg='lightyellow')
    l.place(x=30, y=200)
    e5 = Entry(ps)
    e5.place(x=85, y=200)

    l = Label(ps, text='物理', width=6, bg='lightyellow')
    l.place(x=30, y=240)
    e6 = Entry(ps)
    e6.place(x=85, y=240)

    b1 = Button(ps, text="录入", height=1, width=5, command=lambda:grade_save([e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()],ps), bg='azure')
    b1.place(x=130, y=265)
    b2 = Button(ps, text="返回", height=1, width=5, command=lambda:ps.destroy(), bg='azure')
    b2.place(x=190, y=265)

def grade_save(e,ps):
    name_res = search(e[0],0)
    num_res = search(e[1],1)
    if name_res >=0 and num_res == name_res:
        grade_rev(name_res,e)
        messagebox.showinfo(title='修改提示', message="修改成功")
        ps.destroy()
    else:
        messagebox.showinfo(title='修改提示', message="学号或姓名有误")



def page_query():
    pq = Tk()
    pq.title('查询学生成绩')
    pq.geometry('400x300')
    
    l = Label(pq, text='姓名', width=6, bg='lightyellow')
    l.place(x=30, y=40)

    l = Label(pq, text='学号', width=6, bg='lightyellow')
    l.place(x=30, y=80)

    _e1 = Entry(pq,bg='white')
    _e1.place(x=85, y=40)
    _e2 = Entry(pq,show='*', bg='white')
    _e2.place(x=85, y=80)
    
    b1 = Button(pq, text='查询', width=6, command=lambda:grade_query(_e1,_e2,pq), bg='azure')
    b1.place(x=330, y=40)

    b5 = Button(pq, text="返回", height=1, width=5, command=lambda:pq.destroy(), bg='azure')
    b5.place(x=190, y=265)


def grade_query(_e1,_e2,pq):
    name = _e1.get()
    num = _e2.get()

    name_res = search(name,0)
    num_res = search(num,1)

    if name_res >=0 or num_res >=0:
        if name_res == num_res:
            info = info_query(name_res)
            l = Label(pq, text='C语言', width=6, bg='lightyellow')
            l.place(x=30, y=120)
            
            l = Label(pq, text=info[2], width=6, bg='lightyellow')
            l.place(x=85, y=120)

            l = Label(pq, text='python', width=6, bg='lightyellow')
            l.place(x=30, y=160)

            l = Label(pq, text=info[3], width=6, bg='lightyellow')
            l.place(x=85, y=160)

            l = Label(pq, text='微积分', width=6, bg='lightyellow')
            l.place(x=30, y=200)

            l = Label(pq, text=info[4], width=6, bg='lightyellow')
            l.place(x=85, y=200)

            l = Label(pq, text='物理', width=6, bg='lightyellow')
            l.place(x=30, y=240)

            l = Label(pq, text=info[5], width=6, bg='lightyellow')
            l.place(x=85, y=240)

            

        else:
            messagebox.showinfo(title='查询提示', message="学号与姓名不符")
    else:
        messagebox.showinfo(title='查询提示', message="未查询到信息")
    
def info_cal(name_res):
    name_res = int(name_res)
    with open(filename, 'r+', newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        info = reader[name_res+1]
    # print(reader)

    grade_j = []
    avg = []
    seq_me = []
    for j in range(2,6):
        tot_grade = 0
        tot_num = 0
        grade_j = [(-int(item[j])) for item in reader[1:]]
        # print(grade_j)
        for i in grade_j:
            if i <0:
                tot_grade += i
                tot_num += 1
        # print(tot_grade)
        # print(tot_num)
        if tot_num >0:
            avg += [-(tot_grade / tot_num)]
        else:
            avg += [-1]
        # print(avg)
        grade_seq = np.array(grade_j).argsort()
        # print(grade_seq)
        seq_me += [grade_seq[name_res]+1]
    grade_tot = np.array([-int(item[2])-int(item[3])-int(item[4])-int(item[5]) for item in reader[1:]])
    # print(grade_tot)
    avg_tot = grade_tot.mean()

    class_seq = grade_tot.argsort()[name_res]+1
    info_me = [-grade_tot[name_res],seq_me,class_seq,-avg_tot,avg]
    # print(info_me)
    return info_me

def page_stu(name_res):
    pts = Tk()
    pts.title('学生成绩')
    pts.geometry('400x300')

    info = info_cal(name_res)

    l = Label(pts, text='总分', width=6, bg='lightyellow')
    l.place(x=30, y=40)

    l = Label(pts, text=info[0], width=6, bg='lightyellow')
    l.place(x=205, y=40)

    l = Label(pts, text='班级排名', width=6, bg='lightyellow')
    l.place(x=30, y=80)

    l = Label(pts, text=info[2], width=6, bg='lightyellow')
    l.place(x=205, y=80)

    l = Label(pts, text='c语言排名', width=10, bg='lightyellow')
    l.place(x=30, y=120)

    l = Label(pts, text=info[1][0], width=6, bg='lightyellow')
    l.place(x=205, y=120)

    l = Label(pts, text='python排名', width=20, bg='lightyellow')
    l.place(x=30, y=160)

    l = Label(pts, text=info[1][1], width=6, bg='lightyellow')
    l.place(x=205, y=160)

    l = Label(pts, text='微积分排名', width=20, bg='lightyellow')
    l.place(x=30, y=200)

    l = Label(pts, text=info[1][2], width=6, bg='lightyellow')
    l.place(x=205, y=200)

    l = Label(pts, text='物理排名', width=20, bg='lightyellow')
    l.place(x=30, y=240)

    l = Label(pts, text=info[1][3], width=6, bg='lightyellow')
    l.place(x=205, y=240)

    b2 = Button(pts, text="返回", height=1, width=5, command=lambda:pts.destroy(), bg='azure')
    b2.place(x=190, y=265)

def page_class(name_res):
    ptc = Tk()
    ptc.title('班级成绩')
    ptc.geometry('400x300')

    info = info_cal(name_res)

    l = Label(ptc, text='班级总分均分', width=15, bg='lightyellow')
    l.place(x=30, y=40)

    l = Label(ptc, text=info[3], width=6, bg='lightyellow')
    l.place(x=205, y=40)

    l = Label(ptc, text='c语言均分', width=15, bg='lightyellow')
    l.place(x=30, y=80)

    l = Label(ptc, text=info[4][0], width=6, bg='lightyellow')
    l.place(x=205, y=80)

    l = Label(ptc, text='python均分与极值', width=15, bg='lightyellow')
    l.place(x=30, y=120)

    l = Label(ptc, text=info[4][1], width=6, bg='lightyellow')
    l.place(x=205, y=120)

    l = Label(ptc, text='微积分均分', width=15, bg='lightyellow')
    l.place(x=30, y=160)

    l = Label(ptc, text=info[4][2], width=6, bg='lightyellow')
    l.place(x=205, y=160)

    l = Label(ptc, text='物理均分', width=15, bg='lightyellow')
    l.place(x=30, y=200)

    l = Label(ptc, text=info[4][3], width=6, bg='lightyellow')
    l.place(x=205, y=200)

    b2 = Button(ptc, text="返回", height=1, width=5, command=lambda:ptc.destroy(), bg='azure')
    b2.place(x=190, y=265)


filename = "new.csv"

root = Tk()
root.title('主界面')
root.geometry('400x300')

l1 = Label(text='学生信息管理系统', bg='ghostwhite', fg='red', font=32)
l1.place(x=130, y=50)
l2 = Label(text='姓名', bg='ghostwhite', fg='red', font=22)
l2.place(x=50, y=140)
l3 = Label(text='密码', bg='ghostwhite', fg='red', font=22)
l3.place(x=50, y=180)

user = StringVar()
ee1 = Entry(root, textvariable=user, bg='white')
ee1.place(x=120, y=140)
password = StringVar()
ee2 = Entry(root, textvariable=password, show='*', bg='white')
ee2.place(x=120, y=180)

b1 = Button(root, text="登录", height=1, width=5, command=login, bg='azure')
b1.place(x=130, y=220)
b2 = Button(root, text="注册", height=1, width=5, command=page_register, bg='azure')
b2.place(x=190, y=220)
b3 = Button(root, text="清空", height=1, width=5, command=clr, bg='azure')
b3.place(x=250, y=220)

root.mainloop()
