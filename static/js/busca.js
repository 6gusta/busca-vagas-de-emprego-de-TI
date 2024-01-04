<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

      function mudarCor(elemento) {
        elemento.classList.toggle('clicked');
    }

    function verificarEnter(event) {
        if (event.key === 'Enter') {
            handleMostrarResultado();
        }
    }

    function fecharDiv() {
        document.getElementById('cep').style.display = 'none';
    }

    async function handleMostrarResultado() {
        var barraPesquisa = document.getElementById('busca');
        var resultadoDiv = document.getElementById('resultado');

        if (barraPesquisa.value.trim() !== '') {
            resultadoDiv.innerHTML = 'Resultado para: ' + barraPesquisa.value;

            try {
                const response = await axios.get('/buscar-vagas', {
                    params: { 'termo-pesquisa': barraPesquisa.value }
                });

                exibirResultados(response.data);
            } catch (error) {
                console.error('Erro na requisição:', error);
            }

            document.getElementById('cep').style.display = 'block';
        } else {
            resultadoDiv.innerHTML = 'O campo está vazio, tente novamente...';
            document.getElementById('cep').style.display = 'block';
        }
    }
  
    function exibirResultados(data) {
        var resultadoDiv = document.getElementById('resultado');

        resultadoDiv.innerHTML = ''; // Limpa resultados anteriores

        if (data && data.results && data.results.length > 0) {
            var results = data.results;

            var ul = document.createElement('ul');
            results.forEach(function (vaga) {
                var li = document.createElement('li');
                li.innerHTML = '<strong>Cargo:</strong> ' + (vaga.title || 'N/A') + '<br>' +
                                '<strong>Empresa:</strong> ' + ((vaga.company && vaga.company.display_name) || 'N/A') + '<br>';
                ul.appendChild(li);
            });

            resultadoDiv.appendChild(ul);
        } else {
            resultadoDiv.innerHTML = 'Nenhuma vaga encontrada.';
        }

        // Certifique-se de exibir a div após a atualização dos resultados
        document.getElementById('cep').style.display = 'block';
    }





