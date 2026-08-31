import turtle
import time
import math

# --- Window Setup ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Happy Raksha Bandhan Animation")
screen.bgcolor("#110022")  # Deep royal/festive background
screen.tracer(0)  # Turn off instant drawing for smooth animation frames

# --- Turtle Setup ---
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def draw_glowing_circle(x, y, radius, color):
    """Draws a soft glowing outer ring layer."""
    t.up()
    t.goto(x, y - radius)
    t.down()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_rakhi_thread():
    """Draws the silk protection threads extending from both sides."""
    t.pensize(5)
    # Left thread (crimson and gold blend)
    t.up()
    t.goto(-350, 0)
    t.down()
    t.color("#FFD700")
    for x in range(-350, -60, 5):
        y = 15 * math.sin(x * 0.05)
        t.goto(x, y)
    
    # Right thread
    t.up()
    t.goto(60, 0)
    t.down()
    t.color("#FFD700")
    for x in range(60, 350, 5):
        y = 15 * math.sin(x * 0.05)
        t.goto(x, y)

def draw_rakhi_center(angle_offset):
    """Draws the central dynamic animated dial of the Rakhi."""
    # Outer decorative thread boundary
    draw_glowing_circle(0, 0, 85, "#FF3366")
    draw_glowing_circle(0, 0, 75, "#FFCC00")
    draw_glowing_circle(0, 0, 65, "#00cc88")
    
    # Intricate rotating floral petals
    t.pensize(3)
    petals = 12
    for i in range(petals):
        angle = (i * (360 / petals)) + angle_offset
        rad = math.radians(angle)
        
        # Petal Tip Position
        x_tip = 60 * math.cos(rad)
        y_tip = 60 * math.sin(rad)
        
        t.up()
        t.goto(0, 0)
        t.down()
        t.color("#FF3366")
        t.goto(x_tip, y_tip)
        
        # Decorative bead accents on the petal tips
        t.up()
        t.goto(x_tip, y_tip)
        t.dot(8, "#FFFFFF")
        
    # Central sparkling core diamond
    draw_glowing_circle(0, 0, 25, "#FF0055")
    draw_glowing_circle(0, 0, 15, "#FFFFFF")
    t.up()
    t.goto(0, -4)
    t.color("#FFCC00")
    t.dot(10)

def draw_text(pulse_size):
    """Renders festive typography with a pulsing shadow effect."""
    t.up()
    # Dynamic text color pulsing shift
    t.color("#FFD700") 
    t.goto(0, 160)
    t.write("Happy Raksha Bandhan", align="center", font=("Arial", int(32 + pulse_size), "bold"))
    
    t.color("#FFFFFF")
    t.goto(0, -180)
    t.write("Celebrating the Eternal Bond of Love & Protection", align="center", font=("Verdana", 14, "italic"))

# --- Main Animation Loop ---
angle = 0
pulse = 0
growing = True

try:
    while True:
        t.clear()
        
        # 1. Base structure elements
        draw_rakhi_thread()
        
        # 2. Main rotating center graphic
        draw_rakhi_center(angle)
        
        # 3. Pulsing header text calculations
        if growing:
            pulse += 0.2
            if pulse > 4: growing = False
        else:
            pulse -= 0.2
            if pulse < 0: growing = True
            
        draw_text(pulse)
        
        # 4. Update the screen matrix frame
        screen.update()
        
        # Iteration increments
        angle += 2.5
        time.sleep(0.03)

except turtle.Terminator:
    print("Animation window closed gracefully.")
