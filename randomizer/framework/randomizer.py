import os

from typing import List
from .patch import Patch
from .rom import Rom
from .settings import Settings
from randomizer.custom.customized_randomizer import CustomizedRandomizer

class Randomizer(CustomizedRandomizer):
  def __init__(self) -> None:
    self.input_filename: str = ""
    self.output_location: str = ""
    self.seed: int = 0
    self.settings: Settings

  def ConfigureSettings(self, seed: int, settings: Settings) -> None:
    self.seed = seed
    self.settings = settings

  def Settings(self, input_filename: str, output_location: str, seed: int) -> None:
    self.input_filename = input_filename
    self.output_location = output_location
    self.seed = seed
    self.settings = Settings()

  def Run(self) -> None:
    (input_path, input_full_filename) = os.path.split(self.input_filename)
    (input_filename, input_extension) = os.path.splitext(input_full_filename)
    output_filename = os.path.join(
        self.output_location or input_path,
        "%s-randomized-%d%s" % (input_filename, self.seed, input_extension or ".nes"))
    output_rom = Rom(output_filename, src=self.input_filename)
    output_rom.OpenFile(write_mode=True)

    patch = self.GetPatch()
    for address in patch.GetAddresses():
      data: List[int]
      data = patch.GetData(address)
      output_rom.WriteBytes(address, data)
    print("Patch written!")

