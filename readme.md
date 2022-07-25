# charred.nvim

A simple plugin to automatically format python code.

I wrote this for myself, I don't know what I'm doing. All it does is run isort
and black on any python buffer on write. It has no options. Use at your own
risk.

## Installation

You should have your python venv setup for neovim. If you don't, do that.
Here's one way to do it:
```shell
mkdir -p ~/.local/venv && cd ~/.local/venv
python -m venv nvim
source nvim/bin/activate
pip install pynvim
```
Then let neovim know which virtual environment to use with:
```lua
vim.g.python3_host_prog =  os.getenv("HOME").."/.local/venv/nvim/bin/python"
```
With your virtual environment setup make sure you install black and isort.
```shell
source ~/.local/venv/nvim/bin/activate
pip install black isort
```
Then using whatever package manager you like for neovim install this plugin.
```lua
require('packer').startup(function()
  use 'erooke/charred.nvim'
)
```
Is how you would do it with packer for example.
