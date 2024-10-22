#Modules
from tkinter import*
from tkinter import messagebox
import pubchempy as pbc

#We create the main window
mw=Tk()
mw.geometry('700x500')
mw.title('Information about your compound')
mw.config(bg='gray')

#Heading of the window
headingFrame=Frame(mw,bg='gray',bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel=Label(headingFrame,text='Information about your compound',bg='white',font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

#Taking the input of the user, this will be the molecular formula of a compound
Frame1=Frame(mw,bg='gray')
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
label1=Label(Frame1,text='Enter the chemical formula of your compound: ',bg='gray',fg='black',font=('Times',14,'bold'))
label1.place(relx=0.05,rely=0.2,relheight=0.2)
cformula=StringVar()
formula=Entry(Frame1,font=('Times 12'),textvariable=cformula)
formula.place(relx=0.05,rely=0.4,relwidth=1,relheight=0.2)

#This function will take the input of the user and will determine if it is a compound or not
def submit():
    try:
        cformula_entered = cformula.get()
        compound=pbc.get_compounds(cformula_entered,'formula')[0]
        #If the compound exists a secondary window will open
        sw = Toplevel()
        sw.title('Information about your compound')
        sw.geometry('700x800')
        sw.config(bg='gray')
        #This window will show as a title the molecular formula of the compound
        #And next will show 11 buttons that call a different function each
        headingFrame = Frame(sw, bg='gray', bd=5)
        headingFrame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
        headingLabel = Label(headingFrame, text='Compound : '+compound.molecular_formula, bg='white',font=('Times', 20, 'bold'))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        #This button will call the cid function
        button1 = Button(sw, text='Cid ', font='Times 12 bold', bg='slateblue4', fg='white', padx=2, command=cid)
        button1.place(relx=0.15, rely=0.3, relwidth=0.35, relheight=0.05)

        #This button will call the molecular_weight function
        button2=Button(sw,text='Molecular weight [g/mol]',font='Times 12 bold',bg='slateblue4',fg='white',padx=2,command=molecular_weight)
        button2.place(relx=0.55,rely=0.3,relwidth=0.35,relheight=0.05)

        #This button will call the iupac_name function
        button3=Button(sw,text='Iupac name ',font='Times 12 bold',bg='slateblue4',fg='white',padx=2,command=iupac_name)
        button3.place(relx=0.15,rely=0.4,relwidth=0.35,relheight=0.05)

        #This button will call the synonym function
        button4 = Button(sw, text='Synonym ', font='Times 12 bold', bg='slateblue4', fg='white', padx=2, command=synonym)
        button4.place(relx=0.55, rely=0.4, relwidth=0.35, relheight=0.05)

        #This button will call the elements function
        button5 = Button(sw, text='Elements ', font='Times 12 bold', bg='slateblue4', fg='white', padx=2,command=elements)
        button5.place(relx=0.15, rely=0.5, relwidth=0.35, relheight=0.05)

        #This button will call the isomeric_smiles function
        button6 = Button(sw, text='Isomeric smiles ', font='Times 12 bold', bg='slateblue4', fg='white', padx=2,command=isomeric_smiles)
        button6.place(relx=0.55, rely=0.5, relwidth=0.35, relheight=0.05)

        #This button will call the exact_mass function
        button7=Button(sw,text='Exact mass [g/mol] ',font='Times 12 bold',bg='slateblue4',fg='white',padx=2,command=exact_mass)
        button7.place(relx=0.15, rely=0.6, relwidth=0.35, relheight=0.05)

        #This button will call the hidrogen_bond_donor_count function
        button8 = Button(sw, text='Hidrogen bond donor count ', font='Times 12 bold', bg='slateblue4', fg='white', padx=2,command=hidrogen_bond_donor_count)
        button8.place(relx=0.55, rely=0.6, relwidth=0.35, relheight=0.05)

        #This button will call the hidrogen_bond_acceptor_count function
        button9 = Button(sw, text='Hidrogen bond acceptor count ', font='Times 12 bold', bg='slateblue4', fg='white', padx=2, command=hidrogen_bond_acceptor_count)
        button9.place(relx=0.15, rely=0.7, relwidth=0.35, relheight=0.05)

        #This button will call the complexity function
        button10 = Button(sw, text='Complexity ', font='Times 12 bold', bg='slateblue4', fg='white',padx=2, command=complexity)
        button10.place(relx=0.55, rely=0.7, relwidth=0.35, relheight=0.05)

        #This button will call the create_text function
        button11 = Button(sw, text='Create a .txt with all the information ', font='Times 12 bold', bg='slateblue4', fg='white', padx=2, command=create_txt)
        button11.place(relx=0.15, rely=0.8, relwidth=0.75, relheight=0.05)
    #If the compound does not exist it will show the next message
    except:
        messagebox.showinfo('Information about your compound','Wrong input, try again!' )

#We create the button that calls the submit function
button=Button(mw,text='Submit ',font='Times 12 bold',bg='slateblue4',fg='white',padx=2,command=submit)
button.place(relx=0.4,rely=0.45,relwidth=0.15,relheight=0.05)

#The next function is to define the object c, that will be used in the next functions.
def compound():
    cformula_entered = cformula.get()
    c = pbc.get_compounds(cformula_entered, 'formula')[0]
    return c

#Function determines the value of cid.
def cid():
    c = compound()
    messagebox.showinfo('Information about your compound','Cid= '+str(c.cid))

#Function determines the molecular weight in [g/mol] of the compound.
def molecular_weight():
    c=compound()
    messagebox.showinfo('Information about your compound', 'Molecular weight [g/mol]= ' + str(c.molecular_weight))

#Function determines the iupac name of the compound.
def iupac_name():
    c = compound()
    messagebox.showinfo('Information about your compound', 'Iupac name= ' + str(c.iupac_name))

#Function determines for synonyms of the compound.
def synonym():
    c = compound()
    messagebox.showinfo('Information about your compound', 'Synonym= ' + str(c.synonyms[0:4]))

#Function determines the elements of the compound.
def elements():
    c=compound()
    messagebox.showinfo('Information about your compound', 'Elements= ' + str(c.elements))

#Function determines the isomeric smiles of the compound.
def isomeric_smiles():
    c=compound()
    messagebox.showinfo('Information about your compound', 'Isomeric smiles= ' + str(c.isomeric_smiles))

#Function determines the exact mass in [g/mol] of the compound.
def exact_mass():
    c = compound()
    messagebox.showinfo('Information about your compound', 'Exact mass [g/mol]= ' + str(c.exact_mass))

#Function determines the hidrogen bond donor count of the compound.
def hidrogen_bond_donor_count():
    c = compound()
    messagebox.showinfo('Information about your compound', 'Hidrogen bond donor count= ' + str(c.h_bond_donor_count))

#Function determines the hidrogen bond acceptor count of the compound.
def hidrogen_bond_acceptor_count():
    c = compound()
    messagebox.showinfo('Information about your compound', 'Hidrogen bond acceptor count= ' + str(c.h_bond_acceptor_count))

#Function determines the complexity of the compound.
def complexity():
    c=compound()
    messagebox.showinfo('Information about your compound','Complexity= ' + str(c.complexity))

#Function that creates a .txt file that has all the information that the other buttons provide.
def create_txt():
    c=compound()
    with open('Information about your compound.txt', 'w') as file:
        file.write('Compound= ' + str(c.molecular_formula))
        file.write('\nCid= '+str(c.cid))
        file.write('\nMolecular Weight [g/mol]= ' + str(c.molecular_weight))
        file.write('\nIupac name= ' + str(c.iupac_name))
        file.write('\nSynonym= ' + str(c.synonyms[0:4]))
        file.write('\nElements= ' + str(c.elements))
        file.write('\nIsomeric smiles= ' + str(c.isomeric_smiles))
        file.write('\nExact mass [g/mol]= ' + str(c.exact_mass))
        file.write('\nHidrogen bond donor count= ' + str(c.h_bond_donor_count))
        file.write('\nHidrogen bond acceptor count= ' + str(c.h_bond_acceptor_count))
        file.write('\nComplexity= ' + str(c.complexity))

mw.mainloop()