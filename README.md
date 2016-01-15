# delicious2firefox

Simple script to export bookmarks from `ybookmarks.sqlite` (used by the now discontinued [delicious Firefox add-on](https://addons.mozilla.org/en-US/firefox/addon/delicious-bookmarks/) to a html file in the [Netscape bookmark file format](https://msdn.microsoft.com/en-us/library/aa753582%28v=vs.85%29.aspx). 

The script is based on Qiangning Hong's [**RescueDelicious**](https://pypi.python.org/pypi/RescueDelicious). Thank you for your great work!

This is literally my first Python script. I hope it may still be of use to someone.

## Usage

    d2f.py <your-ybookmarks.sqlite-file>

This will create a file called `fbm.html`, containing all your bookmarks in the Netscape bookmark file format.
This file can be [imported to Firefox](https://support.mozilla.org/en-US/kb/import-bookmarks-html-file).

### Tag to Folder Conversion
Tags used in delicious are converted to folders in the html file.
Note, that as a result any bookmarks previously containing more than one tag will be duplicated in the newly created `fbm.html`.

### ybookmarks.sqlite
The `ybookmarks.sqlite` file is located in your Firefox [profile folder](https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data).

###  Motivation

I have long intended to migrate from delicious to Firefox' built-in bookmarks-management.
When the day came I could not find a working solution to export my bookmarks from the delicious.com website.

Looking for alternatives I stumbled upon the `ybookmarks.sqlite` file, which is a local copy of your delicious bookmarks saved by the no longer maintained [delicious Firefox add-on](https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data).

Luckily Qiangning Hong had already developed [**RescueDelicious**](https://pypi.python.org/pypi/RescueDelicious) which offered a convenient way of extracting the data from the sqlite file. I modified his script to create a html-file that can be imported into Firefox (or any other browser supporting the [Netscape bookmark file format](https://msdn.microsoft.com/en-us/library/aa753582%28v=vs.85%29.aspx)).

## License

[MIT](https://opensource.org/licenses/MIT)
