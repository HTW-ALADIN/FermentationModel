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
uv run src/main.py -p ./test/test_data/test_input.json
```

This will take the data from the file `test/test_data/test_input.json` and pass it to the python script in `src/main.py`. The result of the script will be returned in the terminal.

As this may be inconvenient depending on the length of the output the result can be written into a file. This is done with the following command:

```sh
uv run src/main.py -p ./test/test_data/test_input.json -o df -f ausgabe.json
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

To reduce the coupling of the current variable naming of the input-format and the models to the code that performs the calculation, the DataModels may be used. If the name of a variable changes (e.g. in the input-format) only the name of the right hand side of the respective enum has to be adapted. If a new variables is introduced, it should be added to the DataModels as well.
TODO: Adapt for string values in Fx_ODE_Bioreaktor.py as well.

## USAGE with eXCEl

Bioreaktor_forPy dient als Hilfs GUI, Werte eintragen, speichern
Excel_to_JSON aufrufen (erneuert die JSONS in .src/DataModels und TEst(TEst_data))
dann wie gewohnt main.py mit uv starten

Es resultiert eine output.json die dann mit index.html angezeigt werden kann (Ausführung als localer server mit py -m http.server)

## UPDATE 21.12.2025

!WICHTIG! An der Main bitte nicht herumschrauben – Erweiterungen/Änderungen ausschließlich über die Adapter und die CLI-Parameter (Util/argparser.py). Sonst haut das mit der Schnittstelle zu ALADIN nicht hin.

Alle Berechnungen liegen im Ordner „calc“.

Command Line Interface

    steuert welcher Input und output Adapter vewendet wird

    Bei Fehlermeldung, sowie per -h Flag wird ne Hilfsanleitung zu den Optionen ausgegeben.

INPUT Adapter (zum Auslesen der User-Inputparameter der Modellierung)

    stdin - Standardmethode einlesen der Daten aus der Kommandozeile
    file - zum Auslesen aus einer JSON Datei
    excel - zum direkten Auslesen aus der Datei "Bioreaktor_forPy.xlsx"

OUTPUT Adapter

df - Schreiben als Dataframe 
Chart - als Chart.Js 

Output 
    stdout - Standardmethode
    file - zum Schreiben in eine Datei


Modelldatenbank aktualisieren:

    Die Synchronisation der Excel mit der „Model-Datenbank" (src\DataModels\model_db.json) ist als Utility implementiert (src\Util\sync_excel_models_to_json_file.py) und sollte gezielt ausgeführt werden 

Plotten der Ergebnisse in Python
    Um die Modellergebnisse in Python zu Plotten, liegt unter Util "src\Util\multiplot_ferm.py". Der Aufruf ist in der Main auskommentiert. Zum Testen kann man es wieder einkommentieren oder einfach in nen Test-Case auslagern.


DEBUGGING und Programmlog

Statusausgaben sind über über Logger implementiert. Das LOG_LEVEL kann über eine „.env“-Datei im Wurzelverzeichnis des Repositories gesteuert werden – Default bei Nicht-Setzung ist „INFO“. Es ist gute Praxis die .env-Datei nicht zu versionieren, da diese ggf. auch Geheimnisse enthalten kann, die nicht öffentlich im Git stehen sollen. D. h. die musst du dir einmal manuell anlegen. Die „.demo.env“ ist nur zur Doku der vorhandenen Variablen.


REMARKS:

Output Adapter DF: funktioniert nicht zum Anzeigen der JSON Datei im Browser da Value Pairs erzeugt werden und kein JSON Array
