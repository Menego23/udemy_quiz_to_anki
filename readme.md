# Udemy Quiz to Anki Flashcards Converter 🎯

> Transform any Udemy quiz into beautiful Anki flashcards automatically! Perfect for exam preparation and continuous learning.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![BeautifulSoup4](https://img.shields.io/badge/beautifulsoup4-latest-green.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![Genanki](https://img.shields.io/badge/genanki-latest-orange.svg)](https://github.com/kerrickstaley/genanki)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- Converts Udemy quiz HTML files into Anki flashcards
- Beautiful, responsive card design
- Clear separation between question, options, and explanations
- Bullet-pointed explanations for better readability
- Supports all types of Udemy quizzes
- Customizable card styling

## 📋 Prerequisites

- Python 3.8 or higher
- Anki desktop application
- Udemy quiz HTML files (saved from browser)

## 🔧 Installation

1. Clone this repository:
```bash
git clone https://github.com/menego23/udemy-to-anki.git
cd udemy-to-anki
```

2. Install required packages:
```bash
pip install beautifulsoup4 genanki
```

## 💻 Usage

1. Save your Udemy quiz pages as HTML:
   - Open the quiz in your browser
   - Right-click and select "Save as"
   - Choose "Webpage, Complete" option
   - Save to your input folder

2. Update the configuration in 

main.py

:
```python
html_folder = r'path\to\your\html\files'
output_file = 'your_deck_name.apkg'
```

3. Run the script:
```bash
python main.py
```

4. Import the generated `.apkg` file into Anki

## 📄 HTML Structure Requirements

The script expects Udemy's quiz HTML structure with these classes:
```html
<div class="result-pane--question-result-pane--sIcOh">
    <div class="result-pane--question-format--PBvdY">
        <!-- Question text -->
    </div>
    <div class="answer-result-pane--answer-body--cDGY6">
        <!-- Answer options -->
    </div>
    <div class="overall-explanation-pane--overall-explanation--G-hLQ">
        <!-- Explanation -->
    </div>
</div>
```

## 🎨 Card Design

Each flashcard includes:

**Front:**
- Course-specific title
- Question text
- Multiple choice options

**Back:**
- Correct answer highlight
- Detailed explanation
- Incorrect options analysis

## ⚙️ Customization

Modify the card appearance in 

card_style

:

```python
card_style = """
.card {
    /* Your custom styles */
}
"""
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

MIT License - feel free to use and modify!

## 🙏 Acknowledgements

- [Anki](https://apps.ankiweb.net/)
- [genanki](https://github.com/kerrickstaley/genanki)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Udemy](https://www.udemy.com/)

---

Made with ❤️ for effective learning
