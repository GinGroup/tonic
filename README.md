# tonic
FE Codebase for shape optimization in fluid problems

## Cheatsheet for contributors

### Initial setup

Initial setup is via:

1. Fork repositiory to your account via the Github website
2. Clone repository:
```
git clone https://github.com/USERNAME/tonic.git
```
3. Install with pip:
```
 cd tonic
 pip install --user -e .
```
4. Set upstream remote.
```
git remote add upstream https://github.com/gingroup/tonic.git
```

When you want to write some code:

1. Checkout master:
```
git checkout master
```
2. Pull any changes from upstream:
```
git pull upstream master
```
3. Checkout a new branch
```
git checkout -b myFeature
```
4. ???
5. Profit!

### Building of documentation

Make sure you've got sphinx installed. In the doc directory simply do:
```
make html
```

This builds an html version of the documentation that will be in doc/build

### Testing

Will need to see what the alternative to tox is with anaconda.

