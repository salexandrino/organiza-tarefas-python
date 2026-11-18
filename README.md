Organiza Tarefas em Python 📝
Projeto de organização de tarefas desenvolvido em Python para apoiar a Oficina Introdutória de Git e GitHub, promovida pela Diretoria de Ensino da SLOTH.

Durante a oficina, usaremos este projeto para conhecer o código, acompanhar alterações e praticar o versionamento com Git e GitHub.
🎯 Objetivos
- Entender como um repositório organiza os arquivos e o histórico de um projeto.
- Praticar comandos como clone, status, add, commit, switch, merge e push.
- Criar uma branch para desenvolver uma melhoria.
- Trabalhar com funções, listas, estruturas de repetição e validação de entradas em Python.
🛠️ Pré-requisitos
- Python 3 instalado.
- Git instalado.
- Uma conta no GitHub para publicar suas alterações.
- Um editor de código, como o Visual Studio Code.
Confira as instalações no terminal:
python --version
git --version
No Linux, pode ser necessário usar python3 --version no primeiro comando.
🚀 Como executar
1. Clone o repositório:
git clone https://github.com/salexandrino/organiza-tarefas-python.git
2. Entre na pasta do projeto:
cd organiza-tarefas-python
3. Execute o programa:
python tarefas.py
No Linux, se necessário, use python3 tarefas.py.
💻 Exercício da oficina: editar tarefa
O desafio é acrescentar ao programa a possibilidade de editar o título de uma tarefa.
1. Crie a função editar_tarefa(tarefas) e adicione a opção 5 - Editar tarefa ao menu e à função main().
2. Mostre as tarefas e solicite o ID. Reaproveite as funções listar_tarefas, solicitar_id e buscar_tarefa.
3. Solicite um novo título, remova os espaços das extremidades e aceite apenas um texto não vazio.
4. Atualize somente o título, preservando o ID e a situação da tarefa.
5. Informe quando não houver tarefas, quando o ID for inválido ou quando a tarefa não existir.
Teste sua implementação: cadastre Estudar Git, edite para Revisar branches e confira a listagem. Teste também letras no ID, um ID inexistente e um título formado apenas por espaços. Em caso de edição inválida, o título anterior deve ser preservado.
🌱 Prática com Git
Antes de começar, verifique se você está na branch principal e se não há alterações pendentes:
git switch main
git status
Crie uma branch para a melhoria:
git switch -c feat/editar-tarefa
Depois de implementar e testar, confira e registre suas alterações:
git status
git diff
git add tarefas.py
git commit -m "Adiciona edição do título das tarefas"
Volte à branch principal, integre a melhoria e execute o programa novamente:
git switch main
git merge feat/editar-tarefa
python tarefas.py
Publicando suas alterações
Para enviar mudanças ao GitHub, você precisa ter permissão de escrita no repositório de destino. Para trabalhar na sua própria conta, faça primeiro um fork deste projeto no GitHub e clone o endereço do seu fork. Se já clonou o original, você também pode adicionar seu fork como outro remoto:
git remote add meu-fork https://github.com/SEU-USUARIO/organiza-tarefas-python.git
git push -u meu-fork main
Substitua SEU-USUARIO pelo seu nome de usuário. Se você clonou diretamente o seu fork, pode usar git push -u origin main. Confira o commit e o código atualizado na página do repositório.
👩‍🏫 Equipe da oficina
- Ministrantes: Sthefanny Lara e Clara Eunice
- Colaborador: José Everton
- Organização: Diretoria de Ensino — SLOTH
