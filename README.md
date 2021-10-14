
# User Information Utility CLI

A simple python3.x utility script that returns the basic user information
inside a system in either JSON or csv form to a file-like object (default stdout)

## Usage:

**hr --path path/to/file.txt** Outputs contents into file.txt.
**hr --format json/csv**       Outputs contents in corresponding format.


### Example Output

user@host: $hr

'''json
[
    {
        "name": "username",
        "id": 1000,
        "home": "/home/username",
        "shell": "/usr/bin/bash"
    }
]
'''


