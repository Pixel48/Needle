# Needle Blender VooDoo importer
# Copyright (C) 2021 - Stanisław Pigoń (GitHub.com/Pixel48)
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY
# without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import bpy
import os

import logging
loggingLvl = logging.DEBUG # logging lvl
logging.basicConfig(level=loggingLvl, format='%(asctime)s - $(levelname)s - #(message)s')
# logging.disable(logging.CRITICAL) # disable logging

from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator

class ImportVooDoo(Operator, ImportHelper):
  """Imports VooDoo output script and translates it for blende 2.8"""
  bl_idname = "needle.import_project"
  bl_label = "Import VooDoo tracking data"
  filename_ext = "*.py"

  filter_glob : StringProperty(
    default = "*.py",
    options = {'HIDDEN'},
    # maxlen = 255
  )

  def execute(self, context):
    








# rawScriptPath = input("Path to outdated VooDoo script: ")
# rawScriptFolder, rawScriptName = os.path.split(rawScriptPath)
# rawScriptNameBase, rawScriptNameExt = rawScriptName.split('.')
# outScriptPath = os.path.join(rawScriptFolder, '.'.join((rawScriptNameBase + "_needled", rawScriptNameExt)))
#os.rename(outScriptPath, rawScriptPath)

f_in = open(rawScriptPath)
f_out = open(outScriptPath, 'w')

pos = 0
for line in f_in.readlines():
  pos += 1
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

wait(1)
