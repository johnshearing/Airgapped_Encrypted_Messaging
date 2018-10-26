## Airgapped GPG Encrypted Messaging using QR-Coded Video 
This help file is not complete.  
It is under construction.  

Works on Raspberry Pi and other linux devices.  

Text files are encrypted and then passed across the airgap as a parade of QR-Codes displayed on the touch screen.  
Should work with any kind of file but to date have only tested with text files.  

Requires that OpenCV 3 be installed.   
Instructions for installing OpenCV 3 can be found at the link below:  
[Raspberry_Pi_2_and_OpenCV_3_Tutorial_Part_1/Raspberry Pi 2 + OpenCV 3 Cheat Sheet.txt](https://github.com/johnshearing/Raspberry_Pi_2_and_OpenCV_3_Tutorial_Part_1/blob/master/Raspberry%20Pi%202%20%2B%20OpenCV%203%20Cheat%20Sheet.txt)  

The companion video can be found here.  
[Raspberry Pi 2 and OpenCV 3 Tutorial Part 1](https://www.youtube.com/watch?v=6j-Wy9j0TCs)  
There is no part 2 in case you are wondering but I followed the instructions and was rewarded with a successful install of OpenCV 3 and the ability to read QR-Codes from a video and turn it back into a text file.  

To use this code, just clone the repository into a directory which is included in your path variable.  
Then grant executible permissions to all the scripts.  

Then open a terminal window and type `menu`.  
This starts the PrivateKeyVault application which provides you with a full menu of services provided with the device.  

