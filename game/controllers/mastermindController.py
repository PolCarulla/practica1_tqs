class MasterMindController:
    model = None
    view = None

    def setView(self,view):
        self.view = view
    
    def setModel(self,model):
        self.model = model
        
    def start_menu(self):
        self.view.displayMenu()

    def runGame(self):
        pass