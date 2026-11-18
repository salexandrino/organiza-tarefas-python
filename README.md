# Organiza Tarefas em Python 📝

Projeto de organização de tarefas desenvolvido em Python para apoiar a **Oficina Introdutória de Git e GitHub**, promovida pela Diretoria de Ensino da SLOTH.

Durante a oficina, usaremos este projeto para conhecer o código, acompanhar alterações e praticar o versionamento com Git e GitHub.

## 🎯 Objetivos

- Entender como um repositório organiza os arquivos e o histórico de um projeto.
- Praticar comandos como `clone`, `status`, `add`, `commit`, `switch`, `merge` e `push`.
- Criar uma branch para desenvolver uma melhoria.
- Trabalhar com funções, listas, estruturas de repetição e validação de entradas em Python.

## 🛠️ Pré-requisitos

Para acompanhar a atividade, você precisará de:

- Python 3 instalado.
- Git instalado.
- Uma conta no GitHub para publicar suas alterações.
- Um editor de código, como o Visual Studio Code.

Para conferir as instalações, abra o terminal e execute:

```bash
python --version
git --version
```

No Linux, pode ser necessário usar `python3 --version` no primeiro comando.

## 🚀 Como executar o projeto

### 1. Clone o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/salexandrino/organiza-tarefas-python.git
```

### 2. Entre na pasta do projeto

```bash
cd organiza-tarefas-python
```

### 3. Execute o programa

```bash
python tarefas.py
```

No Linux, se necessário, utilize:

```bash
python3 tarefas.py
```

## 💻 Exercício da oficina: editar tarefa

O desafio é acrescentar ao programa a possibilidade de editar o título de uma tarefa.

### O que implementar

1. Crie a função `editar_tarefa(tarefas)`.
2. Adicione a opção **5 - Editar tarefa** ao menu e à função `main()`.
3. Mostre as tarefas e solicite o ID. Reaproveite as funções `listar_tarefas`, `solicitar_id` e `buscar_tarefa`.
4. Solicite um novo título e remova os espaços das extremidades.
5. Aceite apenas um título que não esteja vazio.
6. Atualize somente o título, preservando o ID e a situação da tarefa.
7. Informe quando não houver tarefas, quando o ID for inválido ou quando a tarefa não existir.

### Teste sua implementação

- Cadastre a tarefa `Estudar Git`.
- Edite o título para `Revisar branches`.
- Confira a listagem de tarefas.
- Tente informar letras no lugar do ID.
- Tente informar um ID que não existe.
- Tente informar um título contendo apenas espaços.

O programa deve continuar funcionando e preservar o título anterior quando a edição for inválida.

## 🌱 Prática com Git

### 1. Confira o estado do repositório

Antes de começar, verifique se você está na branch principal e se não há alterações pendentes:

```bash
git switch main
git status
```

### 2. Crie uma branch para a melhoria

```bash
git switch -c feat/editar-tarefa
```

Agora, implemente a função de edição e teste o programa.

### 3. Confira e registre as alterações

```bash
git status
git diff
git add tarefas.py
git commit -m "Adiciona edição do título das tarefas"
```

### 4. Integre a melhoria à branch principal

```bash
git switch main
git merge feat/editar-tarefa
```

Execute o programa novamente para conferir se tudo continua funcionando:

```bash
python tarefas.py
```

### 5. Publique suas alterações no GitHub

Para enviar mudanças ao GitHub, você precisa ter **permissão de escrita** no repositório de destino.

Uma opção é criar um **fork** deste projeto na sua conta e clonar o endereço do seu próprio fork. Nesse caso, depois de integrar suas alterações à `main`, execute:

```bash
git push -u origin main
```

Se você já clonou o repositório original e criou um fork depois, pode adicionar seu fork como outro remoto:

```bash
git remote add meu-fork https://github.com/SEU-USUARIO/organiza-tarefas-python.git
git push -u meu-fork main
```

Substitua `SEU-USUARIO` pelo seu nome de usuário no GitHub.

Por fim, abra o repositório no GitHub e confira se o commit e o código atualizado aparecem.

## 👩‍🏫 Equipe da oficina

- **Ministrantes:** Sthefanny Lara e Clara Eunice
- **Colaborador:** José Everton
- **Organização:** Diretoria de Ensino — SLOTH
