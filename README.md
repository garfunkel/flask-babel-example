# flask-babel-example
Example of implementing i18n support with Flask-Babel.

##Instructions
###Install Flask-Babel
`pip install Flask-Babel`

###Clone Repo
`git clone https://github.com/garfunkel/flask-babel-example`
`cd flask-babel-example`

###Extract/Update Translatable Strings
We need to instruct Flask-Babel to extract translatable strings from Python source code and from templates. This command extracts these strings into a catalogue file, qhich essentially is just a list of English strings.

`pybabel extract -F babel.cfg -o messages.pot app`

Now we need to create translation files for the supported languages. For this sample project, we only have Spanish as a supported language, but more can be added to the config, and the process is the same.

`pybabel update -i messages.pot -d app/translations`

After this, we will have a .po file for each supported language inside the app/translations folder. Users can then translate these files using a tool such as POEdit.

###Compile Translations
Once translations have been produced, we need to compile the resulting strings for use in our application. If using POEdit, this step is not necessary, as it compiles translations when saving .po files.

`pybabel compile -d app/translations`

After this, we are done! Our app can now be used in any of the languages translated. If some strings are not translated, the default given in the babel config file is used. If a default is not provided, English is used as the default automatically.
