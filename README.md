# Youtube bulk downloader and audio extractor # 

## Description ## 
Bulk Downloads from youtube, extracts only audio and copies to a folder(e.g. USB pen drive folder)

- Save the youtube urls in a file 
- give the file as params in below command
- last param in below command is folder where audio files (extracted from from youtube urls inside file above) will be copied. I used USB folder (for mac its under /Volumes/your_usbname) 

## Usage : ## 
python downloader.py files_containing_list_of_YouTube_urls output_folder_where_files_will_be_copied

## Future improvements ## 
Use threads instead of sequentially downloading file.
