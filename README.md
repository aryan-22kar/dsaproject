# DSA Algorithms Toolkit

A menu-driven Python 3 mini-project for practising core Data Structures and Algorithms.

## Features
- Linear search
- Binary search (sorts the values before searching)
- Bubble sort
- Selection sort
- Insertion sort
- Balanced-bracket checking using a stack
- Duplicate removal while preserving first-seen order

## Requirements
- Python 3.9 or newer
- No third-party packages required

## How to run
1. Extract the ZIP file.
2. Open a terminal in the extracted `DSA_Algorithms_Toolkit` folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py`.

4. Choose an option from the menu and follow the prompts.

## Complexity notes
- Linear search: O(n) time
- Binary search: O(log n) search time on sorted input; this menu option also sorts the input first
- Bubble sort, selection sort, insertion sort: O(n^2) average time
- Balanced brackets: O(n) time and O(n) extra space
- Duplicate removal: O(n) average time using a set
