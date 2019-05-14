from teleporter import *
from matcher import *
from shoter import *
import time

orix=int()
oriy=int()
poslib={'bottom_lef':(-168,194),'bottom_rig':(-148,194),'card_0':(-223,291),'card_1':(-153,291),'card_2':(-83,291),'card_3':(-13,291),'water_sta':(-240,327),'water_end':(-220,347),'bridge_lef':(-255,-105),'bridge_rig':(-55,-105)}
# Backup::poslib={'bottom_lef':(-168,194),'bottom_rig':(-148,194),'card_0':(-223,291),'card_1':(-153,291),'card_2':(-83,291),'card_3':(-13,291),'water_sta':(-271,327),'water_end':(-216,347),'bridge_lef':(-255,-15),'bridge_rig':(-55,-15)}

def get_water_image():
  shot("cur_water.png",orix+poslib['water_sta'][0],oriy+poslib['water_sta'][1],orix+poslib['water_end'][0],oriy+poslib['water_end'][1])

def get_ori():
  global orix,oriy
  shot("cur_screen.png")
  orix,oriy=match_pos("cur_screen.png","Sources/core.png")
  print("Ori Token: ("+str(orix)+","+str(oriy)+")")

def display_bypos(card,desx,desy):
  click(orix+poslib[card][0],oriy+poslib[card][1])
  time.sleep(0.1)
  click(desx,desy)

def display_byname(card,name):
  click(orix+poslib[card][0],oriy+poslib[card][1])
  time.sleep(0.1)
  click(orix+poslib[name][0],oriy+poslib[name][1])

if __name__=='__main__':
  print("Surgeon Here")
