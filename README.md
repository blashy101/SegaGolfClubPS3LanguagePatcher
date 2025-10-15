# SegaGolfClubPS3LanguagePatcher

Hello, so, this game (Miyazato San Kyoudai Naizou: Sega Golf Club BLJM-60007) has unused localization files for 5 different languages, so I wrote up this quick little Python script so you can switch the languages around for your preferred language. There are some caveats though, accent marks are not supported by the font, and in the text files, they're replaced with ASCII "?", so I guess an effort could be made later down the line to update the font/text files but that's a little out of the scope of what I'm willing to do. Drop this script into your Game Disc/"JB Folder" copy of your game in the PS3_GAME\USRDIR\MEDIA and run:

python SegaGolfClubPatcher.py and just follow the on-screen prompts, it's really simple. (Requires Python 3.6+) If you intend to copy the modification over to your PS3, the only two directories altered by this script are "TEXT" and "SPRITE", so just copy those folders from your PC to PS3, or run in RPCS3 if you want. You know what to do. This doesn't touch the EBOOT and there is like maybe 2% text still in Japanese but it's incredibly insignificant. 

It's worth noting that being unused localization files, they aren't exactly super excellent perfect translations or really nice UI/menu elements so, it could be improved later as well but, again, little out of the scope of how much effort I'm willing to put into a golf game from 2006. 

Enjoy, please open an issue if something goes horribly wrong, I only tested the English files for more than 2-3 mins vs other languages.
