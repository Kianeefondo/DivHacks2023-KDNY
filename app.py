from flask import Flask, jsonify, render_template
from flask_cors import CORS
import json
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/questions', methods=['GET'])
def get_questions():
    f = open('questions.json')
    questions = json.load(f)
    columns = ['id', 'question', 'answer', 'wrongAnswer1', 'wrongAnswer2', 'wrongAnswer3', 'topic']

    table = pd.DataFrame(questions, columns=columns)
    data = table.values.tolist()
    # table = df.to_html(index=False)
    print(f"Table content: {table}")
    return render_template("index.html", table=data)
    '''return jsonify(questions)'''





if __name__ == '__main__':
    app.run(debug=True, port=3080)