import os
import sys

from absl import app
from absl import flags

from randomizer.framework.randomizer import Randomizer

flags.DEFINE_integer(name='seed', default=-1, help='The seed number to initialize RNG with.')
flags.DEFINE_string(
    name='input_filename', default='', help='The filename of the vanilla ROM to randomize.')
flags.DEFINE_string(
    name='output_location', default='', help='The location to put the randomized ROM.')
flags.DEFINE_enum(
    'text_speed',
    'normal',
    ['very_fast', 'fast', 'normal', 'slow', 'very_slow', 'random'],
    'How fast the text speed will go. Fast speed is, well, fast, but slower speed allows for '
    'resetting door repair charges.',
)

# TODO: Turn this enum into a string with lambda validation.
flags.DEFINE_enum('level_text', 'level-',
                  ['level-', 'house-', 'block-', 'random', 'cage_-', 'home_-', 'castle'],
                  'What are the dungeons called? This is strictly for fun.')

FLAGS = flags.FLAGS


def main(unused_argv) -> None:
  print("")
  print("Randomizer command line interface.")
  print("")
  if FLAGS.input_filename == '' or FLAGS.seed < 0:
    print("To run the randomizer from the command line, the following parameters are required:")
    print("  --input_filename: The file name of a vanilla ROM to randomize")
    print("  --output_location: The directory where the randomized ROM should be written")
    print("  --seed: A seed number to generate the randomized ROM")
    sys.exit(1)
  output_location = FLAGS.output_location
  if output_location == '':
    output_location = os.getcwd()

  randomizer = Randomizer()
  randomizer.Settings(FLAGS.input_filename, FLAGS.output_location, FLAGS.seed)
  randomizer.Run()


if __name__ == '__main__':
  app.run(main)
