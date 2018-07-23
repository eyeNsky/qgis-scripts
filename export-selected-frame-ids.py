##[TBT-Tools]=group
##Input_Footprints=vector
##Image_IDs=field Input_Footprints
##Output_Image_List=folder
from qgis.utils import *
from osgeo import ogr
from osgeo import osr

IMAGE_IDS = Image_IDs
outDir = Output_Image_List

if len(outDir) == 0:
    outDir = os.environ['HOME']

outDir = os.path.join(outDir,'image.list')

def getFPs(fpIn,IMAGE_IDS):
    '''Write selected image names to file'''
    layer = processing.getObject(fpIn)
    selected = layer.selectedFeatures()
    numImages = len(selected)
    IMAGE_IDS = IMAGE_IDS.encode('utf-8')
    fout = open(outDir,'w')
    for sf in selected:
        thisImage = sf.attribute(IMAGE_IDS)
        progress.setInfo(thisImage)
        outTxt = '%s.jpg\n' % thisImage
        fout.write(outTxt)
    fout.close()    
fpIn = Input_Footprints
progress.setText(fpIn)
fps = getFPs(fpIn,IMAGE_IDS)
