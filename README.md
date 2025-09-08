# 🎨 Colorful Dot Grid with Python Turtle  

This project uses Python's `turtle` module to generate a colorful grid of random dots. Each dot is drawn in a random RGB color, creating a simple but fun piece of generative art.  

## ✨ Features  
- Uses **Python Turtle Graphics**  
- Generates **100 randomly colored dots**  
- Dots arranged in a neat **10x10 grid**  
- Interactive window that closes on click  

## 📸 Preview  
The program will generate something like this (colors vary every run):  

```
🔴 🟢 🔵 🟡 🔴 🟣 ...
```

(A grid of dots in random colors)  

## 🛠️ Requirements  
- Python 3.x  
- No external libraries required (only built-in `turtle` and `random` modules)  

## 🚀 How to Run  
1. Clone this repository or copy the code into a file, e.g., `dot_grid.py`  
2. Run the program:  
   ```bash
   python dot_grid.py
   ```  
3. A new window will open showing the colorful dot grid.  
4. Click inside the window to close it.  

## 📂 Code Explanation  
- **`turtle.colormode(255)`** → allows use of RGB values (0–255).  
- **`func()`** → draws one colored dot, moves turtle forward.  
- Loop runs **100 times**, drawing a **10x10 grid**.  
- Every 10 dots, the turtle moves down to start the next row.  


## 🖌️ Customization  
- Change **dot size** → modify `t.dot(20)`  
- Change **spacing** → adjust `t.forward(50)`  
- Change **grid size** → modify loop range  
