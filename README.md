# Game 24

A Python-based implementation of the classic **Game 24**, where players use four numbers and basic arithmetic operations (`+`, `-`, `*`, `/`) to create an expression that evaluates to 24.

## **Features**
- Automatically generates random numbers that are guaranteed to have a solution.
- Allows players to input their solution and validates it.
- Tracks scores and time taken for each round.
- Displays a performance chart of scores and time taken across rounds.
- Supports non-GUI environments by saving the performance chart as an image.

---

## **How to Play**
1. The program generates 4 random numbers.
2. Use these numbers with `+`, `-`, `*`, `/`, and parentheses `()` to form an expression that evaluates to 24.
3. Input the solution into the program.
4. Repeat for the number of rounds specified (default: 5).

---

## **Prerequisites**
- Python 3.8 or later
- Virtual environment (`venv`) for dependency management

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git https://github.com/witchakornb/24_game_python.git
cd 24_game_python
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
```

### **3. Activate the Virtual Environment**
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### **4. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## **Usage**

### Run the Program
```bash
python main.py
```

### Gameplay Example
```plaintext
Welcome to Game 24!
Solve mathematical expressions to make 24 using the provided numbers.
You can use +, -, *, /, and parentheses.

Round 1 of 5
Numbers: [10, 15, 6, 15]
Enter your solution (e.g., '(8 + 2) * (3 + 1)'): ((15 / 10) * 6) + 15
Correct! You scored 10 points.
```

---

## **Output**
At the end of the game:
1. The total score and time taken per round are displayed in the console.
2. A performance graph is saved as `performance.png` in the current directory.

---

## **File Structure**

```plaintext
Game24/
│
├── game24.py           # Core game logic (number generation and validation)
├── player.py           # Player data management (scores and time tracking)
├── main.py             # Main program to handle game flow
├── requirements.txt    # Dependency list
└── README.md           # Documentation
```

---

## **Technical Details**

### **Core Components**
1. **Game Logic**:
   - Ensures the generated numbers have at least one valid solution.
   - Validates the player's input using both the numbers and mathematical evaluation.

2. **Player Management**:
   - Tracks scores and time for each player.
   - Provides summaries and analytics.

3. **Visualization**:
   - Generates a performance chart for scores and time taken per round using `matplotlib`.

### **Backend Configuration**
The default backend for `matplotlib` is set to `Agg` for non-GUI environments. The chart is saved as an image (`performance.png`).

---

## **Limitations**
- Only supports numbers between 1 and 20 for random generation.
- Assumes valid input; errors in syntax are handled but not deeply parsed.

---

## **Future Enhancements**
- Add support for multi-player mode.
- Improve error handling for invalid mathematical expressions.
- Allow players to set custom numbers or the number of rounds.

---

## **Contributing**
Pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to change.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contact**
If you encounter any issues or have suggestions, feel free to contact:
- **Email**: witchakorn.b@kkumail.com
- **GitHub**: [witchakornb](https://github.com/witchakornb/24_game_python.git)
