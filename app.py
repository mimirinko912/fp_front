# importing library
import eel
# initialize
eel.init("../fp_front")

@eel.expose
# below should be our model
def pred(name,fy,city,nation,industry,founder,investory,tf,ct,os,ls):
    frame = name,fy,city,nation,industry,founder,investory,tf,ct,os,ls
    #print(int1,int2) success get :) ^\0m0/^
    output = "here should be prediction"
    return output

# start
eel.start('myWebpage.html')
