import os
import sys
from builder import FastbootBuilder

class FastbootInstallation:
  commandList: list

  @classmethod
  def config (self):
    if os.path.exists('flashfile.xml'):
      self.fastbootBuilder(self, 'flashfile.xml')
    else:
      self.fastbootBuilder(self, 'servicefile.xml')

  @classmethod
  def run (self):
    for command in self.commandList:
      os.system(command)

  def fastbootBuilder (self, filepath):
    self.commandList = FastbootBuilder.of(filepath).serialize().build()

def main ():
  FastbootInstallation.config()
  FastbootInstallation.run()
