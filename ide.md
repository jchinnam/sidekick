# IDE
### get IDEs
- download and install JetBrains [Pycharm](https://www.jetbrains.com/pycharm/) & [IntelliJ](https://www.jetbrains.com/idea/)

### set theme
I don't typically set the theme anymore as the default Dark theme is pretty good, but if I want to:
- Preferences > Plugins > (Gear) Install Plugins from Disk > choose jar (stored in `/jetbrains/atom-one-jetbrains.jar`)
- If changes aren't immediately reflected, restart IDE
- Preferences > Appearance & Behavior > Appearance > Theme: Atom One Dark 

### set color scheme
- Preferences > Editor > Color Scheme > (Gear) Import Scheme > choose file (stored in `/jetbrains/one_dark_janani.icls`)
- Other colors I often tweak via Preferences > Editor > Color Scheme > General:
  - Editor background color: Editor > Color Scheme > General > Text > Default Text > Background
  - Highlighted row color: Editor > Color Scheme > General > Editor > Carot Row
  - Keyword param: Editor > Color Scheme > Python > Keyword Argument

### configure menus
- Turn on Local Changes menu: Preferences > Version Control > Commit: Uncheck "use non-modal commit interface" ([source](https://stackoverflow.com/questions/63942404/how-to-turn-on-local-changes-default-changelist-for-git-in-intellij))
- Customize main toolbar: Right click on menu bar at the top (where repo name is listed) and choose "Customize Toolbar". Under the "Left" section, add:
  - Version Control Systems button: Update Project 
  - Version Control Systems > Git buttons: Push, Show History
  - Separator
  - Main Menu > Navigate buttons: Back, Forward
  ![](/img/ide_main_toolbar_settings.png)
