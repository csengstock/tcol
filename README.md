# tcol
Ansi text colors for command line apps

## Usage

```
import tcol as tc

print(tc.fmt("sdfdsf", tc.RED, tc.BOLD))
print(tc.fmt("my colored text", "blue", "bold"))
print("Do the %s: This is my %s %s" % \
      (tc.fmt("color", tc.RED), 
       tc.fmt("blue", "blue", "normal"),
       tc.fmt("text", "green", "underline")
      ))

```
