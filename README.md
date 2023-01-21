# Youtube bulk downloader and audio extractor # 

## Python package to install to use this ##
pip install  youtube_dl  or 
pip3 install  youtube_dl (if pip3 is used for python3)


## Description ## 
Bulk Downloads from youtube, extracts only audio and copies to a folder(e.g. USB pen drive folder)

- Save the youtube urls in a file 
- give the file as params in below command
- last param in below command is folder where audio files (extracted from from youtube urls inside file above) will be copied. I used USB folder (for mac its under /Volumes/your_usbname) 

## Usage : ## 
python downloader.py  _**fileContainingListOfYouTubeUrls**_   _**OutputFolderWhereFilesWillBeCopied**_ 

## Future improvements ## 
Use threads instead of sequentially downloading file.

Happy listening  :+1:
