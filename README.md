# Mkdocs doxygen snippets plugin

### Based on  [matusnovak/doxybook](https://matusnovak.github.io/doxybook)

This python tool is extension for MkDocs. Extension will take your programme source code and runs Doxygen.
Than converts exported XML into markdown and create new folder with full generated documentation. 
Next usage is by snippets inside documentation markdown.

## Example usage

1.  Generate class with name `rb::MotorChangeBuilder` 
```yaml
::: doxy.Class
    name: rb::MotorChangeBuilder
```

2. Generate method `brake (MotorId id, uint16_t brakingPower)` from class with name `rb::MotorChangeBuilderA`
```yaml
::: doxy.Class.Method
    name: rb::MotorChangeBuilder
    method: brake (MotorId id, uint16_t brakingPower)
```

3. Generate function with name `readUltra (bool async)` 
```yaml
::: doxy.Function
    name: readUltra (bool async)
```

4. Generate code snippet from file `RBCXLeds.cpp` 
```yaml
::: doxy.Code
    file: RBCXLeds.cpp
    start: 21
    end: 35
```

![Basic-implementation](docs/media/Basic-implementation.png)

<!-- ## Live Demo

See live demo here for [Gitbook here](https://matusnovak.github.io/doxybook/gitbook/api/classexample_1_1Animal.html), [Vuepress here](https://matusnovak.github.io/doxybook/vuepress/api/classexample_1_1Animal.html), [MkDocs here](https://matusnovak.github.io/doxybook/mkdocs/api/classexample_1_1Animal), or [Original here](https://matusnovak.github.io/doxybook/original/classexample_1_1Animal.html). -->

## Requirements

### Apt
- python 3.6 or newer -> `sudo apt install python3` 
- Pip -> `sudo apt install python3-pip`
- Git -> `sudo apt install git`
- Doxygen -> `sudo apt install doxygen`

### Pip
- Jinja2 -> `pip install jinja2`
- Mkdocs -> `pip install mkdocs`
- ruamel.yaml -> `pip install ruamel.yaml`

### Optional:
- mkdocs-material -> `pip install mkdocs-material`


## Installation

**Install using Python Pip: <https://pypi.org/project/mkdocs-doxygen-snippets-plugin/>**

```bash
pip install mkdocs-doxygen-snippets-plugin
or
pip3 install mkdocs-doxygen-snippets-plugin
```

**Or Install manually:**

```
git clone https://github.com/JakubAndrysek/mkdocs-doxygen-snippets-plugin.git
cd doxybook
sudo python setup.py install
```


<!-- ## Compile the example

See the live demo [here](https://matusnovak.github.io/doxybook) or alternatively you can run the examples in the following way:

```bash
# Clone this repository
git clone https://github.com/matusnovak/doxybook.git

# Go to the example folder
cd doxybook/example

# Run doxygen and generate xml folder
doxygen Doxyfile

# Convert xml to md for Vuepress
doxybook -i temp/xml -o vuepress/api -t vuepress
# Note! GitBook requires SUMMARY.md as the following:
# doxybook -i temp/xml -o gitbook/api -t gitbook -s gitbook/SUMMARY.md

# Run vuepress in dev mode
cd vuepress
vuepress dev

# Open http://localhost:8080
``` -->

## What files are generated?

This tool was designed to copy the file naming and structure of Doxygen html output. The naming of the files is identical except tiny changes with Class/Variable/enumeration Index pages.

All classes, namespaces, structures, and interfaces are generated, including the following additional files:

* Directories (e.g. `dir_....md`)
* Files with source code + file documentation (e.g. `filename_8h.md`)
* Markdown pages processed through doxygen, highly do not recommend using this! (e.g. `md_src_....md`)
* Members (e.g. `class_xxx_yyy.md` or `namespace_xxx_yyy.md`)
* Class List (e.g. `annotated.md`)
* Class Index (e.g. `classes.md`)
* Class Members (e.g. `class_members.md`, `class_member_enums.md`, `class_member_functions.md`, `class_member_typedefs.md`, `class_member_variables.md`)
* Class Hierarchy (.e.g `hierarchy.md`)
* Namespace List (e.g. `namespaces.md`)
* Namespace Members (e.g. `namespace_members.md`, `namespace_member_enums.md`, `namespace_member_functions.md`, `namespace_member_typedefs.md`, `namespace_member_variables.md`)
* Modules/groups (e.g. `modules.md`)
* Index page (if exists within Doxygen output as `indexpage.xml`) (e.g. `index.md`)
* Any additional pages generated by Doxygen such as bugs, todo, tests

See the example folder to see all files.

<!-- ## Usage

```
> python -m doxybook -h
usage: __main__.py [-h] [-t TARGET] -i INPUT -o OUTPUT [-s SUMMARY]
                   [-l LINK_PREFIX] [-d DEBUG] [--hints HINTS]
                   [--ignoreerrors IGNOREERRORS]

Convert doxygen XML output into GitBook or Vuepress markdown output.

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Select the target: Gitbook (default), Docsify, MkDocs,
                        or Vuepress, for example: "-t vuepress", "-t docsify",
                        "-t mkdocs", or "-t gitbook"
  -i INPUT, --input INPUT
                        Path to doxygen generated xml folder
  -o OUTPUT, --output OUTPUT
                        Path to the destination folder
  -s SUMMARY, --summary SUMMARY
                        Path to the summary file which contains a link to
                        index.md in the folder pointed by --input (default:
                        false)
  -l LINK_PREFIX, --link-prefix LINK_PREFIX
                        Adds a prefix to all links. You can use this to
                        specify an absolute path if necessary. Docsify might
                        need this. (default: "")
  -d DEBUG, --debug DEBUG
                        Debug the class hierarchy (default: false)
  --hints HINTS         (Vuepress only) If set to true, hints will be
                        generated for the sections note, bug, and a warning
                        (default: true)
  --ignoreerrors IGNOREERRORS
                        If set to true, will continue to generate Markdown
                        files even if an error has been detected (default:
                        false)
``` -->

<!-- ## Detailed usage Vuepress

1. First, create your Doxyfile. I am not going to tell you how, there are plenty of tutorials out there.
2. Set `GENERATE_XML = YES` and `XML_OUTPUT = xml` in the Doxyfile, and don't forget about `OUTPUT_DIRECTORY = temp` (or any other directory).
3. Run the doxygen via `doxygen Doxyfile` 
4. Create your initial Vuepress configuration (optional).
5. Run doxybook as: `doxybook -i temp/xml -o docs/api -t vuepress` (paths are relative).
6. Then run `vuepress dev` and go to `http://localhost:8080`.

## Detailed usage Docsify or MkDocs

Same as VuePress, except use `-t docsify` or `-t mkdocs` when running doxybook.

## Detailed usage Gitbook

1. First, create your Doxyfile. I am not going to tell you how, there are plenty of tutorials out there.
2. Set `GENERATE_XML = YES` and `XML_OUTPUT = xml` in the Doxyfile, and don't forget about `OUTPUT_DIRECTORY = temp`.
3. Run the doxygen via `doxygen Doxyfile` 
4. Create your initial GitBook.
6. Create an empty folder where the markdown files should be generated. For the purpose of this example, we will put it in the `docs/api` folder. 
5. (optional) In your `SUMMARY.md` create a link to the `docs/api/index.md` with any text, for example: `* [Lorem Ipsum](docs/api/index.md)`. This file can be any kind of markdown file. However, the file `index.md` needs to be inside the folder where the markdown files are going to be generated. Doxybook will find this link and will generated a **sub-list** below that markdown link. Anything you have written after the `* [Lorem Ipsum](docs/api/index.md)` will not be affected, only the sub-list items. Note that if you put any list item or sub-lists of `* [Lorem Ipsum](docs/api/index.md)` they will be REMOVED!
6. Run doxybook as: `doxybook -i temp/xml -o docs/api -s SUMMARY.md -t gitbook` (paths are relative) The `-s SUMMARY.md` is optional, if you provide a vaid path to the SUMMARY.md file then the doxybook will alter the contents with links to generated markdown files.
7. Then build your GitBook as: `gitbook build`, or serve it as `gitbook serve` and go to `http://localhost:4000`, or upload the contents of `_book` folder into gh-pages on GitHub. -->

<!-- ## Having errors while generating markdown files?

Run doxybook as `doxybook --ignoreerrors true -i ... -o ... -t ...`. The files will be generated, but some things may be missing. -->

<!-- ## How does the SUMMARY.md work here? (Gitbook only)

GitBook has a big fault that anything not listed in `SUMMARY.md` will get ignored. Therefore the doxybook needs to alter the `SUMMARY.md`. Yes, this is optional, in case GitBook will be fixed in the future. 

For example, given this summary file:

```
# Summary

* [Introduction](README.md)
* [Documentation](docs/api/index.md)
  * [This will get deleted](whatever.md)
* [Something else](something-else.md)
* [Go to my website](http://mywebsite.com/)
```

After running doxybook, the summary will become this code below. Notice how `* [This will get deleted](whatever.md)` has vanished. The doxybook will only modify anything that is a child item of `* [Documentation](docs/api/index.md)` regardless of the indentation. Also, you do not need to remove any generated links to `docs/api` (or whatever folder you have used) as it will be sraped in any re-run of the doxybook and generated from scratch. -->

<!-- ```
# Summary

* [Introduction](README.md)
* [Documentation](api/index.md)
  * [Related Pages](api/pages.md)
    ... etc
  * [Modules](api/modules.md)
    * [Some organism example](api/group__organism.md)
      * [An animal group example](api/group__animals.md)
  * [Class List](api/annotated.md)
    * [namespace example](api/namespaceexample.md)
      * [class example::Animal](api/classexample_1_1_animal.md)
        ... etc
  * [Namespace List](api/namespaces.md)
  ... etc
* [Something else](something-else.md)
* [Go to my website](http://mywebsite.com/)
``` -->

<!-- ## Found a bug or want to request a feature?

[Feel free to do it on GitHub issues](https://github.com/matusnovak/doxybook/issues)

## Pull requests

[Pull requests are welcome](https://github.com/matusnovak/doxybook/pulls)

## Contact

Use GitHub issues or contact me through my email (see my GitHub profile page). -->

## License

```
MIT License

Copyright (c) 2021 Kuba Andrýsek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
