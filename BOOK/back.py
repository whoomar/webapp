import eel

eel.init('BOOK')

@eel.expose

def App() :
    print("Application running")

App()

eel.start("index.html", size=(500,600))