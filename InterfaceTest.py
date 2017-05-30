#In this Interface script, an object of class "figureCreate" is created for each of
#the ___ models in the journal article titled _______. The name of each of these objects
#is simply "Figure_" + the Figure number (e.g. Figure_1).  Each figureCreate object
#has 4 attributes:
#   1) The Figure number
#   2) The Main Model needed to generate the data within the figure
#   3) The specific cross-bridge model that the main model requires
#   4) The specific Ca2+ model that the main model requires

#import matplotlib.pyplot as plt

class figureCreate:
    def __init__(self, figureNumber, mainModel, xbModel, ca2Model, xVariables, yVariables):
        self.figureNumber = figureNumber
        self.mainModel = mainModel
        self.xbModel = xbModel
        self.ca2Model = ca2Model
        self.xVariables = xVariables
        self.yVariables = yVariables
        

def main():
    Figure_1 = figureCreate(1, "Main", "XB", "Ca2", ["xdata1", "xdata2", "xdata3"], ["ydata1", "ydata2", "ydata3"])
    print(Figure_1.xVariables[2])

    #Depending on the number of figures ("x"), there will be x number of "Figure_x" objects 


    #Once each Figure from article ____ has a corresponding object of the class figureCreate,
    #A mechanism will be developed that grabs the appropriate models and runs them on hpc
    #based on what figure (Figure_1, Figure_2, etc...) the user wants to replicate.

    userInput = input("Please type the Figure number you wish to reproduce: ")
    fig2Reproduce = "Figure_" + userInput
    print("Reproducing " + fig2Reproduce + ", please wait")

    #Run the MeganModel

    #Create the .csv output data file (this could happen in the protocol .py document itself?)

    #Plot the figure!
    lengthData = len(Figure_1.xVariables)
    print(lengthData)

    
    #data2Plot = 
    #plt.plot(

if __name__ == "__main__":
    main()



