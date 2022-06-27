from motorcycle import Motorcycle
from bus import Bus

b = Bus('Bus',4,120)
b.set_vin('v1234')
b.set_color('Blue')
b.set_capacity(34)
b.v_detail()
b.bus_detail()

m = Motorcycle('Motocycle',2,100)
m.set_cc(1200)
m.set_vin('v3456')
m.bike_detail()