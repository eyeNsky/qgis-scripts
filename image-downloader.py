##[TBT-Tools]=group
##Input_Footprints=vector
##Output_Directory= folder

import os,urllib
outDir = Output_Directory

if len(outDir) == 0:
    outDir = os.environ['HOME']
from qgis.utils import *
# Get  vector from canvas, must be loaded with features selected.
layer = processing.getObject(Input_Footprints)
selected = layer.selectedFeatures()
numImages = len(selected)

progress.setText('Downloading %s images to %s'%(numImages,outDir))
if numImages == 0:
    progress.setText( 'No images selected for download!' )
for sf in selected:
    imgName = sf.attribute('url')
    thisTif = str(imgName)
    thisVrt = imgName.replace('.tif','.vrt')
    tifSave = os.path.basename(thisTif)
    vrtSave = os.path.basename(thisVrt)
    tifOutPath = os.path.join(outDir,tifSave)
    vrtOutPath = os.path.join(outDir,vrtSave)
    progress.setText('Downloading: %s '%imgName)
    urllib.urlretrieve(thisTif,tifOutPath)
    urllib.urlretrieve(thisVrt, vrtOutPath)
progress.setText('Download complete!')
time.sleep(2)
