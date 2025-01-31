# assistent-pdf-crewai

Criando um assistente para leitura de um PDF utlizando o crewai e o streamlit

## Comandos

### Instalar a versão do Pyhon do projeto
```bash
pyenv update
pyenv install --list | grep '3.12.9'
# ou
pyenv install 3.12.1
pyenv global 3.12.1
python --version
python3 --version
pyenv versions

```
### Virtual environment

#### Criar e Ativar

```bash
python -m venv .venv

source .venv/bin/activate
# ou
. .venv/Scripts/Activate

pip install -r requirements.txt
```

#### Desativar

```bash
deactivate
```
### Streamlit
#### Executar
```bash
streamlit run chat.py 
```
