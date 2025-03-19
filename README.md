No More Porn! - Browser Content Blocker

Description:
No more porn! This Python-based program helps you block and prevent any pornographic content from appearing in your browser. It automatically detects and closes browser tabs or windows containing explicit content by scanning page titles for blocked words.

Features:
- Real-time Protection: Monitors open browser windows and automatically closes tabs with explicit content.
- Customizable Block List: Easily add or remove words to tailor the list of blocked content.
- Background Operation: Works silently in the background to ensure a safe browsing experience.
- Supports Major Browsers: Works with Chrome, Firefox, Edge, Opera, and Brave.

Supported Browsers:
- Chrome
- Firefox
- Edge
- Opera
- Brave

Installation:
1. Clone the Repository:
   git clone https://github.com/thekusaldarshana/blocker.git
   cd blocker

2. Install Dependencies:
   This program uses `psutil`, `pygetwindow`, and `plyer`. Install them using pip:
   pip install -r requirements.txt

3. Run the Program:
   You can run the program directly using Python or compile it into an executable.
   
   To run the program using Python:
   python blocker.py

   Alternatively, you can use the precompiled .exe file if available.

Usage:
1. The program will monitor all open browsers for explicit content.
2. If any browser tab contains a blocked word, the program will automatically close the tab.
3. Customize the list of blocked words in the BLOCKED_WORDS variable as needed.

Customization:
You can add or remove words from the BLOCKED_WORDS list to control what content gets blocked. Edit the list in the blocker.py file:

BLOCKED_WORDS = ["porn", "18+", "pussy", "lesbian", "gay", "milf", "onlyfans", ...]

Contributing:
Feel free to fork this repository, contribute, and submit issues or pull requests. All contributions are welcome!

License:
This project is licensed under the MIT License - see the LICENSE file for details.
