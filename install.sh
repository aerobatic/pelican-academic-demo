
# Create a python3 virtual env 
python3 -m venv .

# Activate the virtual env
source bin/activate

# Clone the pelican-plugins repo
git clone https://github.com/getpelican/pelican-plugins.git plugins

# Update the submodules for the md-metayaml plugin
(cd plugins/md-metayaml; git submodule update --init)

# Install the requirements with pip
pip install -r requirements.txt

# Install the pelican-academic theme.
# Should we clone it from git or use the pelican_themes command?







