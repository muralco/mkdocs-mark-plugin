# MkDocs MarkLinks Plugin

A mkdocs plugin to support links in confluence style.

When pushing markdown to Confluence using https://github.com/kovetskiy/mark, links 
to other confluence pages have to be in one of these formats:

```
[Destination Title](ac:)
[Some Text](ac:Destination Title)
```

Obviously mkdocs has no idea how to do that, so this mkdocs plugin replaces
those link targets with reasonable links to markdown docs, so we can keep
producing mkdocs even when pushing docs to confluence.

