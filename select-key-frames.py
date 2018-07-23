##[TBT-Tools]=group
##Input_Footprints=vector
##Image_IDs=field Input_Footprints
##Overlap_Threshold_0_to_1=number 0.6

from qgis.utils import *
from osgeo import ogr
from osgeo import osr

KEEP_TRESHOLD=Overlap_Threshold_0_to_1
IMAGE_IDS = Image_IDs

def calcIntersection(fpA,fpB):
    fpA = fpA.Buffer(0)
    if not fpA.Intersect(fpB):
        return False, 0
    if fpA.Intersect(fpB):
        areaOfIntersection = fpA.Intersection(fpB).GetArea()
        percentOfIntersection = areaOfIntersection/(fpB.GetArea())
        return True,percentOfIntersection

def getFPs(fpIn,IMAGE_IDS):
    '''SQLite of Footprints as input, selects key frames based on overlap thresehold'''
    fp = ogr.Open(fpIn,0)
    progress.setText(fpIn)
    fpLayer = fp.GetLayer(0) #assumes the footprints are the first layer
    newGeom = ogr.Geometry(type=ogr.wkbGeometryCollection)
    numFps = fpLayer.GetFeatureCount()
    IMAGE_IDS = IMAGE_IDS.encode('utf-8') # str is imported from future, sets type to newstr. ogr does not recognize
    currFp = fpLayer.GetFeature(1) # get first geom to populate the keepers poly
    currFpGeom = currFp.geometry()
    keepGeom = ogr.Geometry(type=ogr.wkbGeometryCollection) # create a geom to hold keepers
    keepGeom.AddGeometry(currFpGeom) # add first fp
    keepList = [1,numFps] # list to hold the keepers ids, with first and last frame.
    keepers = 0
    for i in range(2,numFps):
        currFp = fpLayer.GetFeature(i)
        nextFp = fpLayer.GetFeature(i+1)
        thisImage = currFp.GetField(IMAGE_IDS)
        nextImage = nextFp.GetField(IMAGE_IDS)
        thisTime = int(thisImage[-8:])
        nextTime = int(nextImage[-8:])
        absDiff = abs(nextTime-thisTime)
        if absDiff > 30:
            keepList.append(i)
            continue
        a = keepGeom
        b = currFp.geometry()
        doesIntersect, percentIntersect = calcIntersection(a,b)
        if percentIntersect < KEEP_TRESHOLD:
            keepGeom.AddGeometry(b)
            keepers += 1
            keepList.append(i)
    keepTxt = 'keeping %s of of %s images' %(keepers,numFps)
    progress.setInfo(keepTxt)
    time.sleep(1)
    fpLayer = processing.getObject(fpIn)
    fpLayer.select(keepList)   
    return keepList

fpIn = Input_Footprints
fps = getFPs(fpIn,IMAGE_IDS)
