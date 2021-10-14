
# User Information Utility CLI

</p>A simple python3.x utility script that returns the basic user information
inside a system in either JSON or csv form to a file-like object (default stdout). It takes two optional --format and --path. Any user with user_id over 1000 is considered valid and returned.</p>

## Usage:

**hr --path path/to/file.txt**  <p> Outputs contents into file.txt.</p>
**hr --format [json,csv]**        <p> utputs contents in corresponding format.</p>

### Example Output

<p>user@host: $hr</p>

```json
[
    {
        "name": "username",
        "id": 1000,
        "home": "/home/username",
        "shell": "/usr/bin/bash"
    }
]
```


