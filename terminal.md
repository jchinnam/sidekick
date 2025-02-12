# terminal
## get iterm2
- download and install [iTerm2](https://iterm2.com/)
- Settings > Appearance > Theme: Minimal

### set up profile
- Settings > Profiles > create a new profile, "Banana", set it as default profile
- Within that profile, set the following 
  - in General > Basics: set Title to Session Name
  - in Window: set Transparency to 9
  - in Window: check Blur and set to 13
  - in Colors > Color Presents: Import (stored here in `iterm2/banana.itermcolors`)
  ![](/img/iterm2_profile_colors.png)

### add custom font
  - download [Meslo](https://www.programmingfonts.org/#meslo) from [nerd fonts](https://www.nerdfonts.com/font-downloads) and move the folder to `~/Library/Fonts/`
  - in Preferences > Text > Font: select it (may be named MesloGLDZ Nerd Font Mono), set font size to 12, set `n/n` to 115

## customize tab titles
- set tab titles to be the current directory by adding the following to `zshrc` ([source](https://gist.github.com/phette23/5270658))
```bash
DISABLE_AUTO_TITLE="true"
precmd() {
  # sets the tab title to current dir
  echo -ne "\e]1;${PWD##*/}\a"
}
```

## add [starship](https://starship.rs/)
- install starship to computer with `curl -sS https://starship.rs/install.sh | sh`
- if doing from scratch, create and populate `~/.config/starship.toml` via instructions at https://starship.rs/config/
    - styling strings: https://starship.rs/advanced-config/#style-strings
    - icons for module symbols: https://www.nerdfonts.com/cheat-sheet
- or copy from `starship.toml` in this repo
- add the below to `zshrc`:
```bash
eval "$(starship init zsh)"
```
