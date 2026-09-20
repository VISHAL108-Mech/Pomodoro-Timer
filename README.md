# 🍅 Pomodoro Timer

A desktop productivity app built with Python's `tkinter` GUI toolkit, implementing the **Pomodoro Technique** — 25 minutes of focused work, followed by short breaks, with a longer break every 4th session. A visual tomato icon and checkmark tracker keep you motivated as you power through work sessions.

> Start the timer, focus for 25 minutes, take a break, repeat. Every completed work session earns you a ✔ on screen.

---

## 🎮 Demo

<img width="400" height="300" alt="Screenshot 2026-09-20 205803" src="https://github.com/user-attachments/assets/39e70173-3981-4ce1-83d1-e0a32dc2236a" />
<img width="400" height="300" alt="Screenshot 2026-09-20 183024" src="https://github.com/user-attachments/assets/2f996176-11a6-4e8d-8969-af32e52cada1" />

---

## ✨ Features

- ⏱️ **Full Pomodoro cycle automation** — 25-minute work sessions, 5-minute short breaks, and a 10-minute long break every 4th work session, cycling automatically without manual switching.
- 🔁 **Self-scheduling countdown** using `window.after()`, updating the display every second without freezing the GUI.
- ✔️ **Visual progress tracking** — a checkmark is added for every completed work session, so you can see your streak at a glance.
- 🎨 **Dynamic label styling** — the "Focus," "Short Break," and "Long Break" labels change color and size depending on the current session type.
- 🔄 **One-click reset** — cancels the running timer and resets the display, labels, and session count back to zero.
- 🍅 **Custom tomato graphic** rendered on a canvas, true to the technique's namesake (Pomodoro = Italian for "tomato").

---

## 🛠️ Tech Stack

| Category | Tool / Concept |
|---|---|
| Language | Python 3 |
| GUI | `tkinter` (standard library) |
| Timing | `window.after()` — tkinter's built-in event scheduler |
| Math | `math.floor()` for minute/second conversion |
| Core Concepts | Recursive scheduling, global state management, conditional session logic |

---

## 📂 Project Structure

```
Pomodoro Timer/
│
├── main.py          # Entry point — timer logic, session cycling, and GUI layout
├── tomato.png         # Tomato graphic displayed on the canvas
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- `tkinter` (ships with most Python installations — no extra `pip install` needed)

### Run it
```bash
git clone https://github.com/VISHAL108-Mech/Pomodoro-Timer.git
cd pomodoro-timer
python main.py
```

### How to Use
| Button | Action |
|---|---|
| **Start** | Begins the next session in the cycle (work → short break → work → ... → long break) |
| **Reset** | Cancels the current countdown and resets everything back to zero |

---

## 🧩 How It Works

### 1. Session Constants
Work and break lengths are defined once as constants (in minutes), making it trivial to tweak the technique's timing without touching any logic.

```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
REPS = 0
timer = None
```

### 2. Deciding Which Session Comes Next
Every time `start_timer()` runs, it increments a global rep counter and uses simple modulo logic to decide whether this rep is a work session, a short break, or — every 8th rep (4th completed work/break pair) — a long break.

```python
def start_timer():
    global REPS
    REPS += 1
    work_session = WORK_MIN * 60
    short_break_session = SHORT_BREAK_MIN * 60
    long_break_session = LONG_BREAK_MIN * 60

    if REPS % 2 != 0:
        count_down(work_session)
        timer_label.config(text="Focus", fg=GREEN, bg=YELLOW,
                            font=(FONT_NAME, 40, "bold"))
    elif REPS % 8 == 0:
        count_down(long_break_session)
        timer_label.config(text="Long Break", fg=RED, bg=YELLOW,
                            font=(FONT_NAME, 20, "bold"))
    else:
        count_down(short_break_session)
        timer_label.config(text="Short Break", fg=PINK, bg=YELLOW,
                            font=(FONT_NAME, 20, "bold"))
```

### 3. The Countdown Mechanism
This is the heart of the app — instead of blocking with `time.sleep()` (which would freeze the GUI), it uses `window.after()` to reschedule itself every second, decrementing the count each call until it hits zero and automatically kicks off the next session.

```python
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔"
        tick_label.config(text=marks)
```

### 4. Resetting Everything
Cancels the pending scheduled call with `window.after_cancel()` — critical to stop the recursive countdown from continuing in the background — then resets all display elements and the rep counter.

```python
def reset_timer():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    REPS = 0
```

### 5. Building the Interface
A `Canvas` widget hosts the tomato graphic with the countdown text layered directly on top of it, while `Start`/`Reset` buttons and labels are arranged around it using tkinter's grid layout.

```python
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
```

---

## 📚 What This Project Demonstrates

- Using `window.after()` for non-blocking, self-rescheduling timers in a GUI event loop
- Managing global state (`REPS`, `timer`) cleanly across multiple functions
- Translating a real productivity methodology into conditional program logic
- Canceling scheduled callbacks properly (`after_cancel()`) to avoid orphaned background timers
- Building responsive, dynamically-updating UI elements without external animation libraries

---

## 🔮 Future Improvements

- [ ] Add a sound/notification when a session ends
- [ ] Make work/break durations configurable through the UI instead of hardcoded constants
- [ ] Persist session history across app restarts
- [ ] Add a pause/resume option instead of only start/reset
- [ ] Package as a standalone executable for easier sharing

---

## 👤 Developer

**VISHAL YADAV**
- GitHub: [@VISHAL108-Mech](https://github.com/VISHAL108-Mech)
- LinkedIn: [vishal-yadav-2a91a7428](https://www.linkedin.com/in/vishal-yadav-2a91a7428)
- Email: [vy4122000@gmail.com](mailto:vy4122000@gmail.com)
