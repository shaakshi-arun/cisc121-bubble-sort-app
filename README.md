# Bubble Sort Visualizer 

This project is an interactive Python application that demonstrates how the Bubble Sort algorithm works.  
It is designed as a learning tool, showing not only the final sorted list but also a step-by-step explanation of every comparison and swap.

---

## Demo Screenshot of Test

Below is a screenshot of the app running on Hugging Face Spaces:

<img width="2426" height="741" alt="image" src="https://github.com/user-attachments/assets/8288694e-1f9f-4b82-8663-09c47dd19a4e" />
<img width="2417" height="718" alt="image" src="https://github.com/user-attachments/assets/d37fa082-8fd4-4af1-a88b-9c2c1ca1df8b" />
<img width="2430" height="713" alt="image" src="https://github.com/user-attachments/assets/6bf8c700-65b2-4e80-9c2a-4e995006dd9a" />



The interface includes:
- An input box for comma-separated integers
- A button to run the algorithm
- A box showing the sorted output
- A detailed explanation box that walks through each pass of Bubble Sort

---

## Problem Breakdown & Computational Thinking

### Problem Breakdown
The goal of this project was to select a sorting algorithm, implement it in Python, and present it through an interactive, easy-to-use user interface.

The application must:
- Accept user input safely
- Process the input using a correct algorithm
- Return accurate output
- Help users understand how the algorithm works, not just the result
- Be deployed publicly using Hugging Face

I chose Bubble Sort because it clearly shows how comparison-based sorting works and is ideal for teaching fundamental algorithm concepts.

---

### The Four Pillars of Computational Thinking

#### 1. Decomposition
The problem was broken into the following components:
- Reading user input (string)
- Parsing input into a list of integers
- Implementing Bubble Sort logic
- Recording each comparison and swap
- Displaying results clearly
- Building a Gradio-based UI
- Deploying the app on Hugging Face Spaces

---

#### 2. Pattern Recognition
Bubble Sort repeats a consistent pattern:
- Compare adjacent values
- Swap if the left value is larger
- After each pass, the largest value moves to the end
- The algorithm stops early if no swaps occur

Recognizing these patterns helped structure the algorithm efficiently.

---

#### 3. Abstraction
Internal details such as loops, indices, and list mutations are hidden from the user.

The user only interacts with:
- A clean input field
- A run button
- Clear output and explanations

This keeps the app beginner-friendly and focused on learning.

---

#### 4. Algorithm Design
Input:  
Comma-separated integers (e.g. `5, 3, 8, 1`)

Process: 
Parse input → run Bubble Sort → track steps

Output:
- Final sorted list  
- Step-by-step explanation of how sorting occurred  

---

## Algorithm Implementation & UI (Gradio)

The algorithm is implemented entirely in Python using Bubble Sort.

- The sort runs in-place
- Time complexity: O(n²)
- Space complexity: O(1)

The user interface is built using Gradio Blocks, which provides:
- Descriptive labels
- Readable text output
- Immediate feedback after running the algorithm

Gradio was chosen because it allows Python algorithms to be turned into web apps with minimal overhead while still being clear and interactive.

Comments are included in the Python code to explain each major section of logic.

---

## Testing & Verification

The app was tested using multiple inputs to ensure correctness and proper error handling.

### Test Case 1
Input: `5, 3, 8, 1, 2`  
Output: `1, 2, 3, 5, 8`  
Correct sorting with full explanation displayed: yes

---

### Test Case 2
Input: `10, 9, 8, 7`  
Output: `7, 8, 9, 10`  
Correct handling of descending input: yes

---

### Test Case 3 (Already Sorted)
Input: `1, 2, 3, 4`  
Algorithm stops early and reports no swaps: yes

---

### Test Case 4 (Invalid Input)
Input: `5, a, 3`  
App displays a clear error message instead of crashing: yes

These tests demonstrate correctness, robustness, and good user feedback.

---

## Steps to Run

### Run Online (Recommended)
Click the Hugging Face link below to use the app instantly:
- No setup required
- Runs entirely in the browser

### Run Locally (Optional)
1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Run `python app.py`
4. Open the local Gradio link in your browser

---

## Hugging Face Link
Live Application:  
https://huggingface.co/spaces/shaakshi-arun/cisc121-bubble-sort-app
---

## Author & Acknowledgment

Author: Shaakshi Kumbhat Arun  
Course: CISC 121 – Algorithm Design  
Technologies Used: Python, Gradio, GitHub, Hugging Face Spaces

Inspirational references:
- VisuAlgo – Sorting Visualizations
- Bubble Sort Game examples
- Gradio + Hugging Face documentation blogs

---
