# SSOCR (only for linux)

## What does it do?

**When the program is setup and running,**
**Use this shortcut -> Meta (the windows key) + Shift + P**

**You should enter an area grab screenshot mode ( like snip tool on windows ).**
**Go ahead and grab an area to screenshot.**

**Any text that's in that area should now be copied for you to paste!**
**Use this to quickly copy text that's in images or unselectable.**

![Gif Demo](https://imgur.com/a/Ue8le69.gif)

## How to setup

**You need 4 things installed,**
- **python**
- **python-pip**
- **tesseract**
- **python-virtualenv**

**On Arch, You can install them like so,**
```
sudo pacman -S python python-pip tesseract python-virtualenv
```

**If you're not on arch, just use whatever package manager your distro provides**

**After that clone the repo or just download the code as zip and extract it.**

**There should be a Code > Download ZIP button in green on the top right.**

**Open the project folder in your terminal and make sure the scripts have permission to run,**
```
chmod +x start.sh
chmod +x build.sh
```

**Now just start the program by**
```
./start.sh
```

**And we're done! enjoy : )**

**(You can also include the start script in autostart apps so you never have to think about it again)**