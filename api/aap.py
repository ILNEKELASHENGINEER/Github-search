from socket import gethostname
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        # links = generate_links(input_text)
        # return render_template('result.html', links=links)
    return render_template('index.html')

def generate_links(input_text):
    # Your code to generate the list of links goes here
    pass

@app.route('/results', methods=['POST']) 
def results(): 
  
    # Get the form data as Python ImmutableDict datatype  
    data = request.form
    input = data['input_text'] 
    print(input)
    
    def find_github_repositories(topic):
        url = f"https://api.github.com/search/repositories?q={topic}"
        response = requests.get(url)
        data = response.json()
        repositories = data["items"]
        return repositories
    list=[]
    repositories = find_github_repositories(input)
    for repository in repositories:
        list.append(repository["html_url"])
    # print(repository["name"], repository["html_url"])
    print(list)
  
    ## Return the extracted information  
    return render_template('list.html', links=list)

if __name__ == '__main__':
    if 'liveconsole' not in gethostname():
        app.run()
