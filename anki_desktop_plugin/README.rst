Anki Desktop Plugin
===================

You should copy this directory into your 'addons21' folder in your Anki data directory. This is ~/.local/share/Anki2/ on Ubuntu Linux, you'll need to look for this on other platforms and copy there.

In theory, the ID could clash with something from Ankiweb, but the plugin corresponding to the one included here has been removed. I am assuming the Ids don't get reused, and that is a reasonable assumption in my view!

If your anki-sync-server is not on localhost or you are not exposing via port 27701 then you will need to change these after copying. You will need to restart Anki Desktop for the changes to take effect

TODOs:
- turn both the host and port into config options
