# bat-json-polyglot

python script to generate batch/json polyglots!

the new file looks something like this, shown with json syntax highlighting:
```json
{"\" > nul 2> nul & echo hello, world & ::": 1,
    "\" > nul 2> nul & echo this seems to work & ::": 1,
    "857\" > nul 2> nul & exit & ::": 1,
    "test json data": [1,2,3],
    "good": "yes",
    "number": 56
}
```

same code block, but with batch syntax highlighting:
```batch
{"\" > nul 2> nul & echo hello, world & ::": 1,
    "\" > nul 2> nul & echo this seems to work & ::": 1,
    "857\" > nul 2> nul & exit & ::": 1,
    "test json data": [1,2,3],
    "good": "yes",
    "number": 56
}
```


usage: `python bat-json-polyglot.py <batch file> <json file> <output path>`
