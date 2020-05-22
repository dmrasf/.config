# Defined in - @ line 1
function f --description "alias f fzf --height 40% --reverse --preview 'ccat {}'"
	fzf --height 60% --reverse --preview 'ccat -C="always" {}' $argv;
end
