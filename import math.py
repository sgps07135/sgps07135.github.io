import turtle
import math

def draw_pythagoras_tree(t, x, y, size, angle, depth, max_depth, square_id_counter):
    if depth > max_depth:
        return square_id_counter
    
    current_id = square_id_counter
    square_id_counter += 1

    # 計算弧度
    rad = math.radians(angle)
    cos_a, sin_a = math.cos(rad), math.sin(rad)

    # 四個頂點座標
    p0 = (x, y)
    p1 = (x + size * cos_a, y + size * sin_a)
    p2 = (x + size * cos_a - size * sin_a, y + size * sin_a + size * cos_a)
    p3 = (x - size * sin_a, y + size * cos_a)

    # 1. 畫正方形
    t.penup()
    t.goto(p0)
    t.pendown()
    t.begin_fill()
    for px, py in [p1, p2, p3, p0]:
        t.goto(px, py)
    t.end_fill()

    # 2. 標示編號
    center_x = (p0 + p2) / 2
    center_y = (p0[1] + p2[1]) / 2
    t.penup()
    t.goto(center_x, center_y - 6)
    t.color("black")
    t.write(str(current_id), align="center", font=("Arial", max(8, 12 - depth), "bold"))
    t.fillcolor("lightgreen")

    # 3. 計算頂部三角形頂點
    mid_x = (p3 + p2) / 2
    mid_y = (p3[1] + p2[1]) / 2
    peak_x = mid_x - (size / 2) * sin_a
    peak_y = mid_y + (size / 2) * cos_a

    # 4. 畫頂部三角形
    t.goto(p3)
    t.pendown()
    t.goto(p2)
    t.goto(peak_x, peak_y)
    t.goto(p3)
    t.penup()

    # 5. 遞迴繪製左側與右側正方形
    new_size = size / math.sqrt(2)
    
    # 左側
    draw_pythagoras_tree(t, p3, p3[1], new_size, angle + 45, depth + 1, max_depth, square_id_counter)
    # 右側
    draw_pythagoras_tree(t, peak_x, peak_y, new_size, angle - 45, depth + 1, max_depth, square_id_counter)

# 畫圖主程式
def start_turtle_drawing():
    screen = turtle.Screen()
    screen.setup(width=800, height=700)
    screen.title("神奇壁畫 - 動態繪畫")
    
    t = turtle.Turtle()
    t.speed(0)  # 最快速度
    t.hideturtle()
    t.fillcolor("lightgreen")
    
    # 開始繪製 5 層
    draw_pythagoras_tree(t, x=-40, y=-250, size=80, angle=0, depth=1, max_depth=5, square_id_counter=[1])
    screen.mainloop()

# 若在桌面版 Python 環境執行請取消註解下方這行：
# start_turtle_drawing()