import random

from randomizer.framework.patch import Patch

VERSION = '0.01'
PREFIX = "ABC" # An acronym for your game
GAME_NAME = "Insert Game Name Here"

class CustomizedRandomizer(object):
  def __init__(self) -> None:
    self.input_filename: str = ""
    self.output_location: str = ""
    self.seed: int = 0
    self.settings: Settings

  # Add custom logic for your randomizer to patch the vanilla ROM here
  def GetPatch(self) -> Patch:
    # Initialize random number generation and empty ROM patch to return
    random.seed(self.seed)
    patch = Patch()

    print("Hello world!")
    if self.settings.shuffle_thing:
      print("Shuffle Thing flag is enabled!")
      # patch.AddData(0x1234, [0x01, 0x02, 0x03])
    else:
      print("Shuffle Thing flag is not enabled")

    return patch