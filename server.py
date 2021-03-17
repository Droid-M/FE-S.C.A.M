from flask import Flask, render_template


app = Flask(__name__, template_folder='templates', static_folder='static')

menus = {
    'Hello World': {
        'title': 'Hello World',
        'data-feather': 'hello-world',
        'url': '/'
    },
    'Cadastrar Paciente': {
        'title': 'Cadastrar Paciente',
        'data-feather': 'cadastrar-paciente',
        'url': '/cadastrar_paciente'
    },
    'Listar Pacientes': {
        'title': 'Listar Pacientes',
        'data-feather': 'listar-pacientes',
        'url': '/listar_pacientes'
    },
    'Cadastrar Medicamento': {
        'title': 'Cadastrar Medicamento',
        'data-feather': 'cadastrar-medicamento',
        'url': '/'
    },
    'Cadastrar Enfermeiro': {
        'title': 'Cadastrar Enfermeiro',
        'data-feather': 'cadastrar-enfermeiro',
        'url': '/cadastrar_enfermeiro'
    },
    'Listar Enfermeiros': {
        'title': 'Listar Enfermeiros',
        'data-feather': 'listar-enfermeiros',
        'url': '/listar_enfermeiros'
    }
}


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/')
def hello_world():
    menulist = menus
    active = menulist['Hello World']

    title = 'Hello World'
    return render_template('hello_world.html', **locals())


@app.route('/cadastrar_paciente')
def cadastro_de_paciente():
    menulist = menus
    active = menulist['Cadastrar Paciente']
    remedios = []
    for i in range(1, 21):
        new_remedio = {
            'id': i,
            'nome': f'Remédio {i}'
        }
        remedios.append(new_remedio)

    title = menulist['Cadastrar Paciente']['title']
    return render_template('cadastro_paciente.html', **locals())


@app.route('/cadastrar_enfermeiro')
def cadastro_de_enfermeiro():
    menulist = menus
    active = menulist['Cadastrar Enfermeiro']

    title = menulist['Cadastrar Enfermeiro']['title']
    return render_template('cadastro_enfermeiro.html', **locals())


@app.route('/listar_pacientes')
def listar_pacientes():
    menulist = menus
    active = menulist['Listar Pacientes']
    export = True

    pacientes = [
        {
            'id': 1,
            'nome': 'Pedro Antonio Nunes Moreira',
            'cpf': '883.834.233-11'
        },
        {
            'id': 2,
            'nome': 'Fulano de Oliveira',
            'cpf': '863.233.834-11'
        }
    ]

    title = menulist['Listar Pacientes']['title']
    return render_template('relatório_pacientes.html', **locals())


@app.route('/listar_enfermeiros')
def listar_enfermeiros():
    menulist = menus
    active = menulist['Listar Enfermeiros']

    enfermeiros = [
        {
            'id': 1,
            'nome': 'Pedro Antonio Nunes Moreira',
            'cpf': '883.834.233-11'
        },
        {
            'id': 2,
            'nome': 'Fulano de Oliveira',
            'cpf': '863.233.834-11'
        }
    ]

    title = menulist['Listar Enfermeiros']['title']
    return render_template('relatorio_enfermeiros.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
