##[TBT-Tools]=group
##Input_Footprints=vector
##Output_Curl_List= file 

import os,sys
outList = Output_Curl_List

if len(outList) == 0:
    outDir = os.environ['HOME']
    outList = os.path.join(outDir,'curl.list')
from qgis.utils import *
# Get  vector from canvas, must be loaded with features selected.
layer = processing.getObject(Input_Footprints)
selected = layer.selectedFeatures()
numImages = len(selected)

progress.setText('Adding %s images to %s'%(numImages,outList))
if numImages == 0:
    progress.setText( 'No images selected for download!' )
    progress.setText('Please select some images and try again!')
else:
    out = open(outList,'w')
    for sf in selected:
        imgName = sf.attribute('url')
        thisTif = str(imgName)
        thisVrt = imgName.replace('.tif','.vrt')
        progress.setText('Adding: %s '%imgName)
        outTxt = 'url=%s\n-O\nurl=%s\n-O\n' %(thisTif,thisVrt)
        out.write(outTxt)
    out.close()
    progress.setText('List complete!')
    cmdTxt = 'You can now execute "curl -K %s" to download the files' % outList
    progress.setText(cmdTxt)
time.sleep(5)