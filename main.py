import glob
from bs4 import BeautifulSoup
import genanki
import random
import html

name_file = "xyz"
html_folder = r'user\path\to\html\folder'
output_file = f'{name_file}.apkg'

card_style = """
.card {
    font-family: arial;
    font-size: 16px;
    text-align: left;
    color: black;
    background-color: white;
    line-height: 1.8;
    padding: 25px;
    max-width: 800px;
    margin: 0 auto;
}
.title {
    font-size: 20px;
    font-weight: bold;
    color: #2b6dad;
    margin-bottom: 25px;
    padding-bottom: 15px;
    border-bottom: 2px solid #eee;
}
.question { 
    margin: 30px 0;
    line-height: 1.8;
    font-size: 17px;
}
.answers-section {
    margin-top: 30px;
}
.answers-title {
    font-weight: bold;
    color: #555;
    margin-bottom: 20px;
}
.option { 
    margin: 25px 0;
    padding-left: 25px;
}
.correct { 
    color: #2d5a27;
    font-weight: bold;
    margin: 25px 0;
    padding: 20px;
    background-color: #f5f9f5;
    border-radius: 5px;
}
.explanation { 
    margin-top: 45px;
    padding-top: 25px;
    border-top: 2px solid #eee;
    line-height: 1.8;
}
.section-title {
    font-weight: bold;
    color: #444;
    margin: 20px 0 15px 0;
}
.explanation-item {
    margin: 15px 0;
    padding-left: 20px;
}
"""

model_id = random.randrange(1 << 30, 1 << 31)
model = genanki.Model(
    model_id,
    'AWS ML Specialty Flashcard',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'}
    ],
    templates=[{
        'name': 'Card 1',
        'qfmt': '''
            <div class="card">
                {{Question}}
            </div>
        ''',
        'afmt': '''
            <div class="card">
                {{FrontSide}}
                <hr id="answer">
                {{Answer}}
            </div>
        ''',
        'css': card_style,
    }]
)

deck_id = random.randrange(1 << 30, 1 << 31)
deck = genanki.Deck(deck_id, 'AWS ML Specialty')

def clean_text(text):
    text = html.escape(text)
    text = text.replace('\n', '<br>')
    return text

def format_explanation(text):
    parts = text.split('Incorrect options:')
    
    if len(parts) == 2:
        main_explanation = parts[0].strip()
        incorrect_options = parts[1].strip()
        
        incorrect_items = [item.strip() for item in incorrect_options.split('Incorrect Choice:') if item.strip()]
        
        formatted_text = f'<div class="explanation-item">• {main_explanation}</div><br><br>'
        formatted_text += '<div class="section-title">Incorrect options:</div><br>'
        
        for item in incorrect_items:
            if item:
                formatted_text += f'<div class="explanation-item">• {item}</div><br><br>'
            
        return formatted_text
    else:
        return f'<div class="explanation-item">• {text}</div>'

for html_file in glob.glob(f'{html_folder}\*.html'):
    print(f"Processing {html_file}...")
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        question_blocks = soup.find_all('div', class_='result-pane--question-result-pane--sIcOh')
        if not question_blocks:
            print(f"Warning: No questions found in {html_file}!")
            continue
            
        for block in question_blocks:
            question_elem = block.find('div', class_='result-pane--question-format--PBvdY')
            if not question_elem:
                print(f"Warning: Missing question in {html_file}!")
                continue
            q_text = clean_text(question_elem.get_text(strip=True))
            
            answer_items = block.find_all('div', class_='answer-result-pane--answer-body--cDGY6')
            if not answer_items:
                print(f"Warning: Missing answers in {html_file}!")
                continue

            formatted_answers = []
            correct_answer_text = ''
            for answer_item in answer_items:
                parent = answer_item.find_parent('div', class_='answer-result-pane--answer-correct--PLOEU')
                is_correct = parent is not None
                
                answer_text = clean_text(answer_item.get_text(strip=True))
                formatted_answers.append(f'<div class="option">○ {answer_text}</div><br><br>')
                
                if is_correct:
                    correct_answer_text = answer_text

            answers_text = '\n'.join(formatted_answers)

            explanation = block.find('div', class_='overall-explanation-pane--overall-explanation--G-hLQ')
            if not explanation:
                print(f"Warning: Missing explanation in {html_file}!")
                continue
            explanation_text = clean_text(explanation.get_text(strip=True))
            explanation_text = format_explanation(explanation_text)

            front = f'''
                <div class="title">AWS ML Specialty Question</div>
                <div class="question">{q_text}</div>
                <div class="answers-section">
                    <div class="answers-title">Answer Options:</div>
                    <br>
                    {answers_text}
                </div>
            '''
            
            back = f'''
                <div class="title">AWS ML Specialty Answer</div>
                <div class="correct">
                    <div class="section-title">✓ Correct Answer:</div>
                    {correct_answer_text}
                </div>
                <div class="explanation">
                    <div class="section-title">
                        <br><br>
                        Detailed Explanation:</div>
                    {explanation_text}
                </div>
            '''

            note = genanki.Note(
                model=model,
                fields=[front.strip(), back.strip()]
            )
            deck.add_note(note)

genanki.Package(deck).write_to_file(output_file)
print(f"Anki deck saved to {output_file}")