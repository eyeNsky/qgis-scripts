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
