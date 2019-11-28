import subprocess

screen_active = True
while True:
  output = subprocess.check_output("xinput query-state 17", shell=True).decode()
  pos = output.find('Proximity')
  if screen_active and output[pos + 10 : pos + 11] == 'I':
    subprocess.check_call("xinput disable 11", shell=True)
    screen_active = False
  if not screen_active and output[pos + 10 : pos + 11] == 'O':
    subprocess.check_call("xinput enable 11", shell=True)
    screen_active = True
