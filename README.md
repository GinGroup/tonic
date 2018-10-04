# tonic
FE Codebase for shape optimization in fluid problems

## Cheatsheet for contributors

### Initial setup

Initial setup is via:

1. Fork repositiory to your account via the Github website
2. Clone repository with https:
```
git clone https://github.com/USERNAME/tonic.git
```
Clone repository with ssh:
```
git clone git@github.com:USERNAME/tonic.git
```
3. Install with pip:
```
 cd tonic
 pip install --user -e .
```
4. Set upstream remote with https:
```
git remote add upstream https://github.com/gingroup/tonic.git
```
Set upstream remote with ssh:
```
git remote add upstream git@github.com:GinGroup/tonic.git
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

Tox doesn't seem to work very well with anaconda. Under the assumption we want to stick with using anaconda to install FEniCS, a bash script has been written to automate the testing.
In order to run the test suite do:

```
./provision/travis/run-tests.sh
```

This will:
1. Run pytest
2. Attempt to build the documentation
3. Run `black --check` against the module code

The Travis build will fail if any of the above fail.

