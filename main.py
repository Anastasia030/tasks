from ru_local import *

DAY = int(input())
SPEED = 38241                                                 # Probe speed in miles/h.
SPEED_WAVES = 299792458                                       # The speed of propagation of radio waves in m/s.
DISTANCE_SUN = 149597870                                      # Distance from the Earth to the Sun in km.

distance_ml = DAY * 24 * SPEED + 16637000000
distance_km = distance_ml * 1.609344
distance_ae = distance_ml * 0.0000000108
delay = (distance_km - DISTANCE_SUN)/(SPEED_WAVES * 3.6)

print(PART_1, DAY, PART_2, distance_ml, PART_3, round(distance_km, 2), PART_4, round(distance_ae, 2), PART_5)
print(PART_6, round(delay, 2), PART_7)

