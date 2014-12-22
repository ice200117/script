

#-----------------------------------------------------
# Author: Yaqiang Wang
# Date: 2014-11-30
# Purpose: Get and plot grid data
# Note: Sample
#-----------------------------------------------------
#---- Import classes
print 'Import classes...'
from org.meteoinfo.layout import MapLayout
from org.meteoinfo.data.mapdata import MapDataManage
from org.meteoinfo.data.meteodata import MeteoDataInfo, DrawMeteoData
from org.meteoinfo.layout import LegendStyles
from org.meteoinfo.global import Extent
from org.meteoinfo.layer import VectorLayer
from org.meteoinfo.shape import ShapeTypes
from org.meteoinfo.table import DataTypes
from org.meteoinfo.shape import PointShape
from org.meteoinfo.global import PointD
from org.meteoinfo.geoprocess import GeoComputation
import os
from java.awt import Color
from javax.swing import JFrame
 
#---- Set directories
print 'Set directories...'
mapDir = 'c:/share/map'

#---- Create MapLayout object
mapLayout = MapLayout()
mapFrame = mapLayout.getActiveMapFrame()
 
#---- Load country layer
print 'Load country layer...'
countryLayer = MapDataManage.loadLayer(os.path.join(mapDir, 'poly_region.shp'))
lb = countryLayer.getLegendScheme().getLegendBreaks().get(0)
lb.setDrawFill(False)
lb.setOutlineColor(Color.blue)
mapFrame.addLayer(countryLayer)
 
#---- Create MeteoDataInfo object
mdi = MeteoDataInfo()
 
#---- Open a GrADS data file
# fn = os.path.join(dataDir, 'GrADS/model.ctl')
# mdi.openGrADSData(fn)
 
#---- Get grid data
#mdi.setTimeIndex(2)
#mdi.setLevelIndex(3)
#gdata = mdi.getGridData('Z')
#gdata.extendToGlobal()

 

#---- Create a grid point and determine grid points are in or out of Tibet
nLayer = VectorLayer(ShapeTypes.Point)
nLayer.setLayerName("nLayer")
nLayer.setVisible( True)
fieldName = "Inside"
nLayer.editAddField(fieldName, DataTypes.String)

print 'The points inside Tibet are:'
tibetArea = countryLayer.getShapes()[107]

sLon = 110.05
sLat = 35.85
delt = 0.1
print 'x     y      long    lat'
for i in range(0, 120):
  lon = sLon + i * delt
  for j in range(0, 70):
    
    aPS = PointShape()    
    lat = sLat + j * delt
    #print lon, lat
    aPoint = PointD(lon, lat)
    aPS.setPoint( aPoint)
    shapeNum = nLayer.getShapeNum()
    #print "Shape Number: %d" % (shapeNum)
    nLayer.editInsertShape(aPS, shapeNum)
    if GeoComputation.pointInPolygon(tibetArea, aPoint):
      nLayer.editCellValue(fieldName, shapeNum, "Y")
      print i+1, '  ',  j+1, '   ',  "%5.2f  %5.2f" % (lon, lat)
    else:
      nLayer.editCellValue(fieldName, shapeNum, "N")

#print "Layer Name: %s" % (nLayer.getLayerName())
mapFrame.addLayer(nLayer) 
#nLayer.saveFile()  
#print 'Finished!'
