# Kestrel Documentation Website

Landing page for downloading released and mdbook for documentation.


# Building

rsync -a site/ static/
rsync -a releases static/
mdbook build

