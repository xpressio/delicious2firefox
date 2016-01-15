# delicious2firefox
## Synopsis

Simple script that can be used to export bookmarks from the sqlite database file used by the now discontinued [delicious Firefox add-on](https://addons.mozilla.org/en-US/firefox/addon/delicious-bookmarks/) to a html file in the [Netscape Bookmark File Format](https://msdn.microsoft.com/en-us/library/aa753582%28v=vs.85%29.aspx). 

The script is based on Qiangning Hong's [**RescueDelicious**](https://pypi.python.org/pypi/RescueDelicious). Thank you for your great work!

## Usage

    d2f.py <your-ybookmarks.sql-file>

This will create a file called "fbm.html", containing all your bookmarks in the Netscape Bookmark File Format.
This file can be imported to Firefox as described here: https://support.mozilla.org/en-US/kb/import-bookmarks-html-file.

## Tag to Folder Conversion
Tags used in delicious are converted to folders in the html file.
Note, that any bookmark that previously contained more than one tag will be duplicated in the 

## Motivation

Wanting to migrate from delicious to Firefox' built-in bookmarks-management, I did not find working solution to export my bookmarks from the delicious.com website.

## License

[MIT](https://opensource.org/licenses/MIT)
