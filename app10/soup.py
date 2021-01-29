from bs4 import BeautifulSoup
    
def center_func():
    soup = BeautifulSoup(open('templates/edited.html'), "html.parser")
    soup.find('table')['align'] = 'center'

    #print(soup)
    print(type(soup))
    #f = open("templates/edited.html", "w")
    #f.write("Woops! I have deleted the content!")
    #f.close()
    with open("templates/edited.html", "w") as file:
        file.write(str(soup))
    
    
    #https://stackoverflow.com/questions/17497819/beautifulsoup-adding-attribute-to-tag
    #https://gist.github.com/ScribbleGhost/e5b6a808681004d207a3ee7fdb6ec9ea
    #https://stackoverflow.com/questions/40529848/how-to-write-the-output-to-html-file-with-python-beautifulsoup