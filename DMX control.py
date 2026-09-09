from PyDMXControl.controllers import OpenDMXController
from PyDMXControl.profiles.Generic import Dimmer
from PyDMXControl.profiles.Generic import Custom

dmx = OpenDMXController()

profile = dmx.add_fixture(Custom, 6, "Profile - event lighting") # 1: master dim 2: fine dim 3: strobe 4: effects 5: effect speed 6: dimming curve
fresnel = dmx.add_fixture(Custom, 10, "Fresnel - event lighting") # 1: dim 2: red 3: green 4: blue 5: amber 6: lime 7: cool white 8: strobe 9: fine dim 10: zoom 
par_can_event = dmx.add_fixture(Custom, 6, "Par Cam - event lighting") # 1: dim 2: strobe 3: red 4: green 5: blue 6: amber/ white
par_can_show = dmx.add_fixture(Custom, 10, "Par Can - show tech") # 1: red 2: green 3: blue 4: white 5: amber 6: UV 7: dim 8: color jump/ fade 
wall_washer = dmx.add_fixture(Custom, 3, "Wall Washer - beamz") # 1: red 2: green 3: blue
dimmer = dmx.add_fixture(Dimmer, 4, "4 channel dimmer") 