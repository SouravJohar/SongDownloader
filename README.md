# YouTubeScraper
a simple webscraping code developed in java using jsoup and ui4j libraries to download something in youtube and convert it into high quality audio format(mp3). It can be used as a song downloader.

## Requirements
- System requirements  
    - Ubuntu  
        `apt-get install qt5-default libqt5webkit5-dev build-essential python-lxml       python-pip xvfb` 
    - Arch Linux  
        `pacman -S qt5-base qt5-webkit base-devel python2-pip xorg-server-xvfb jre8-openjdk`  
        Arch defaults to python3, so be careful to use the python2 versions of pip (pip2) and the other libraries.
- python
    `pip install -r requirements.txt`

- Java Based Requirements: Install .jar file for each package and put it in the same directory as the file otherwise use IDE for the same.

    1. Java 1.8

    2. Jsoup library

    3. UI4J Library


## Future Plans:

- Fetch album art and add it to the downloaded mp3 file(using id3 editing libraries)

- Add Album name, artist name, etc...(using id3 editors)
