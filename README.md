# [BaniDB](https://pypi.org/user/KhalisFoundation/)
[![](bdb.svg)](http://banidb.com)

# Vision Statement

BaniDB's vision is to create a single, universally accessible Gurbani Database for Sikh websites and applications. BaniDB is, and will continue to be, the most accurate and complete Gurbani database ever created for use by Sikhs around the world.

In order to make this vision possible, members of this collaborative effort work to ensure that the platform is self-sustaining, tested, and secure.

## Python package for BaniDB API

### Installation
With pip
```
pip install banidb
```

### Usage
Quick Start
```
shabad = banidb.random()
print(shabad)

```
Search shabad by first letters"
```
print("\tSearching Bandhana Har Bandhana ....")
shabad = banidb.search("bhbgggr")
print(shabad)
```


## Release
### Checkout the main branch
``` 
git checkout main
git pull
```

#### Increment the version 

Pick one of the `major|minor|patch` to update 
For example, let's release the version to 0.4.0

```
bump2version --allow-dirty --verbose --commit --tag --new-version 0.4.0 patch setup.py
```

For minor
``` 
bump2version --allow-dirty --verbose --commit --tag --new-version 0.4.0 minor setup.py

```

For major
```  
bump2version --allow-dirty --verbose --commit --tag --new-version 1.0.0 major setup.py

```

Note: its always good to start with the `--dry run` first

### Push to remote
```
git push

```
Push the tag to remote too
in our case 0.4.0 `git push origin 0.4.0`
```
git push origin <tag-name>
```

#### Run the github release action

#### From UI
This will upload the bits to pypi.org
It can be done from the UI. Select the tag we just created and pushed

#### From CLI (untested)
`gh` has a new feature to trigger workflow from the CLI. 
Note: at the time of writing this doc, this feature was not working on MacOS 
``` 
gh workflow run python-publish.yml
```

