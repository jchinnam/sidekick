# Aliases
alias up='. ~/bin/up'

# Customizing prompt [currently overridden by starship below]
autoload -Uz vcs_info
precmd_vcs_info() { vcs_info }
precmd_functions+=( precmd_vcs_info )
setopt prompt_subst

zstyle ':vcs_info:git:*' formats '%F{green}(%b)%f'
zstyle ':vcs_info:*' enable git

PROMPT='%B%F{240}%3~ ${vcs_info_msg_0_}%b%f %# '

# Starship
eval "$(starship init zsh)"

# Customize terminal tabs (https://gist.github.com/phette23/5270658)
DISABLE_AUTO_TITLE="true"

precmd() {
  # sets the tab title to current dir
  echo -ne "\e]1;${PWD##*/}\a"
}
