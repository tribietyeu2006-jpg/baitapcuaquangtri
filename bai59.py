import tkinter as tk

# Danh sách Can và Chi (mốc năm 0 = Canh Thân)
can = ["Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỷ"]
chi = ["Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]

def tinh_nam():
    nam = int(o_nhap.get())
    
    ten_can = can[nam % 10]
    ten_chi = chi[nam % 12]
    
    nam_lap = nam + 60
    
    ketqua.config(text=
                  str(nam)+" - "+ten_can+" "+ten_chi+
                  "\n"+
                  str(nam_lap)+" - "+ten_can+" "+ten_chi)

# Tạo cửa sổ
win = tk.Tk()
win.title("Bài 59 - Năm âm lịch")
win.geometry("300x200")

# Label
tk.Label(win,text="Nhập năm dương lịch:",font=("Arial",12)).pack(pady=5)

# Ô nhập
o_nhap = tk.Entry(win,font=("Arial",12))
o_nhap.pack(pady=5)

# Nút tính
tk.Button(win,text="Tính",font=("Arial",12),command=tinh_nam).pack(pady=5)

# Kết quả
ketqua = tk.Label(win,text="Kết quả",font=("Arial",12))
ketqua.pack(pady=10)

win.mainloop()
