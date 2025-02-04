# terminal
## get iterm2
- download and install [iTerm2](https://iterm2.com/)
- Settings > Appearance > Theme: Minimal

### set up profile
- set up a new profile, "Banana", set it as default profile
  - in Preferences > General > Basics: set Title to Session Name
  - in Preferences > Window: set Transparency to 9
  - in Preferences > Window: check Blur and set to 13
  - in Preferences > Colors > Color Presents: Import (stored in `iterm2/banana.itermcolors`)
  ![](/img/iterm2_profile_colors.png)

### add custom font
  - download [Meslo](https://www.programmingfonts.org/#meslo) from [nerd fonts](https://www.nerdfonts.com/font-downloads) and save in `~/Library/Fonts/`
  - in Preferences > Text > Font: select it and set font size to 12 (may be named MesloGLDZ Nerd Font Mono)

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
- install with `curl -sS https://starship.rs/install.sh | sh`
- create and populate `starship.toml`, lives at `~/.config/starship.toml`
  - see https://starship.rs/config/ to get started from scratch
    - styling strings: https://starship.rs/advanced-config/#style-strings
    - icons for module symbols: https://www.nerdfonts.com/cheat-sheet
  - or copy from `/starship.toml` in this repo
- add to `zshrc`:
```bash
eval "$(starship init zsh)"
```
