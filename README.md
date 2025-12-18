# FermentationsModel

## How to work with Git

Before starting to work on the repository, always run the following cmd:

### Getting new code from GitHub

```sh
git pull
```

Submitt your changes to version control frequently and in small chunks with the following commands.

### Updating code

Stage your changes. `.` adds every file with a change. By naming the file-paths individual files can be staged.

```sh
git add .
```

Write a concise commit message for the changes you have made. Ideally commit are small and only change one thing. A "thing" may be multiple lines of code in multiple files but contributes to the same feature, bug-fix, etc. [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) provides a commonly used framework on how to write commit messages.

```sh
git commit -m ""
```

After you have commited your changes locally, you can submit them to the shared version control (Github), so others can see your changes.

```sh
git push
```

## Run the code

For executing the code during local development run the following command in your terminal:

```sh
uv run src/main.py "$(cat test/test_data/test_input.json)"
```

This will take the data from the file `test/test_data/test_input.json` and pass it to the python script in `src/main.py`. The result of the script will be returned in the terminal.

As this may be inconvenient depending on the length of the output, you may "redirect" (<> operators) the result (and any other e.g. print-statements) into a file. This is done with the following command:

```sh
uv run src/main.py "$(cat test/test_data/test_input.json)"" > output.json
```

## Installing new packages

To install new packages run

```sh
uv pip install [package]
```

where `[package]` should be replaced with the name of the package you want to install.

## Developing and running tests

To ensure the functionality of the code, create unit tests that determine whether the expected result is returned. New tests should be put into the `test`-directory and include `test` in their filename. Multiple tests can be grouped together in one file.

The tests can be executed with the following command:

```sh
uv run pytest
```

Ideally, the tests cover the entirety of the code base. Whether this is the case or not can be checked with:

```sh
uv run pytest --cov=.
```

## Updating "interfaces"

To reduce the coupling of the current variable naming of the input-format and the models to the code that performs the calculation, the DataModels may used. If the name of a variable changes (e.g. in the input-format) only the name of the right hand side of the respective enum has to be adapted. If a new variables is introduced, it should be added to the DataModels as well.


## USAGE with eXCEl

Bioreaktor_forPy dient als Hilfs GUI, Werte eintragen, speichern
Excel_to_JSON aufrufen (erneuert die JSONS in .src/DataModels und TEst(TEst_data))
dann wie gewohnt main.py mit uv starten

Es resultiert eine output.json die dann mit index.html angezeigt werden kann (Ausführung als localer server mit py -m http.server)
