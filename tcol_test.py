import tcol as tc

def test_list():
  for fg in range(0,100):
    for tp in range(0,9):
      print(tc.fmt("%02d;%dm" % (fg,tp), fg, tp)),
    print("")
  print(tc.fmt("The default green!"))

def test_t1():
  for c in ["red","blue","green","yellow","cyan","magenta","black","white"]:
    for t in ["bold","opaque","normal","underline","blink"]:
      print(tc.fmt("blalbla", c, t)),
    print("")

if __name__ == "__main__":
  test_list()
  test_t1()
  print(tc.fmt("sdfdsf", tc.RED, tc.BOLD))
  print(tc.fmt("my colored text", "blue", "bold"))
  print("Do the %s: This is my %s %s" % \
        (tc.fmt("color", tc.RED), 
         tc.fmt("blue", "blue", "normal"),
         tc.fmt("text", "green", "underline")
        ))

