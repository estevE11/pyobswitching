# PyOBSwitching
This project is inspired by [OBSwitching](https://github.com/pagoru/OBSwitching) by [pagoru](https://github.com/pagoru)

This is a simple plugin for OBS that switches to the scene containing the monitor your cursor is in.

This was created for personal use, but feel free to use it yourself!

## Usage
In order for **PyOBSwitching** to work, you need to bind a key combo to "Change scence" for each scene containing a screen. It must be a key combo strange enough so that you dont press it unintencionally.

Examples:
 - Screen 1: CTRL + ALT + SHIFT + P
 - Screen 2: CTRL + ALT + SHIFT + O

***Beware that all the keys exept for the last one must be exactly the same for all binds.***
 
 ### Running the script
 `python pyobswitching.py [keys for each monitor] [shared bind]`

Example: `python pyobswitching.py p o ctrl alt shift`
`p o` --> keys for each monitor
`ctrl alt shift` --> shared bind

***Beware that you'll need to input  as many keys as  monitors you have connectet  even if you don't use them in OBS***