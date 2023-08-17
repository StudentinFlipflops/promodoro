import tkinter as tk
from playsound import playsound

segment_patterns = [
    "abcdef",  # 0
    "bc",      # 1
    "abdeg",   # 2
    "abcdg",   # 3
    "bcfg",    # 4
    "acdfg",   # 5
    "acdefg",  # 6
    "abc",     # 7
    "abcdefg", # 8
    "abcfg"    # 9
]

segment_coords = {
    "a": (10, 10, 60, 10),
    "b": (62, 12, 62, 60),
    "c": (62, 65, 62, 120),
    "d": (10, 122, 60, 122),
    "e": (7, 65, 7, 120),
    "f": (7, 13, 7, 60),
    "g": (10, 62, 60, 62)
}

def ring():
    playsound("/home/adam/programs/my-projects/mpts/sound/ring.mp3")

def count_down(minutes, seconds, canvas, hours , break_time):
    
    
    
    if seconds == 0:
        seconds = 59
        minutes -= 1
    else:
        seconds -= 1

    if minutes < 0 and break_time == False:
        ring()
        print("break time")
        hours+=1
        minutes = 15
        seconds = 0
        break_time = True
        print("you work " , hours , "hours")

    elif minutes < 0 and break_time == True:
        ring()
        print("study time")
        minutes = 45
        seconds = 0
        break_time = False

        

    for x in "abcdefg":
        if x in segment_patterns[minutes // 10]:
            canvas.itemconfig("segment_10m_" + x, fill="red")
        else:
            canvas.itemconfig("segment_10m_" + x, fill="gray")
    
    for x in "abcdefg":
        if x in segment_patterns[minutes % 10]:
            canvas.itemconfig("segment_1m_" + x, fill="red")
        else:
            canvas.itemconfig("segment_1m_" + x, fill="gray")            
    
    for x in "abcdefg":
        if x in segment_patterns[seconds // 10]:
            canvas.itemconfig("segment_10s_" + x, fill="red")
        else:
            canvas.itemconfig("segment_10s_" + x, fill="gray")                
    
    for x in "abcdefg":
        if x in segment_patterns[seconds % 10]:
            canvas.itemconfig("segment_1s_" + x, fill="red")
        else:
            canvas.itemconfig("segment_1s_" + x, fill="gray")                    
    
    canvas.after(1000, count_down, minutes, seconds, canvas , hours , break_time)

    

def create_window():

    window = tk.Tk()
    window.title("Seven-Segment Countdown Clock")
    
    canvas = tk.Canvas(window, width=320, height=150)
    canvas.pack()

    for seg , coords in segment_coords.items():
        canvas.create_line( coords[0]     , coords[1] ,coords[2]     , coords[3] , fill="gray", width=10, tags="segment_10m_"+seg  )
        canvas.create_line( coords[0] +70 , coords[1] ,coords[2] +70 , coords[3] , fill="gray", width=10, tags="segment_1m_" +seg  )
        canvas.create_line( coords[0] +170, coords[1] ,coords[2] +170, coords[3] , fill="gray", width=10, tags="segment_10s_"+seg  )
        canvas.create_line( coords[0] +240, coords[1] ,coords[2] +240, coords[3] , fill="gray", width=10, tags="segment_1s_" +seg  )

    canvas.create_rectangle(150 ,30 , 160 , 40 , fill="red"  )
    canvas.create_rectangle(150 ,80 , 160 , 90 , fill="red"  )


    countdown_minutes = 45
    countdown_seconds = 0
    working_hours = 0
    break_time = False
    count_down(countdown_minutes, countdown_seconds, canvas, working_hours , break_time)

    window.mainloop()    


create_window()


# *** DONE *** # TODO: add ring sound 
# TODO: save working/studying hours with the dates they were saved


# Ideas for the future:
# -button to confirm presence
# -the ability to view learning and work statistics
#