import tkinter as tk

class DraggableObject:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(x, y, x+50, y+50, fill="blue")
        self.canvas.tag_bind(self.rect, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.rect, "<ButtonRelease-1>", self.on_release)
        self.canvas.tag_bind(self.rect, "<B1-Motion>", self.on_drag)
        self.start_x = 0
        self.start_y = 0

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_release(self, event):
        pass

    def on_drag(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.canvas.move(self.rect, x - self.start_x, y - self.start_y)
        self.start_x = x
        self.start_y = y

root = tk.Tk()
root.title("Draggable Objects")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

obj1 = DraggableObject(canvas, 100, 100)
obj2 = DraggableObject(canvas, 200, 200)

root.mainloop()
