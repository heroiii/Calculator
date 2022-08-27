from tkinter import *
import math
import parser
from tkinter import messagebox
import tkinter.messagebox 

#----add science fram----------
def add_frame():
    if frm1['text']=='Scientific Calculator' :
        
        frm1['text']='' 
        frm3.pack_forget()
        
    else:
        
        frm1['text']='Scientific Calculator'
       
        frm3.pack()
#----add science fram----------
        
#-----button gird science cal----------
        btn1 = Button(**btn_style,text = 'Sin',command = lambda:Add_sc(result,'sin'))
        btn2 = Button(**btn_style,text = 'Cos',command = lambda:Add_sc(result,'cos'))
        btn3 = Button(**btn_style,text = 'Tan',command = lambda:Add_sc(result,'tan'))
        btn4 = Button(**btn_style,text = 'Cot',command = lambda:Add_sc(result,'cot'))
        btn5 = Button(**btn_style,text = 'Pi',command = lambda:Add_sc(result,'pi'))
        btn6 = Button(**btn_style,text = '!',command = lambda:Add_sc(result,'!'))
        btn7 = Button(**btn_style,text = 'log',command = lambda:Add_sc(result,'log'))
        btn8 = Button(**btn_style,text = 'In',command = lambda:Add_sc(result,'in'))
        btn9 = Button(**btn_style,text = 'Abs',command = lambda:Add_sc(result,'abs'))
        btn10 = Button(**btn_style,text = '%',command = lambda:Add_sc(result,'%'))            
        btn11 = Button(**btn_style,text = '^',command = lambda:Add_sc(result,'^'))
        btn12 = Button(**btn_style,text = 'Sqrt',command = lambda:Add_sc(result,'sqrt'))

        btn1.grid(row = 1,column =1)
        btn2.grid(row = 1,column =2)
        btn3.grid(row = 1,column =3)
        btn4.grid(row = 1,column =4)
        btn5.grid(row = 1,column =5)
        btn6.grid(row = 1,column =6)
        btn7.grid(row = 2,column =1)
        btn8.grid(row = 2,column =2)
        btn9.grid(row = 2,column =3)
        btn10.grid(row = 2,column =4)
        btn11.grid(row = 2,column =5)
        btn12.grid(row = 2,column =6)

#-----button gird science cal----------
#-------all myfuncs-------
#-----func for delete a char
def Remove_a_num(labl):
    g =labl['text']
    result=''
    if(len(g))>0:
        for i,j in enumerate(g):
            if i==len(g)-1:
                pass
            else:result = result + j
    labl.config(text = result)
    labl.update
#-----func for delete a char
#-------func for clean labletext
def CleanResult(labl):
    labl.config(text = '')
    labl.update()
#-------func for clean labletext
#------func for add for simple cal---
def Add(labl,txt):
    g =labl['text']
    labl.config(text = g + txt)
    labl.update()
#------func for add for simple cal---

#------func for Perform operations ---
def Hesab(labl):
    flag ='False'
    g = labl['text']
    g1 = ''
    g2 = ''
    gs = ''
    gr = ''
    g0 = ''
    for i in range(len(g)):
        if g[i]=='s'or g[i]=='c' or g[i]=='t' or g[i] == 'l':
            flag = 'True'
    
            for i in range(len(g)):
                if g[i]=='s'or g[i]=='c' or g[i]=='t' or g[i] == 'l':
            
                    for j in range(i,len(g)):
                        if g[j] == ')':
                            gs = gs + g[j]
                            for k in range(j+1,len(g)):
                                g2 = g2 + g[k]
                            break
                        else:
                            gs = gs + g[j]
                    for l in range(len(gs)):
                        if gs[1]=='l':
                            break
                        else:   
                            
                            if l>=4:
                                gr = gr+ gs[l]
                            elif l<4:
                                g0 = g0 +gs[l]
                    if 'l' in gs:
                        gs = gs
                    else:
                        
                        gs = g0 + 'math.radians('+ gr + ')'
                    
                    break
                    
                        
                else:
                    g1 = g1 + g[i]
        
            g = g1 +'math.'+ gs + g2
    
            break
      
       
    try:
        
        result= eval(g)
        labl.config(text =str(result))
    except:
        labl.config(text = '')
        messagebox.showinfo('error','عبارت نامعتبر')
    labl.update()
    
           
    
#------func for Perform operations ---

#------func for add for science cal---
def Add_sc(labl,txt):
    ref = '*/+-'
    g =labl['text']
    l=abs(len(g)-1)
    if g=='' or g[l] in ref:
        
        if  txt=='sin' :  
            labl.config(text = g + 'sin(')
            labl.update()         
        
        elif  txt=='cos' :  
            labl.config(text = g + 'cos(')
            labl.update()
        
        elif  txt=='tan' :  
            labl.config(text = g + 'tan(')
            labl.update()
        
        elif  txt=='cot' :  
            labl.config(text = g + 'cot(')
            labl.update()
        
        elif  txt=='log' :  
            labl.config(text = g + 'log(')
            labl.update()
        
        elif  txt=='in' :  
            labl.config(text = g + 'In(')
            labl.update()         
    else:    
        if txt == 'sqrt':
            labl.config(text = str(math.sqrt(eval(g))))
            labl.update()
            
        elif txt == 'abs':
            labl.config(text =str( abs(float(g))))
            labl.update()
            
        elif txt=='^':
            labl.config(text = g + '**')
            labl.update()
        
        elif txt=='!':
            labl.config(text = str(math.factorial(eval(g))))
            labl.update()
        
        elif txt == '%':
            labl.config(text = str(eval(g)/100))
            labl.update()
        
        elif txt == 'pi':
            labl.config(text = str(eval(g)*math.pi))
            labl.update()
            
        elif  txt=='sin' :
            messagebox.showinfo('error','عبارت نامعتبر')
            
        elif  txt=='cos' :
            messagebox.showinfo('error','عبارت نامعتبر')
            
        elif  txt=='tan' :
            messagebox.showinfo('error','عبارت نامعتبر')
            
        elif  txt=='cot' :
            messagebox.showinfo('error','عبارت نامعتبر')
            
            
    if g=='':
        
        if  txt=='sin' :  
            labl.config(text =  'sin(')
            labl.update()
           
          
        
        elif  txt=='cos' :  
            labl.config(text =  'cos(')
            labl.update()
        
        elif  txt=='tan' :  
            labl.config(text =  'tan(')
            labl.update()
        
        elif  txt=='cot' :  
            labl.config(text =  'cot(')
            labl.update()
        
        elif  txt=='log' :  
            labl.config(text =  'log10(')
            labl.update()
        
        elif  txt=='in' :  
            labl.config(text =  'log(')
            labl.update()

        else:
            labl.config(text = '')
            messagebox.showinfo('error','عبارت نامعتبر')
            labl.update() 
        
        
#------func for add for science cal---
    


#--- exit from cal
def exit():
    exit=tkinter.messagebox.askyesno('Science Calculator','Do you want to exit the system')
    if exit>0:
        win.destroy()
    return
#--- exit from cal
    
#------func for add for science cal---    
          
   
#-------all myfuncs-------         
    
    
win = Tk()
win.geometry('450x300+150+150')
win.resizable(False,False)
win.title('Calculator by HeroKolichi')
win.iconbitmap('01.ico')
win.configure(bg = 'gray')
win.state('normal')
#-----menubar---------
menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
#filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=filemenu)
#-----menubar---------

#------framelabel---
frm = LabelFrame(win
                 ,text = 'Result'
                 ,font = ('tahoma',10)
                 ,relief = 'raised'
                 ,width = 80
                 ,height = 50
                 ,bg = 'beige'

                 )
frm.pack()

result = Label(frm
            ,text = ''
            ,width =45
            ,height = 1
            ,bg = 'dark green'
            ,font = ('tahoma',14)
            ,relief = SUNKEN
            ,bd = 6
               ,fg = 'orange'
            )
           


result.pack(side = 'bottom')


#----framelabel----


frm1 = LabelFrame(win
                  ,text = ''
                  ,font = ('tahoma',10)
                  
                  ,width = 450
                  ,height = 80
                  ,bg = 'gray'
    )
frm1.pack()

frm3 = LabelFrame(frm1
                  ,text = ''
                  ,font = ('tahoma',10)
                  
                  ,width = 450
                  ,height = 80
                  ,bg = 'gray'
    )


#-----buttonstyle--------
btn_style = {'master':frm3
            ,'width' :8
            ,'height' : 1
            ,'bg' : 'black'
            ,'fg' : 'white'
            ,'font' : ('tahoma',10,'bold')
            ,'relief' : 'raised'
            ,'bd' : 3
             
    }
#-----buttonstyle--------
#----frame simple calculator-----
frm2 = LabelFrame(win
                  ,text = 'Simple Calculator'
                  ,font = ('tahoma',10)
                  ,relief = 'raised'
                  ,width = 500
                  ,height = 200
                  ,bg = 'beige'
    )
frm2.pack()
#-----buttonstyle--------
btn_style1 = {'master':frm2
            ,'width' :8
            ,'height' : 1
            ,'bg' : 'black'
            ,'fg' : 'white'
            ,'font' : ('tahoma',10,'bold')
            ,'relief' : 'raised'
            ,'bd' : 3
             
    }

btn_style2 = {'master':frm2
            ,'width' :8
            ,'height' : 1
            ,'bg' : 'white'
            ,'fg' : 'black'
            ,'font' : ('tahoma',10,'bold')
            ,'relief' : 'raised'
            ,'bd' : 3
             
    }

btn_style3 = {'master':frm2
            ,'width' :8
            ,'height' : 1
            ,'bg' : 'orange'
            ,'fg' : 'white'
            ,'font' : ('tahoma',10,'bold')
            ,'relief' : 'raised'
            ,'bd' : 3
             
    }

btn_style4 = {'master':frm2
            ,'width' :8
            ,'height' : 1
            ,'bg' : 'green'
            ,'fg' : 'white'
            ,'font' : ('tahoma',10,'bold')
            ,'relief' : 'raised'
            ,'bd' : 3
             
    }

btn_style5 = {'master':frm2
            ,'width' :17
            ,'height' : 1
            ,'bg' : 'green'
            ,'fg' : 'white'
            ,'font' : ('tahoma',10,'bold')
            ,'relief' : 'raised'
            ,'bd' : 3
             
    }
#-----buttonstyle--------

#-----button gird simple cal----------
btn1 = Button(**btn_style2,text = '7',command = lambda:Add(result,'7'))
btn2 = Button(**btn_style2,text = '8',command = lambda:Add(result,'8'))
btn3 = Button(**btn_style2,text = '9',command = lambda:Add(result,'9'))
btn4 = Button(**btn_style2,text = '4',command = lambda:Add(result,'4'))
btn5 = Button(**btn_style2,text = '5',command = lambda:Add(result,'5'))
btn6 = Button(**btn_style2,text = '6',command = lambda:Add(result,'6'))
btn7 = Button(**btn_style2,text = '1',command = lambda:Add(result,'1'))
btn8 = Button(**btn_style2,text = '2',command = lambda:Add(result,'2'))
btn9 = Button(**btn_style2,text = '3',command = lambda:Add(result,'3'))
btn10 = Button(**btn_style4,text = 'scientific',command = add_frame)
btn11 = Button(**btn_style2,text = '0',command = lambda:Add(result,'0'))
btn12 = Button(**btn_style1,text = '.',command = lambda:Add(result,'.'))
btn13 = Button(**btn_style1,text = '*',command = lambda:Add(result,'*'))
btn14 = Button(**btn_style3,text = 'Ac',command = lambda:CleanResult(result))
btn15 = Button(**btn_style3,text = 'C',command = lambda:Remove_a_num(result))
btn16 = Button(**btn_style1,text = '+',command = lambda:Add(result,'+'))
btn17 = Button(**btn_style1,text = '(',command = lambda:Add(result,'('))
btn18 = Button(**btn_style1,text = ')',command = lambda:Add(result,')'))
btn19 = Button(**btn_style1,text = '/',command = lambda:Add(result,'/'))
btn20 = Button(**btn_style1,text = '<',command = lambda:Add(result,'<'))
btn21 = Button(**btn_style1,text = '>',command = lambda:Add(result,'>'))
btn22 = Button(**btn_style1,text = '-',command = lambda:Add(result,'-'))
btn23 = Button(**btn_style5,text = '=',command = lambda:Hesab(result))

btn1.grid(row = 1,column =1)
btn2.grid(row = 1,column =2)
btn3.grid(row = 1,column =3)
btn4.grid(row = 2,column =1)
btn5.grid(row = 2,column =2)
btn6.grid(row = 2,column =3)
btn7.grid(row = 3,column =1)
btn8.grid(row = 3,column =2)
btn9.grid(row = 3,column =3)
btn10.grid(row = 4,column =1)
btn11.grid(row = 4,column =2)
btn12.grid(row = 4,column =3)
btn13.grid(row = 1,column =4)
btn14.grid(row = 1,column =5)
btn15.grid(row = 1,column =6)
btn16.grid(row = 2,column =4)
btn17.grid(row = 2,column =5)
btn18.grid(row = 2,column =6)
btn19.grid(row = 3,column =4)
btn20.grid(row = 3,column =5)
btn21.grid(row = 3,column =6)
btn22.grid(row = 4,column =4)
btn23.grid(row = 4,column =5,columnspan=6)

#-----button gird----------

win.config(menu=menubar)
win.mainloop()
