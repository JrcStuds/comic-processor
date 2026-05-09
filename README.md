## Comic Processor

# Description

This tool is used to convert a collection of cbz files that make up a trade and turn them into individual issue cbz files.

# How To Use

1. Place the cbz files that make up the trade into the trades directory.
2. Within the config.json file, describe how the trade is made up.
    - "default_name" is the main name of the comic in the trade, typically the run.
    - "page_count" is the default number of pages that a comic will have (excluding the cover image).
    - "intro" is the amount of pages in the cbz file before the cover of the first comic (e.g. table of contents, etc.).
    - "trades" is a list of the indexes of the trade cbz files within the trades directory. This is for specifying which specific cbz files go in which order if more than one trade's cbz files are in the directory.
    - "issues" is the list (in order) of issues in the trade. Integer values will use the default_name string in their title, while other titles may be specified with a string.
    - "special_page_counts" is for when an issue has a non-standard number of pages, to specify this deviation, the key-value pair would be the name of the issue (as per the "issues" list, or by the integer value) and the number of pages (as an integer).
    - "buffer_pages" is a list of the issues with a buffer page between the cover image and the first page. These issues are specified with their integer or string issue name.
3. Run main.py, and the resulting cbz files will be generated into the output directory.