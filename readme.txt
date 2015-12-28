Had some time to work on this over the holiday weekend and thought I would share the joy of converting xmarks to evernotes

Export xmarks bookmarks to an HTML file and download to a local drive. (If you don't know how to do this, this might be a bit complex for you)
Download the python script (.py) in this repo.
Make sure that you have python and pip installed
pip install selenium

Edit the python script to use the filename of your xmarks bookmark file.
Login to evernote and set your default notebook to where you want ALL of your xmarks to go. I suggest a new notebook.
Run the script. You might change the sleep time – when I tried less than 20 seconds, there was a problem, but it might work for you.

The script will check all of the URL's to be sure that they have not moved and if they have it will print the URL for you so that you can check the bookmark and manually save them later – or perhaps edit your bookmark file and re-run the script. All good bookmarks are saved into your default folder in Evernote.

This program is released as open source without warranty of any kind.
