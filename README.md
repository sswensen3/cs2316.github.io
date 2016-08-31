# python-data

Jekyll source for website containing course materials for Python Data Manipulation course

# Slides

Slides are written in Markdown and converted to Reveal.js HTML using [Pandoc](http://pandoc.org/) to  [produce the slides](http://pandoc.org/README.html#producing-slide-shows-with-pandoc)

```sh
$ cd slides
$ pandoc -s --mathjax -t revealjs -V theme=gt -V "slideNumber='c/t'" -V progress=true -o intro-python.html intro-python.md

```

To generate all the slides:

```sh
for file in `ls *.md`; do pandoc -s --mathjax -t revealjs -V theme=gt -V "slideNumber='c/t'" -V progress=true -o $(basename $file .md).html $file; done
```
