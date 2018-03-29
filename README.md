
## Setup

Clone the demo repo

```
git clone https://github.com/aerobatic/pelican-academic-demo.git pelican-academic-site
```

<!--  http://nosferalatu.com/Pelican.html -->
### Clone pelican-plugins

```
git clone https://github.com/getpelican/pelican-plugins.git plugins
(cd plugins/md-metayaml; git submodule update --init)
```

Make sure Python3 is installed.

On OSX with homebrew
```
brew install python3
```

Create a virtual env
```
python3 -m venv .
```

Activate the virtual env
```
source bin/activate
```

Now
```
pip install -r requirements.txt
```

https://github.com/gcushen/hugo-academic/tree/master/exampleSite
