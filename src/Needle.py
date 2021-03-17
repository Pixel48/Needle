import os
from time import sleep as wait

rawScriptPath = input("Path to outdated VooDoo script: ")
rawScriptFolder, rawScriptName = os.path.split(rawScriptPath)
rawScriptNameBase, rawScriptNameExt = rawScriptName.split('.')
outScriptPath = os.path.join(rawScriptFolder, '.'.join(
    (rawScriptNameBase + "_needled", rawScriptNameExt)))

f_in = open(rawScriptPath)
f_out = open(outScriptPath, 'w')

print("\n\tFiles opend\r", end='', flush=True)

pos = 0
for line in f_in.readlines():
  pos += 1
  print("\tConverted line " + str(pos) + "\r", end='', flush=True)
  if pos in (13, 17, 19, 27, 30, 31, 38):
    if pos == 13:
      f_out.write("_scene = bpy.context.collection\n" + line)
    if pos in (17, 31, 38):
      f_out.write("_" + line)
    if pos == 19:
      f_out.write(line.replace("DEGREES", "MILLIMETERS"))
    if pos == 27:
      f_out.write(line.replace("_", ".focus_"))
    if pos == 30:
      f_out.write(line.replace("draw", "display"))
    continue
  else:
    f_out.write(line)

f_in.close()
f_out.close()

print("\tConversion done!", flush=True)
wait(1)
