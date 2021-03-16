# Apache Petri

[Apache Petri](https://petri.apache.org/)

This repository provides the website and source code for Apache Petri.

- [info.yaml](content/info.yaml) -- Machine Readable Culture Status
- [petri.rdf](content/petri.rdf) -- Machine Readable [Project DOAP](https://projects.apache.org/project.html?petri)
- [Pages](content/pages) -- website pages in GitHub Markdown
- [Issues](https://github.com/apache/petri-site/issues) -- tracker

The website is built with [Pelican](https://blog.getpelican.com).
CI/CD is via a [.asf.yaml file](https://cwiki.apache.org/confluence/display/INFRA/Git+-+.asf.yaml+features).

- [Template](theme/apache/templates) -- simple html template
- [CSS](theme/apache/static/css) -- simple additional framework
- [Images](content/images) -- logo and other images
- [Pelican Configuration](pelicanconf.py) -- pelican configuration
- [ASF YAML build](.asf.yaml) -- ASF infrastructure instructions

JavaScript frameworks available are:

- [JQuery 3.3.1 Slim](https://code.jquery.com/jquery-3.3.1.slim.js)
- [Popper 1.14.7](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.js)
- [Bootstrap 4.3.1](https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.js)

CSS frameworks available are:

- [Bootstrap 4.3.1](https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.css)
- [GitHub Markdown 3.0.1](https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/3.0.1/github-markdown.css)

Additional testing with GitHub Actions:

- [markdownlint](https://github.com/DavidAnson/markdownlint) -- using [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) - Node.js style checker and lint tool for Markdown/CommonMark files
- [misspell](https://github.com/client9/misspell) -- Golang library to correct commonly misspelled English words quickly
- [yamllint](https://yamllint.readthedocs.io/en/stable/) -- a linter for YAML files
