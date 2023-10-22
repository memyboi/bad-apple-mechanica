# bad-apple-mechanica
playing bad apple in mechanica (made for linux - may not work with windows)

# linux instructions:
1. install roblox (preferrably through [vinegar](https://devforum.roblox.com/t/vinegar-the-better-way-to-run-roblox-on-linux/2224394))
2. clone this repo with `git clone`
3. download python (if you haven't already) preferrably from ur package manager (eg. apt, pacman, zyppr)
4. go through the depends.txt file and download each dependancy with `pip install` (some might be uninstallable cuz u alr have it)
5. read oop-depends.txt (out of pip dependancies) and download pygobject (so it can screenshot)
6. run `init.py` to create the frames in the ffmpegd folder (yes ik it doesn't use ffmpeg, it cba to change it now)
7. prep everything in roblox by making a 32x24 default colour platform in mechanica, saving it to slot 2, changing it completely to black (0, 0, 0) and saving it to slot 3
8. prep the camera to look down as much as possible and to be perfectly straight
9. open a terminal (eg. Konsole), pin it to the top of the screen, and run `run.py`
10. go afk until it finishes rendering
11. run `compiledRendered.py` to turn all the screenshots into a video (at 30fps)
12. your final result should be as a file called `project.mp4`

# windows instructions:
you could probably do this with wsl2, but as of now unsupported
screenshots might not work

#macos instructions:
good luck lmao
(just try to copy linux instructions - mac os is pretty similar to linux as they're based on unix)
screenshots might not work
