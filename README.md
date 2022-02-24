# FantasyFootballV2
 Predictive modeling of Fantasy Football players

This is an ongoing project to play around with fantasy football player data and generate a predictive model for yearly stats.

My current data source is FantasyPros github yearly spreadsheets: https://github.com/fantasydatapros/data

INITIAL COMMIT UPDATE 2/23/22:
Right now all I have for V2 is all the player as json files with makePlayers.py, but I'll be implementing a K Nearest Neighbors model soon.

V1 (yes, it's messy):
I worked on V1 this summer, which was kind of a mess. I tried using the ESPN Fantasy API in espn.py, which was too undocumented to use. I was able to load player data from spreadsheets, make a k nearest neighbors model, and graph it's accuracy, sensitivity and specitivity for different k values. The model only got ~52% accuracy, ~60% sensitivity, and ~40% specitivity predicting whether or not a player would hit their season projection, which was dissapointing. The dataset I was working with however, wasn't very good, and I was using too much of a "meat grinder" modeling approach (not to mention the obnoxiously under-commented, messy code), so I'm starting over with V2 and a better dataset! V1 is included on this repo for reference (although not the old dataset), but it was a working project not intended to be published on github as anything polished or usable.