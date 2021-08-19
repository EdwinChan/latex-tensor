import os
import os.path
import shutil
import subprocess
import tempfile

def make_document(unicode_math, flex_pos):
  return (
    r'''
    \documentclass{article}
    \usepackage{color}
    \usepackage[''' + ('flexpos' if flex_pos else '') + ''']{tensor}
    '''
    + (r'\usepackage{unicode-math}' if unicode_math else '') +
    r"""
    \newcommand*\bl{%
      \clap{\color\lc\vrule width 2\paperwidth height .01pt depth .01pt}}
    \begin{document}
    $\tensor{f'}{}$
    \def\lc{red}$\tensor{g''}
      {_\alpha\beta\bl^\gamma\delta\bl_\epsilon\zeta\bl^\eta\theta\bl}$
    \def\lc{green}$\tensor{h'''}
      {^\alpha\beta\bl_\gamma\delta\bl^\epsilon\zeta\bl_\eta\theta\bl}$
    \def\lc{blue}$\tensor{\Bigg|}
      {^\alpha^\beta^\gamma\bl_\delta_\epsilon_\zeta\bl}$
    \def\lc{cyan}$\displaystyle\int
      _{\tensor x{^\alpha\bl_\beta\bl}}^{\tensor{y'}{_\gamma\bl^\delta\bl}}$
    \end{document}
    """)

test_cases = {
  'p':   ('pdflatex', False, False),
  'x':   ('xelatex',  False, False),
  'xu':  ('xelatex',  True,  False),
  'l':   ('lualatex', False, False),
  'lu':  ('lualatex', True,  False),
  'luf': ('lualatex', True,  True )}

cur_dir = os.getcwd()

with tempfile.TemporaryDirectory() as tmp_dir:
  os.chdir(tmp_dir)

  for fname, (latex, unicode_math, flex_pos) in test_cases.items():
    tex_fname     = os.path.join(tmp_dir, fname + '.tex')
    src_pdf_fname = os.path.join(tmp_dir, fname + '.pdf')
    dst_pdf_fname = os.path.join(cur_dir, fname + '.pdf')

    with open(tex_fname, 'wt') as file:
      file.write(make_document(unicode_math, flex_pos))

    subprocess.run(
      [latex, '-interaction=nonstopmode', tex_fname],
      check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    shutil.move(src_pdf_fname, dst_pdf_fname)
