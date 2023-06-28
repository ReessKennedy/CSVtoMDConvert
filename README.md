# CSVtoMDConvertor

## What ⚡
A simple script to convert Raindrop backup .csv files to markdown files that can then be searched easily inside a markdown-based, plain file notes app like Obsidian, Logseq, iA Writer or many others. 

## Why 🤷‍♂️
It's great to be able to search all your bookmarks inside your notes tool. 

## How 📋
### 1] Get your backup file
In Raindrop, just go to your settings and then click on backups and download your backup as a CSV file. 

### 2] Run
-Place your file in the folder of this repository and name it "RDBackup.csv"
-Open your terminal and type in `cd` and then drag in the repo to get the path and then click enter so you're working inside this file. 
-In the terminal, simply type `python CSVtoMD.py` and click enter!
-Relocate the files that this command generates to your markdown notes app. 

## Notes

### Search tips
Put all your markdown files in a dedicated bookmarks folders. This allows you to filter them out of search if you wish. 

If Obsidian, to achieve this, just add something like `path:-/bookmarks/` after you search term where the minus symbol just means "do not include this" and then you include the folder path. 

### Sample output

### File grouping
The script groups bookmarks into yearly files. If you capture a huge number of bookmarks you may need to split these up even further but this organization will be good for 95% of users, I suspect. 

### Headers
Files are outputted with headers as markdown h2 elements. If your notes app outlines a doc based on header elements then this provides a nice navigation element. 
