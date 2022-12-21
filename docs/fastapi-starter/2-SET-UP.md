# Virtual Environments & Packages

Before getting started with our API, we have to first create a virtual environment and install the packages. Luckily, there's a tool we can use to help us with both of them. But first, some quick explanations.

- ### What are virtual environments?

Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages.

- ### What problem does a virtual environment solve?

The more Python projects you have, the more likely it is that you need to work with different versions of Python libraries, or even Python itself. Newer versions of libraries for one project can break compatibility in another project.

- ### What are packages?

A **package** is a bundle of reusable code.
_Packages_ can also be called libraries, dependencies or imports.

# Create Virtual Environments and Install Packages

## [Pipenv](https://pipenv.pypa.io/en/latest/) 💡

Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages.

- Pipenv automatically maps projects to their specific virtual environments.

- By default, the virtualenv is stored globally with the name of the project’s root directory plus the hash of the full path to the project’s root (e.g., my_project-a3de50).

### Setting up a Virtual Environment with Pipenv and Installing Dependencies

1. Install Pipenv with pip: `pip install --user pipenv`

> This does a user installation to prevent breaking any system-wide packages.

2. Create a folder for your project: `mkdir my-project && cd my-project`

3. Start installing packages:

   - `pipenv install fastapi`
   - `pipenv install "uvicorn[standard]"`

> We need `uvicorn` to run our server later

```shell
# terminal output:

...
Updated Pipfile.lock (4f56a0)!
Installing dependencies from Pipfile.lock (4f56a0)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
To activate this projects virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

Pipenv will install the FastAPI library and create a Pipfile for you in your project’s directory. The Pipfile is used to track which dependencies your project needs in case you need to re-install them, such as when you share your project with others.

[Next → Git](https://karlaevelize.github.io/fastapi-starter/docs/fastapi-starter/3-GIT)
