from __future__ import division
#python2.7
#!/usr/bin/env python

import Tkinter as tk  

class TheCount(tk.Frame):
    def __init__(self, master= None):
        self.isEditing = False
        self.counts = [0,0,0]
        self.valuesForAvg = [1,2,3,4,5,6,7,8,9,10]
        self.buttons = []
        self.tallies = []
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.buttons = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9, self.button10]
        self.tallies = [self.tally1, self.tally2, self.tally3, self.tally4, self.tally5, self.tally6, self.tally7, self.tally8, self.tally9, self.tally10]
        self.NameEntryLabel = [None]*10
        self.NameEntry = [None]*10
        self.ValueEntryLabel = [None]*10
        self.ValueEntry = [None]*10
        self.FixCountLabel = [None]*10
        self.FixCountEntry = [None]*10
        self.DoneEditing = [None]*10
        self.DeleteButton = [None]*10
        self.bind_all("=", self.addCounter)
        self.bind_all("+", self.addCounter)
        self.bind_all("-", self.removeCounter)
        self.bind_all("1", lambda x : self.count(1))
        self.bind_all("2", lambda x : self.count(2))
        self.bind_all("3", lambda x : self.count(3))
        self.bind_all("4", lambda x : self.count(4))
        self.bind_all("5", lambda x : self.count(5))
        self.bind_all("6", lambda x : self.count(6))
        self.bind_all("7", lambda x : self.count(7))
        self.bind_all("8", lambda x : self.count(8))
        self.bind_all("9", lambda x : self.count(9))
        self.bind_all("0", lambda x : self.count(10))
        self.bind_all("!", lambda x : self.count(1, neg = True))
        self.bind_all("@", lambda x : self.count(2, neg = True))
        self.bind_all("#", lambda x : self.count(3, neg = True))
        self.bind_all("$", lambda x : self.count(4, neg = True))
        self.bind_all("%", lambda x : self.count(5, neg = True))
        self.bind_all("^", lambda x : self.count(6, neg = True))
        self.bind_all("&", lambda x : self.count(7, neg = True))
        self.bind_all("*", lambda x : self.count(8, neg = True))
        self.bind_all("(", lambda x : self.count(9, neg = True))
        self.bind_all(")", lambda x : self.count(0, neg = True))
        for buttonIndex in range(len(self.buttons)):
            self.buttons[buttonIndex].bind('<Button-3>', lambda x, buttonIndex=buttonIndex:self.editCounter(buttonIndex+1))
        
    def createWidgets(self):
        self.button1 = tk.Button(self, text='1', command = lambda: self.count(1))
        self.button1.grid(row=1, column=1)
        self.button2 = tk.Button(self, text='2', command = lambda: self.count(2))
        self.button2.grid(row=1, column=2)
        self.button3 = tk.Button(self, text='3', command = lambda: self.count(3))
        self.button3.grid(row=1, column=3)
        self.button4 = tk.Button(self, text='4', command = lambda: self.count(4))
        self.button5 = tk.Button(self, text='5', command = lambda: self.count(5))
        self.button6 = tk.Button(self, text='6', command = lambda: self.count(6))
        self.button7 = tk.Button(self, text='7', command = lambda: self.count(7))
        self.button8 = tk.Button(self, text='8', command = lambda: self.count(8))
        self.button9 = tk.Button(self, text='9', command = lambda: self.count(9))
        self.button10 = tk.Button(self, text='10', command = lambda: self.count(10))

        self.addbutton = tk.Button(self, text='+', command = self.addCounter)
        self.addbutton.grid(row=1, column=100)
        self.addbutton.config(width=7)
        self.removebutton = tk.Button(self, text='-', command = self.removeCounter)
        self.removebutton.config(width=7)
        self.removebutton.grid(row=1, column=99)
        self.clearbutton = tk.Button(self, text = "Clear", command = self.clearCounts)
        self.clearbutton.config(width=7)
        self.clearbutton.grid(row=1, column = 101)
        
        val1 = tk.StringVar()
        val1.set('0')
        self.tally1 = tk.Label(self, textvariable = val1) 
        self.tally1.grid(row=2, column=1)
        val2 = tk.StringVar()
        val2.set('0')
        self.tally2 = tk.Label(self, textvariable = val2) 
        self.tally2.grid(row=2, column=2)
        val3 = tk.StringVar()
        val3.set('0')
        self.tally3 = tk.Label(self, textvariable = val3) 
        self.tally3.grid(row=2, column=3)
        val4 = tk.StringVar()
        val4.set('0')
        self.tally4 = tk.Label(self, textvariable = val4) 
        val5 = tk.StringVar()
        val5.set('0')
        self.tally5 = tk.Label(self, textvariable = val5) 
        
        val6 = tk.StringVar()
        val6.set('0')
        self.tally6 = tk.Label(self, textvariable = val6) 
        
        val7 = tk.StringVar()
        val7.set('0')
        self.tally7 = tk.Label(self, textvariable = val7) 
        
        val8 = tk.StringVar()
        val8.set('0')
        self.tally8 = tk.Label(self, textvariable = val8) 
        
        val9 = tk.StringVar()
        val9.set('0')
        self.tally9 = tk.Label(self, textvariable = val9) 
        
        val10 = tk.StringVar()
        val10.set('0')
        self.tally10 = tk.Label(self, textvariable = val10) 
        
        self.vals = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]
        
        pro1 = tk.StringVar()
        self.prop1 = tk.Label(self, textvariable = pro1)
        self.prop1.grid(row=3,column=1)
        pro2 = tk.StringVar()
        self.prop2 = tk.Label(self, textvariable = pro2)
        self.prop2.grid(row=3,column=2)
        pro3 = tk.StringVar()
        self.prop3 = tk.Label(self, textvariable = pro3)
        self.prop3.grid(row=3,column=3)
        pro4 = tk.StringVar()
        self.prop4 = tk.Label(self, textvariable = pro4)
        pro5 = tk.StringVar()
        self.prop5 = tk.Label(self, textvariable = pro5)
        pro6 = tk.StringVar()
        self.prop6 = tk.Label(self, textvariable = pro6)
        pro7 = tk.StringVar()
        self.prop7 = tk.Label(self, textvariable = pro7)
        pro8 = tk.StringVar()
        self.prop8 = tk.Label(self, textvariable = pro8)
        pro9 = tk.StringVar()
        self.prop9 = tk.Label(self, textvariable = pro9)
        pro10 = tk.StringVar()
        self.prop10 = tk.Label(self, textvariable = pro10)
        self.props = [self.prop1, self.prop2, self.prop3, self.prop4 , self.prop5 , self.prop6 , self.prop7 , self.prop8 , self.prop9 , self.prop10]
        self.pros = [pro1, pro2, pro3, pro4, pro5, pro6, pro7, pro8, pro9, pro10]
        
        self.total = tk.StringVar()
        self.total.set('tot=0')
        self.totalLabel = tk.Label(self, textvariable = self.total)
        self.totalLabel.grid(row=2, column = 99)
        self.avg = tk.StringVar()
        self.avg.set('avg=0')
        self.avgLabel = tk.Label(self, textvariable = self.avg)
        self.avgLabel.grid(row=2, column = 100)
    
    def count(self, buttonNum, neg = False):
        buttonNum -= 1 #button 1 is internally button 0
        if len(self.counts) > buttonNum and not self.isEditing:
            if neg:
                self.counts[buttonNum] -= 1
            else:
                self.counts[buttonNum] += 1
            self.vals[buttonNum].set(str(self.counts[buttonNum]))
            self.calcProportions()
                
    def calcProportions(self):
        if sum(self.counts) > 0:
            for counter in range(len(self.counts)):
                #self.pros[counter].set( str(self.counts[counter]/sum(self.counts))[0:5] )
                self.pros[counter].set( "%0.3f" % (self.counts[counter]/sum(self.counts)) )
        else:
            for counter in range(len(self.counts)):
                self.pros[counter].set('0')
        self.total.set('tot=' + str(sum(self.counts)))
        if not sum(self.counts) == 0:
            self.avgnum = sum([self.counts[a]*float(self.valuesForAvg[a]) for a in range(len(self.counts))])/sum(self.counts)
        else:
            self.avgnum = 0
        self.avg.set('avg=' + str(self.avgnum)[0:5])
    
    def addCounter(self, event = None):
        if not self.isEditing:
            newCounterNum = len(self.counts)+1
            if newCounterNum <= len(self.buttons):
                self.counts.append(0)
                self.vals[newCounterNum-1].set('0')
                self.buttons[newCounterNum-1].grid(row=1, column = newCounterNum)
                self.tallies[newCounterNum-1].grid(row=2, column = newCounterNum)
                self.props[newCounterNum-1].grid(row=3, column = newCounterNum)
                self.calcProportions()
    
    def removeCounter(self, event = None):
        if not self.isEditing and len(self.counts) > 0:
            lastNum = len(self.counts)
            self.buttons[lastNum-1]["text"] = lastNum
            self.counts.pop(lastNum-1)
            self.vals[lastNum-1].set('0')
            self.buttons[lastNum-1].grid_remove()
            self.tallies[lastNum-1].grid_remove()
            self.props[lastNum-1].grid_remove()
            self.valuesForAvg[lastNum-1] = lastNum
            self.calcProportions()
    
    def editCounter(self, buttonNum):
        if not self.isEditing:
            print 'editing counter ' + str(buttonNum)
            self.DeleteButton[buttonNum-1] = tk.Button(self, text = 'Clear counter', command = lambda buttonNum=buttonNum: self.deleteCounter(buttonNum))
            self.DeleteButton[buttonNum-1].grid(row = 98, column = buttonNum) 
            self.NameEntryLabel[buttonNum-1] = tk.Label(self, text = 'Counter name')
            self.NameEntryLabel[buttonNum-1].grid(row = 99, column = buttonNum) 
            self.NameEntry[buttonNum-1] = tk.Entry(self)
            self.NameEntry[buttonNum-1].grid(row = 100, column = buttonNum)
            self.ValueEntryLabel[buttonNum-1] = tk.Label(self, text = 'Value for averaging')
            self.ValueEntryLabel[buttonNum-1].grid(row = 101, column = buttonNum) 
            self.ValueEntry[buttonNum-1] = tk.Entry(self)
            self.ValueEntry[buttonNum-1].insert(0, self.valuesForAvg[buttonNum-1])
            self.ValueEntry[buttonNum-1].grid(row = 102, column = buttonNum)
            self.FixCountLabel[buttonNum-1] = tk.Label(self, text = 'Enter a new count')
            self.FixCountLabel[buttonNum-1].grid(row = 103, column = buttonNum) 
            self.FixCountEntry[buttonNum-1] = tk.Entry(self)
            self.FixCountEntry[buttonNum-1].grid(row = 104, column = buttonNum)
            self.DoneEditing[buttonNum-1] = tk.Button(self, text = 'Done', command = lambda buttonNum=buttonNum: self.doneEditing(buttonNum) )
            self.DoneEditing[buttonNum-1].grid(row = 105, column = buttonNum)
            self.isEditing = True
        
    def doneEditing(self, buttonNum):
        def RepresentsInt(s):
            try: 
                int(s)
                return True
            except ValueError:
                return False
        def RepresentsFloat(s):
            try: 
                float(s)
                return True
            except ValueError:
                return False
        if len(self.counts) > buttonNum-1:
            if RepresentsInt(self.ValueEntry[buttonNum-1].get()):
                self.valuesForAvg[buttonNum-1] = self.ValueEntry[buttonNum-1].get()
            if len(self.NameEntry[buttonNum-1].get()) > 0:
                self.buttons[buttonNum-1]["text"] = self.NameEntry[buttonNum-1].get()
            if RepresentsInt(self.FixCountEntry[buttonNum-1].get()):
                self.vals[buttonNum-1].set(str(self.FixCountEntry[buttonNum-1].get()))
                self.counts[buttonNum-1] = int(self.FixCountEntry[buttonNum-1].get())
            if RepresentsFloat(self.ValueEntry[buttonNum-1].get()):
                self.valuesForAvg[buttonNum-1] = float(self.ValueEntry[buttonNum-1].get())
            self.NameEntryLabel[buttonNum-1].grid_remove()
            self.NameEntry[buttonNum-1].grid_remove()
            self.ValueEntryLabel[buttonNum-1].grid_remove()
            self.ValueEntry[buttonNum-1].grid_remove()
            self.FixCountLabel[buttonNum-1].grid_remove()
            self.FixCountEntry[buttonNum-1].grid_remove()
            self.DoneEditing[buttonNum-1].grid_remove()
            self.DeleteButton[buttonNum-1].grid_remove()
            self.calcProportions()
            self.isEditing = False
    
        
    def deleteCounter(self, buttonNum):
        if len(self.counts) > buttonNum-1:
            self.doneEditing(buttonNum)
            self.buttons[buttonNum-1]["text"] = buttonNum
            self.counts[buttonNum-1] = 0
            self.vals[buttonNum-1].set('0')
            self.valuesForAvg[buttonNum-1] = buttonNum
            self.isEditing = False
            self.calcProportions()
    
    def clearCounts(self):
        self.counts = [0 for x in self.counts]
        for buttonNum in range(len(self.counts)):
            self.vals[buttonNum].set(str(self.counts[buttonNum]))
        self.calcProportions()
        self.total.set('tot=0')
        self.avg.set('avg=0')
    
app = TheCount()

app.master.title('TheCount')
app.mainloop()

