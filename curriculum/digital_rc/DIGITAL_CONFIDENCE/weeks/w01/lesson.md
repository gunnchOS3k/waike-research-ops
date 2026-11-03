# Week 1: Folders and paths — knowing where a file really lives

Help card DCO-3101: Ana saved a summer photo and the file dialog now says 'not found'. Every file has an address called a path, written from the top of the drive down through folders, like /home/ana/Documents/photos/summer.jpg. That full form is an absolute path because it starts at the root, the single slash. Programs also accept relative paths that start from wherever you are standing, called the current working directory. Two dots mean the folder above, and a single dot means here. Standing in /home/ana/Documents/letters, the relative path ../photos/2026/../summer.jpg climbs out of letters into Documents, steps into photos and into 2026, then climbs back out of 2026, landing on /home/ana/Documents/photos/summer.jpg. Walk it with your finger on a drawn tree before trusting it. Windows writes C:\Users\Ana\Documents with backslashes and a drive letter, but the idea of climbing and descending is the same. When a file goes missing, ask two questions out loud: where am I standing, and which way does the path walk from here.

## Worked example

cwd /home/ana/Documents/letters + ../photos/2026/../summer.jpg → /home/ana/Documents/photos/summer.jpg
