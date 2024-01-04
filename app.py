from flask import Flask, render_template,url_for, request, redirect, jsonify, session
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates',static_folder='static')
CORS(app)


@app.route('/', methods=['GET'])
def inicio():
    termo_pesquisa = request.args.get('termo-pesquisa', '')
    return render_template('busca.html')

@app.route('/ajuda.html')
def inicioz():

    return render_template('ajuda.html')

@app.route('/cadastro.html')
def cadastro():
    return render_template('cadastro.html')



@app.route('/buscar', methods=['GET'])
def buscar_links():
    termo = request.args.get('termo')
    
    # Adicione um log para verificar o termo recebido
    print(f"Termo de pesquisa recebido: {termo}")

    if termo == 'vagas TI':
        links = {
           "Vagas na Vagas.com": "https://www.vagas.com.br/vagas-de-ti",
            "Oportunidades no Nerdin": "https://www.nerdin.com.br/vagas",
            "Posições no LinkedIn (Analista de TI)": "https://www.linkedin.com/jobs/analista-de-ti-vagas/",
            "Vagas de Estágio TI no LinkedIn": "https://www.linkedin.com/jobs/estagio-ti-vagas/"

            
        }
        
    elif termo == 'estagio TI':
        links = {
          
            "Estágio em TI na Catho": "https://www.catho.com.br/vagas/estagio-em-ti/brasilia-df/",
            "Estágio TI no Indeed": "https://br.indeed.com/q-est%C3%A1gio-ti-vagas.html",
            "Vagas de Estágio TI no Infojobs": "https://www.infojobs.com.br/vagas-de-emprego-estagio+ti.aspx",
            "Estágio TI no Trabalha Brasil": "https://www.trabalhabrasil.com.br/vagas-empregos/estagio-ti",
            "Estágio TI em Brasília no Glassdoor": "https://www.glassdoor.com.br/Vaga/bras%C3%ADlia-est%C3%A1gio-ti-vagas-SRCH_IL.0,8_IC2494161_KO9,19.htm",
            
        }
    else:
        links = {}
    
    # Adicione um log para verificar os links que estão sendo retornados
    print(f"Links retornados para o termo {termo}: {links}")

    return jsonify(links=links)

@app.route('/api/login', methods=['POST'])
def fazer_login():
    dados = request.json  # Obtenha os dados enviados na requisição POST
    usuario = dados.get('usuario')
    senha = dados.get('senha')

 

    # Verifique as credenciais.
    if usuario == 'gusta' and senha == 'luiz9175':
        return jsonify({'autenticado': True, 'mensagem': 'Login bem-sucedido!'}), 200
    else:
        return jsonify({'autenticado': False, 'mensagem': 'Credenciais inválidas'}), 401

@app.route('/tela-inicial.html')
def telainicial():
    return render_template('tela-inicial.html')

@app.route('/perfil.html')
def perfil():
    return render_template('perfil.html')
if __name__ == '__main__':
    app.run(port=8020, debug=True)
