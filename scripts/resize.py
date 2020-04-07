import Augmentor  # pylint:disable=import-error

# Augmentor doesn't reset working directory after
# navigating to INPUT_PATH, apparently
INPUT_PATH = "./gallery-dl/output"
OUTPUT_PATH = "../../resized"
DIM = 512

p = Augmentor.Pipeline(INPUT_PATH, OUTPUT_PATH)
p.resize(probability=1.0, width=DIM, height=DIM)
p.process()
