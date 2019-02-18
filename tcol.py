"""
Convenience function to help with ansi text colors.

Usage:

  import tcol as tc

  print(tc.fmt("sdfdsf", tc.RED, tc.BOLD))
  print(tc.fmt("my colored text", "blue", "bold"))
  print("Do the %s: This is my %s %s" % \
        (tc.fmt("color", tc.RED), 
         tc.fmt("blue", "blue", "normal"),
         tc.fmt("text", "green", "underline")
        ))

"""

BLACK=30
RED=31
GREEN=32
YELLOW=33
BLUE=34
MAGENTA=35
CYAN=36
GREY=GRAY=37
WHITE=38

BOLD=1
OPAQUE=2
NORMAL=3
UNDERLINE=4
BLINK=5

COLS = {
  "BLACK": BLACK,
  "RED": RED,
  "R": RED,
  "GREEN": GREEN,
  "G": GREEN,
  "YELLOW": YELLOW,
  "Y": YELLOW,
  "BLUE": BLUE,
  "B": BLUE,
  "MAGENTA": MAGENTA,
  "M": MAGENTA,
  "CYAN": CYAN,
  "C": CYAN,
  "GREY": GREY,
  "WHITE": WHITE
}

TYPE = {
  "BOLD": BOLD,
  "B": BOLD,
  "OPAQUE": OPAQUE,
  "O": OPAQUE,
  "NORMAL": NORMAL,
  "N": NORMAL,
  "UNDERLINE": UNDERLINE,
  "U": UNDERLINE,
  "BLINK": BLINK,
  "L": BLINK
}

def fmt(s, c=32, t=1):
  if type(c) == str:
    c = COLS[c.upper()]
  if type(t) == str:
    t = TYPE[t.upper()]
  return "\033[%d;%dm%s\033[0m" % (c, t, s) 

