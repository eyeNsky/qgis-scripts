# qgis-scripts
Collection of scripts for the processing toolbox in QGIS. Loads into Scripts/TBT-Tools. Use either the load script funtion in the toolbox or drop the script into ~/.qgis/processing/scripts.
# image-downloader
Load a vector that has a field 'url', select some features and launch the script. The script will download the selected images and the associated vrt file.
# image-curl-list
Load a vector that has a field 'url', select some features and launch the script. The script will add the selected images and the associated vrt file to a 'curl.list' file. Use with "curl -K curl.list".
# image-wget-list
Load a vector that has a field 'url', select some features and launch the script. The script will add the selected images and the associated vrt file to a 'wget.list' file. Use with "wget -i wget.list". You can also check if the images exist with:
<pre><code>wget --outputfile=spider.txt --spider -i wget.list
grep broken spider.txt</pre></code>
# select-key-frames
Load vector of image footprints that have high overlap (say ones that were collected for SfM). The code will select key frames to mosaic based on an overlap threshold. Images that overlap the existing set of footprints by more than the threshold will be skipped. Frames that are not skipped are appended to the existing set.
# export-selected-frame-ids
After selecting key frames, run this to export the image names (+.jpg) to 'image.list' in the directory of your choosing. Defaults to $HOME
