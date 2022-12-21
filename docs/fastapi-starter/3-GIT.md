# Git

Before we write any code, we want to make sure that we have the tools we need to keep track of it.

Keeping a detailed log of all the changes you make sounds like a lot of work, doesn't it? That's what Git is for, and not only that!

Git helps us:

- keep a detailed log of what happened in our code
- travel through time and switch to previous versions of our code
- collaborate with others by hosting our code on a remote repository

In other words, one could argue that Git enables you to _**Code Fearlessly**_.

## Using Git

The first thing you want to do is to start tracking, but remember you don't have to push everything to GitHub, some files should be _ignored_, usually files that contains secrets, dependency caches, the content of node_modules or packages, etc.

Make sure you are in the correct directory in your terminal and run the following:

1. `git init`
2. `touch .gitignore`
3. Open git ignore (with `nano` or a code editor of your preference) and add to it:

```js
//.gitignore

*.pyc
__pycache__/
```

This will be enough for now, but we might ignore more files later. Feel free to make your first commit already.

[Next → Getting Started](https://karlaevelize.github.io/fastapi-starter/docs/fastapi-starter/4-GETTING-STARTED)
