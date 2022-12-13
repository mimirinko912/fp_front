# importing the eel library
import eel
# initializing the application
eel.init("../fp_front")

# using the eel.expose command
@eel.expose
# defining the function for addition of two numbers
def add(data_1, data_2):
    int1 = int(data_1)
    int2 = int(data_2)

    #print(int1,int2) success get :) ^\0m0/^
    output = int1 + int2
    return output

# starting the application
eel.start('myWebpage.html')
