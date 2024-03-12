from tkinter import *
from deep_translator import GoogleTranslator

WDN_WIDTH  = 200
WDN_HEIGHT = 400
WHITE = "#F5EEE6"
GREEN = "#24D68D"

root = Tk()
root.title("Vocabulary book")
root.configure(background=WHITE)
root.geometry(str(WDN_WIDTH)+'x'+str(WDN_HEIGHT))
root.minsize(WDN_WIDTH, WDN_HEIGHT)
root.maxsize(WDN_WIDTH, WDN_HEIGHT)


class Input_Module:
    def __init__(self, root): 
        input_frame = Frame(root, background=WHITE)    
        input_frame.grid(row=0, column=0, sticky=W)   
        
        word_lable  = Label(input_frame, text="Word: ", background=WHITE)
        word_lable.grid(row=0,column=0,sticky=W) 
        
        self.word_input = StringVar()
        word_box   = Entry(input_frame, textvariable=self.word_input)
        word_box.grid(row=0, column=1,pady=5)
        
        root.bind('<Return>', self.input)
    
    def input(self, event):
        r = GoogleTranslator(source='en', target='zh-CN').translate(self.word_input.get())
        t.add_word(self.word_input.get(), r)
        self.word_input.set('')
        
        
Input_Module(root)

class Title_Module:
    def __init__(self, root):
        volume_title_frame = Frame(root, background=WHITE)   
        volume_title_frame.grid(row=1, column=0, sticky=W) 
        
        frame_title = StringVar() 
        frame_title.set("3-1.A") 
        
        frame_name = Entry(volume_title_frame, textvariable=frame_title, bg=GREEN, relief=RIDGE)
        frame_name.grid(row=0, column=0)
Title_Module(root)

class List_Module:
    def __init__(self, root):
        self.width = 2
        self.canvas     = Canvas(root, borderwidth=0, background=WHITE)
        self.word_frame = Frame(self.canvas, background="#8CE2B9", width=20)
        
        self.vsb = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        
        self.canvas.grid(row=2, column=0, pady=5, ipadx=20)
        self.word_frame.grid(row=0, column=0)
        self.vsb.grid(row=2, column=0, sticky=NS)

        self.canvas_word_frame=self.canvas.create_window(0, 0, window=self.word_frame, anchor="nw")
        
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.word_frame.bind("<Configure>", self.OnFrameConfigure)
        self.canvas.bind("<Configure>", self.FrameWidth)
        
        self.word_count = 0
        self.word_frame.grid_columnconfigure(0, minsize=66)
        self.word_frame.grid_columnconfigure(1, minsize=132)
    
    def FrameWidth(self, event):
        self.canvas_width = event.width
        self.canvas.itemconfig(self.canvas_word_frame, width = self.canvas_width)

    def OnFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def dummy_frame(self):
        for i in range(0): #Rows
            for j in range(self.width): #Columns
                b = Label(self.word_frame, text="hello"+str(i), background=WHITE, justify='left')
                if j == 0:
                    b.grid(row=i, column=0, sticky=NSEW, padx=1)
                else:
                    b.grid(row=i, column=1, columnspan=2, sticky=NSEW,padx=1)
    
    def add_word(self, word, meaning):
        wl = Label(self.word_frame, text=word, background=WHITE, justify='left')
        ml = Label(self.word_frame, text=meaning, background=WHITE, justify='left')
        wl.grid(row=self.word_count, column=0, sticky=NSEW, padx=1)
        ml.grid(row=self.word_count, column=1, columnspan=2, sticky=NSEW, padx=1)
        self.word_count += 1

t = List_Module(root)

root.mainloop()