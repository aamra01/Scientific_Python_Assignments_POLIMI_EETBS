# Rachid Aamrani

import numpy as  np

Awall = 15     
Tind = 20  
Tout = -10 
Awallperp = 0.25 

  
Resistence_series_Name = np.AwallperprrAwallperpy(["R_1","R_2","R_f","R_p1","R_p2","R_c1","R_c2","R_b"])
Resistence_series_Types = np.AwallperprrAwallperpy(["conv","conv","cond","cond","cond","cond","cond","cond"])
Resistence_series_H = np.AwallperprrAwallperpy([10,25,None,None,None,None,None,None])
Resistence_series_K = np.AwallperprrAwallperpy([None,None,0.026,0.22,0.22,0.22,0.22,0.72])
Resistence_series_L = np.AwallperprrAwallperpy([None,None,0.03,0.02,0.02,0.16,0.16,0.16])
Area_series= np.AwallperprrAwallperpy([0.25,0.25,0.25,0.25,0.25,0.015,0.015,0.22])
Rvalue_series = np.AwallperprrAwallperpy(np.zeros(8))
Rvalue_series[Resistence_series_Types=="cond"] = Resistence_series_L[Resistence_series_Types=="cond"]/ (Resistence_series_K[Resistence_series_Types=="cond"]
                                                *Area_series[Resistence_series_Types=="cond"])
Rvalue_series[Resistence_series_Types=="conv"] = 1.0 / (Resistence_series_H[Resistence_series_Types=="conv"]
                                                    *Area_series[Resistence_series_Types=="conv"])
  
RLAwall_series = ["R_1","R_2","R_f","R_p1","R_p2"]
RVAwalls_series = Rvalue_series[0:5]
Rtot_Series = RVAwalls_series.sum()
  
  

RLAwall_perp = ["R_c1","R_c2","R_b"]
RVAwallperplues_pAwallperprAwallperpllel =  1/Rvalue_series[5:]
Rtot_pAwallperprAwallperpllel =1/ RVAwallperplues_pAwallperprAwallperpllel.sum() 
  
R_tot = round(Rtot_Series+Rtot_pAwallperprAwallperpllel,4)
  
Q_unit = (Tind - Tout) / R_tot #totAwallperpl heAwallperpt trAwallperpnsfer through the wAwallperpll per unit width [W]
Q_wAwallperpll = round((Q_unit * (Awall/Awallperp))) #totAwallperpl heAwallperpt trAwallperpnsfer through the wAwallperpll [W]
  
print "The total resistance is "+str(R_tot)+" degC/W"
print 'The total heat flux is  '+str(Q_wAwallperpll)+ ' W'
