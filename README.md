# delicious2firefox
## Synopsis

This very simple script exports bookmarks saved in the sqlite database file ("ybookmarks.sql") used by the delicious Firefox add-on to the Netscape Bookmark File Format https://msdn.microsoft.com/en-us/library/aa753582%28v=vs.85%29.aspx. 

The script is based on Qiangning Hong's **RescueDelicious**. Thank you for your great work!

## Usage

    d2f.py <your-ybookmarks.sql-file>

This will create a file called "fbm.html", containing all your bookmarks in the Netscape Bookmark File Format.
This file can be imported to Firefox as described here: https://support.mozilla.org/en-US/kb/import-bookmarks-html-file.

## Motivation

Wanting to migrate from delicious to Firefox' built-in bookmarks-management, I did not find a working or satisfying way to export my bookmarks from delicious.

## Installation

Provide code examples and explanations of how to get the project.

## API Reference

Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

## License

MIT
