import csv
import os
import tkinter as tk
import random
# Get the directory of the current script
script_dir = os.path.dirname(__file__)
# Assuming your CSV file is named 'data.csv'
file_name = 'smite_two_items.csv'
# Construct the full path to the CSV file
file_path = os.path.join(script_dir, file_name)

#Create Dictionary of items
items = {}
items[1] = {}
i = 1
new_item = False
with open(file_path, 'r') as csvfile:
    rd = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for raw in rd:
        raw = [element.replace('\t','') for element in raw]
        raw = ' '.join(raw)
        if raw.endswith(',') == False:
            new_item = True
        raw = raw.split('-')
        raw = [element.replace(',','') for element in raw]
        items[i][raw[0]] = raw[1]
        if new_item == True:
            i = i + 1
            items[i] = {}
            new_item = False
#End Create Dictionary of items

#Draggable GUI
class DraggableObject:
    selected_rectangles = []

    def __init__(self, canvas, x, y, info):
        self.canvas = canvas
        self.copy_rect = None
        if "Name" in info:
            self.name = info['Name']
        else:
            self.name = 'NA'
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        # Format the color string
        self.fill_color = f"#{r:02x}{g:02x}{b:02x}"    
        self.rect = canvas.create_rectangle(x, y, x+50, y+50, fill=self.fill_color, outline = "black", width = 1)
        self.canvas.tag_bind(self.rect, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.rect, "<ButtonRelease-1>", self.on_release)
        self.canvas.tag_bind(self.rect, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.rect, "<Leave>", self.on_leave)
        self.selected = False
        self.start_x = 0
        self.start_y = 0
        self.grid_size = 50
        self.canvas_width = canvas.winfo_reqwidth()
        self.canvas_height = canvas.winfo_reqheight()
        self.info_label = None

    def on_press(self, event):
        if self.selected:
            self.selected = False
            DraggableObject.selected_rectangles.remove(self)
            self.remove_copy_if_deselected()
        else:
            if len(DraggableObject.selected_rectangles) < 6:
                self.selected = True
                DraggableObject.selected_rectangles.append(self)
                self.create_copy_if_selected()
            else:
                return
        self.update()

    def on_release(self, event):
        pass

    def on_drag(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        
        # Snap to grid
        x = round(x / self.grid_size) * self.grid_size
        y = round(y / self.grid_size) * self.grid_size
        
        # Check if object exceeds halfway point
        if x < self.canvas_width *0.70:
            self.canvas.coords(self.rect, x, y, x+50, y+50)

    def on_enter(self, event):
        if self.info_label is None:
            self.info_label = tk.Label(self.canvas, text=self.name)
            self.info_label.place(relx=0.8, rely=0.1, anchor=tk.CENTER)

    def on_leave(self, event):
        if self.info_label is not None:
            self.info_label.destroy()
            self.info_label = None

    def update(self):
        if self.selected:
            self.canvas.itemconfig(self.rect, outline="red", width=2)
        else:
            self.canvas.itemconfig(self.rect, outline="black", width=1)

    def create_copy_if_selected(self):
        if self.selected:
            new_x = self.canvas_width / 2 - 150 + len(DraggableObject.selected_rectangles) * 50
            new_y = self.canvas_height - 50
            new_rect = self.canvas.create_rectangle(new_x, new_y, new_x + 50, new_y + 50, fill=self.fill_color, outline="black", width=1)
            self.copy_rect = new_rect
            self.canvas.tag_raise(new_rect)

    def remove_copy_if_deselected(self):
        if not self.selected and self.copy_rect is not None:
            self.canvas.delete(self.copy_rect)
            self.copy_rect = None

root = tk.Tk()
root.title("Draggable Objects")

canvas = tk.Canvas(root, width=1000, height=800, bg="white")
canvas.pack()

objects_info=[]

# Fill objects_info with coordinates
q = 1
for y in range(0, 500, 50):
    for x in range(0, 500, 50):
        info = f"Info: Object at ({x}, {y})"
        if q < len(items):
            objects_info.append({"x": x, "y": y, "info": items[q]})
        q = q + 1

objects = []
for obj_info in objects_info:
    obj = DraggableObject(canvas, obj_info["x"], obj_info["y"], obj_info["info"])
    objects.append(obj)

root.mainloop()

#End Draggable GUI