README  
Hack & Hustle Academy Sampler  
Authored by Gurtej Singh  
Created on July 7, 2017  
Python Version 3.6  

#### INSTALLATION

sudo add-apt-repository ppa:fkrull/deadsnakes  
sudo apt-get update  
sudo apt-get install python3.6  
sudo apt-get install python3-pip  
sudo python3.6 -m pip install --upgrade pip  
sudo python3.6 -m pip install pygame --user  

#### CONFIGURATION

Specific sound kit information found in config.json.  
Roland TR-808 sound kit by Michael Fischer included.  
By default, some 808 sounds used from samples/rolandTR808,but more samples included in samples/originalRolandTR808 for customization options.  
Add new sound kit as dictionary in json under "soundKits".  
Add subfolder to samples folder in directory with sounds to include.  
Then add new root path and key input mappings to config.json.  

#### OPERATING INSTRUCTIONS

Navigate to hackhustlesampler folder, then execute program in terminal:  
python3.6 hackhustlesampler.py  
Keep the black window in focus while operating the program.  
Tap on keyboard to trigger sounds.  
Press ESC or the (x) button on the window to exit program.  

#### CURRENT FEATURES

Support for multiple sound kits.  
Support for multiple sounds played simultaneously with a single key press.  
Sound file name displayed in console when triggered.  
Each sample will not overlap audio with itself when triggered more than once.  

#### ABOUT

This code is meant to be relatively simple and used for educational purposes. Students brand new to programming will work to build a similar sampler of their own in increments.

The Hack & Hustle Social Entrepreneurship Academy is a workforce development program created through an equal partnership between Jecha Networks, Informative Technologies, and Hip Hop University. Hack & Hustle will increase economic mobility for underserved youth by placing scholars in technology training while providing them with face-to-face mentorship. These scholars will be coding with in-demand programming languages such as Python, bringing further value to computers once viewed as eWaste while learning skills beneficial to them in the modern economy.

#### CONTACT

Gurtej Singh  
Technology Director of Hip Hop University  
gurtejsingh(dot)com  
tech4hiphopuniversity(at)gmail(dot)com  
hackhustleacademy(at)gmail(dot)com  


