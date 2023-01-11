import xml.etree.ElementTree as ET

class FastbootBuilder:
  commands: list
  def __init__ (self, filepath):
    self.filepath = filepath

  @classmethod
  def of (self, filepath):
    return FastbootBuilder(filepath)
  
  def serialize (self):
    tree = ET.parse(self.filepath)
    root = tree.getroot()
    self.commands = root.findall(".//step")
    return self

  def build (self):
    listCommands = []
    for command in self.commands:
      if 'partition' in command.attrib:
        operation = command.attrib['operation']
        partition = command.attrib['partition']
        if 'filename' in command.attrib:
          file = command.attrib['filename']
          listCommands.append(f'fastboot {operation} {partition} {file}')
        listCommands.append(f'fastboot {operation} {partition}')
    return listCommands