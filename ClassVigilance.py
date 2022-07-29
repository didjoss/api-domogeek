#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Gruik coded by GuiguiAbloc
# http://blog.guiguiabloc.fr
# http://api.domogeek.fr
#

import urllib
from xml.dom import minidom

Nom_color = ( 'Vert', 'Vert','Jaune','Orange','Rouge' )
Nom_risk = ( 'RAS', 'vent', 'pluie-inondation', 'orages', 'inondations', 'neige-verglas', 'canicule', 'grand-froid' )
class vigilance:
  def getvigilance(self, deprequest):
    if len(deprequest) != 2:
      return "Error in department number"
    url = 'http://vigilance.meteofrance.com/data/NXFR34_LFPW_.xml'
    dom = minidom.parse(urllib.urlopen(url))
    for all in dom.getElementsByTagName('datavigilance'):
         depart = all.attributes['dep'].value
         colorresult = all.attributes['couleur'].value
         riskresult = "0"
         flood = "0"
         for risk in all.getElementsByTagName('risque'):
              riskresult = risk.attributes['valeur'].value
         for flood in all.getElementsByTagName('crue'):
              floodresult = flood.attributes['valeur'].value
         if not riskresult: 
           riskresult = "0"
         if depart == deprequest:
           return Nom_color[int(colorresult)],Nom_risk[int(riskresult)],Nom_color[int(floodresult)]
           
