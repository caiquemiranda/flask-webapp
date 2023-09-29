from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/projetos/<int:projeto_id>')
def projeto_detalhes(projeto_id):
    projeto = projetos[projeto_id - 1]
    return render_template('projeto_detalhes.html', projeto=projeto)

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
