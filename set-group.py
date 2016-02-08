##[Mosaic-Tools]=group
##Input_Footprints=vector


import os,urllib
from sqlite3 import dbapi2 as db

from qgis.utils import *
# Get  vector from canvas, must be loaded with features selected.
layer = processing.getObject(Input_Footprints)
selected = layer.selectedFeatures()
numImages = len(selected)
if numImages == 0:
    print 'No images selected for mosaic group!'
theDb = (Input_Footprints)
conn = db.connect(theDb)
cur = conn.cursor()
cur.execute("""select MAX(grp) from fp""")
maxGrp = cur.fetchone()[0]
if maxGrp == None:
    maxGrp = 0
nextGrp = int(maxGrp) + 1
for sf in selected:
    imgName = sf.attribute('imageid')
    cur.execute("""update fp set grp = ? where imageid = ?""",(nextGrp,imgName))
    #progress.setText('Setting group for: %s '%imgName)
conn.commit()
conn.close()
time.sleep(2)