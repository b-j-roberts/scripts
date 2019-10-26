import subprocess
import time

current_down = False
clocked_in = time.time()
double_test = False
just_clicked = False
while(True):
  output = subprocess.check_output("xinput query-state 17", shell=True).decode()
  pos = output.find('button[1]')
  update_time = False
  if output[pos + 10 : pos + 11] == 'u':
    if current_down and not just_clicked:
      double_test = True
    current_down = False
    just_clicked = False
  else:
    if not current_down:
      update_time = True
    current_down = True
  if current_down:
    if double_test and time.time() - clocked_in < .2:
      subprocess.check_call("xdotool click 3", shell=True)
      just_clicked = True
    double_test = False
    if update_time:
      clocked_in = time.time()
