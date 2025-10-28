# HANDLING PYTHON PROJECT WITH uv

#### PROJECT DESCRIPTION
Currently, handling Python packages is made possible with `pip` and hence we cannot overwrite the advantages it has contributed to the Python community and developers especially when running packaging tools and managers.

One of the disadvantage of `pip` is that it can be slower especially with many dependencies, cold caches and often each virtual environments duplicates packages.

To achieve more efficient Python packages handling, `uv` provides a much better and improved packaging tools and managers.

What is `uv`?

`uv` is a relatively new Python packaging tool/package manager, developed by `Astral.sh`. It is meant to be high-performance replacement for `pip`, `pip-tools`, and `virtualenv` workflows.

It is written in [RUST](rust-lang.org) and designed for speed, `uv` can install packages faster than `pip`, up to `10-100x` faster, specifically good when working on projects with large dependency trees. It is also comes with a `pip interface` (commands like `uv pip install`, `uv pip sync` etc.), which is designed to be compatible or familiar to users of `pip/pip-tools`. 

For detailed documentation, visit: [UV_DOC](docs.astral.sh/uv/).

#### INSTALLATION

Install `uv` with the official standalone installer both on `WINDOWS` and `MacOS & LINUX`

###### Windows
From the terminal enter the code below
```bash
$ powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
###### MacOS and LINUX
From the terminal enter the code below
```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

###### Restart or Enter the below commands
```bash
cmd: $ set Path=C:\Users\COMPUTER_USERNAME\.local\bin;%Path%
powershell: $ $env:Path = "C:\Users\COMPUTER_USERNAME\.local\bin;$env:Path"
```

###### CHECK FOR THE `uv` INSTALLED VERSION
```bash
$ uv --version
output: uv 0.8.18 (c4c47814a 2025-09-17)  # But will vary depending on your own PC and the uv version
```

##### CREATE A PROJECT WITH `uv`
Once `uv` is installed, we can then use uv to structure our project properly.

One way to manually achieve this is:
```bash
$ mkdir new_project/   # create new project folder or directory
$ cd new_project/   # navigate into the new project folder
$ uv init   # initialize the uv and this automatically created some files automatically that uv will use to track progress.
```
Other way which is the best is:
```bash
$ uv init name_of_folder_for_project  # This will perform the 1st and 3rd stages manual process at once.
$ cd name_of_folder_for_project

For Example:
$ uv init uv_tutorial
$ cd uv_tutorial
$ ls


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         9/18/2025   7:53 PM            .gitignore
-a----         9/18/2025   7:53 PM            .python-version
-a----         9/18/2025   7:53 PM             main.py
-a----         9/18/2025   7:53 PM             pyproject.toml
-a----         9/18/2025   7:53 PM             README.md
```

###### EXAMINE EACH FILES CONTAINED IN NEW PROJECT FOLDER
```bash

The 'pyproject.toml' contains metadata about your project.
$ cat pyproject.toml
output:
[project]
name = "uv-tutorial"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []


The 'main.py' is a default python scripts that only print 'Hello from uv-tutorial!'. It is just to ascertain that 'uv' is working and properly implemented on the project. The main.py can be modified.
$ cat main.py
output:
def main():
    print("Hello from uv-tutorial!")


if __name__ == "__main__":
    main()


This is to track unuse files and folders
$ cat .gitignore
output:
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv


The '.venv' is the default virtual environment folder that contains project's virtual environment, a Python environment that is isolated from the rest of your system. This is where 'uv' will install your project's dependencies.
$ cd .venv
$ ls

output:
output:
Name
---------
Lib
Scripts
.gitignore
.lock
CACHEDIR.TAG
pyvenv.cfg


The '.python-version' file contains the project's default Python version. This file tells 'uv' which Python version to use when creating the project's virtual environment.
$ cat .python-version


uv.lock
'uv.lock' is a cross-platform lockfile that contains exact information about your project's dependencies. Unlike the 'pyproject.toml' which is used to specify the broad requirements of your project, the lockfile conatins the exact resolved versions that are installed in the project environment. This file should be checked into version control, allowing for consistent and reproducible installations across machines. 'uv.lock' is a human-readable TOML file but managed by 'uv' and should not be edited manually.
```

###### CREATING THE VIRTUAL ENVIRONMENT
It is a standard practise to create virtual environment to manage project and one of the greatest advantage using `uv` is that it create `virtual environment` automatically for us after running your first python scripts, especially when you run: `uv run main.py`.

Let me show you the two ways to create virtual environment with `uv`:

```bash
1. You can run the default 'main.py' scripts directly with 'uv run main.py' and since this will be your first script execution, 'uv' will automatically create the new virtual environment named '.venv' where all dependencies will be isolated.

Automatically:
$ cd new_project/
new_project $ uv run main.py

2. You can also create your own manually: $ uv venv or $ uv venv .name_of_your_virtual_environment/ e.g: $ uv venv .uv_tutorial/ --> The dot . is just to keep it as hidden.

Manually:
$ cd new_project/
$ uv venv .name_of_virtual_environment --> E.g: $ uv venv .uv_tutorial/

3. Activate the virtual environment

MACOS: $ source .venv/bin/activate or $ source .name_of_your_virtual_environment/bin/activate

WINDOWS: $ .venv\Scripts\activate or $ .name_of_your_virtual_environment\Scripts\activate

For Example:

$ .venv\Scripts\activate

output:
(.venv) new_project $ 

run:
(.venv) new_project $ ls

output:
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         9/18/2025   8:51 PM                .venv
-a----         9/18/2025   7:53 PM                .gitignore
-a----         9/18/2025   7:53 PM                .python-version
-a----         9/18/2025   7:53 PM                 main.py
-a----         9/18/2025   7:53 PM                 pyproject.toml
-a----         9/18/2025   7:53 PM                 README.md



4. Clear the VENV CACHE
run:
(.venv) new_project $ uv cache clean

5. Deactivate the Virtual Environment
run: 
$ deactivate

6. Delete Virtual Environment if no longer needed
run:
$ rm -r name_of_your_virtual_environment
```

###### MANAGING DEPENDENCIES
In `uv`, we use the keyword `add` to install all packages and libraries.

###### INSTALLING PACKAGES AND DEPENDENCIES
```bash
We achieve this by running:
$ uv add package_name OR $ uv add 'package_name==version'

For example:

$ uv add numpy OR $ uv add 'numpy==1.0.0'

(.venv) uv_tutorial $ uv add numpy, pandas

output:

Resolved 7 packages in 301ms
Prepared 6 packages in 10.95s
Installed 6 packages in 3.24s
 + numpy==2.3.3
 + pandas==2.3.2
 + python-dateutil==2.9.0.post0
 + pytz==2025.2
 + six==1.17.0
 + tzdata==2025.2

# The pyproject.toml will have been updated with the new added dependencies. To check:
$ cat pyproject.toml
[project]
name = "uv-tutorial"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "numpy>=2.3.3",
    "pandas>=2.3.2",
]

```

###### REMOVING PACKAGES AND DEPENDENCIES
We can remove insatlled dependencies with the keyword `remove`
```bash
$ uv remove package_name OR $ uv remove 'package_name==version'

For example:

$ uv remove numpy OR uv remove 'numpy==1.0.0'
```

###### UPDATING THE DEPENDENCIES WITH A REQUIREMENT.TXT FILE
```bash
You can directly use: 
$ uv pip install -r requirement.txt --> To install dependencies for project.

You can also use: 
$ uv pip install -r requirement.txt -c constraints.txt --> This install the dependencies and applies version constraints.

Always use this as standard:
$ uv add -r requirements.txt -c constraints.txt
AND AFTER RUN:
$ uv sync

The above will then install requirements into the uv.lock files and no need for requirements.txt again. This add requirements.txt and the dependencies contained into uv-managed project. It essentially update the pyproject.toml and uv.lock files.
```

###### SAMPLE OF RESULT

Running a sample python script with `uv`
```bash
$ uv run uv_tutorial.py

Enter your full name: UV
Enter your phone number with country code (+): +33XXXXXXXXXX
Enter your location - city, and country: FR
Enter your country of origin: NG
Enter the number of rows for your matrix: 2
Enter the number of columns for your matrix: 2
Enter the rth row and jth column element (A_ij) --> [1][1]: -2
Enter the rth row and jth column element (A_ij) --> [1][2]: -1
Enter the rth row and jth column element (A_ij) --> [2][1]: 1
Enter the rth row and jth column element (A_ij) --> [2][2]: 0

======= FINAL REPORT =======

USER PROFILE:
  NAME LOCATION COUNTRY          PHONE
0   UV       FR      NG  +33XXXXXXXXXX

MATRIX:
[[-2. -1.]
 [ 1.  0.]]

DETERMINANT RESULT: 1.0
```

###### LICENSING AND SUPPORTING ORGANIZATION
`uv` use the [MIT LICENSE](opensource.org/license/mit), which allows free use in open-source and commercial projects. However, `uv` is developed by [Astral](astral.sh), which is a private company.

###### CONCLUSION
In this piece of work, I have been able to introduced a new Python packages and how it handle package installation, dependencies management, and environment reproducibility, as well as speed, ecosystem support, package removal, and governance models.

Choosing the right package manager is crucial for efficient and reputable Python environments. As the ecosystem evolves, understanding the strengths and trade-offs of uv will help developers build faster, cleaner, and more maintainable projects.


###### COMPILED BY:

Email: `larrysman2004@yahoo.com`

###### REFERENCES
[ASTRAL](astral.sh)

[REAL PYTHON](realpython.com/uv-vs-pip/?utm_source=chatgpt.com)
