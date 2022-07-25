import black
import pynvim as nvim
from isort.api import sort_code_string
from isort.settings import Config
from pynvim import Nvim


@nvim.plugin
class Charred:
    def __init__(self, vim: Nvim):
        self.vim = vim

    @nvim.autocmd("BufWritePre", pattern="*.py", sync=True)
    def char(self):
        buffer = "\n".join(self.vim.current.buffer)
        mode = black.FileMode()

        try:
            buffer = black.format_file_contents(buffer, fast=False, mode=mode)
        except black.NothingChanged:
            pass
        except black.InvalidInput:
            pass

        isort_config = Config(
            multi_line_output=3,
            include_trailing_comma=True,
            force_grid_wrap=0,
            use_parentheses=True,
            ensure_newline_before_comments=True,
            line_length=88,
        )

        buffer = sort_code_string(buffer, config=isort_config)

        self.vim.current.buffer[:] = buffer.split("\n")[:-1]
