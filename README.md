# Rickroll
Convert links to [Rick Rolls](https://www.youtube.com/watch?v=dQw4w9WgXcQ).

## Usage
```console
$ cat ./samples/sample.md
[Google](google.com)
[YouTube](youtube.com)
[Github](github.com)

$ ./rickroll.py ./samples/sample.md

$ cat ./samples/sample.md
[Google](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
[YouTube](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
[Github](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
```

## Supported Filetypes
- Markdown (`.md`)
- Html (`.html`)

[PRs](https://github.com/shoumodip/rickroll/compare) are welcome
