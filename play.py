import nim
import sys
import numpy as np

def main():

	# Check command-line arguments
	if len(sys.argv) != 2:
		sys.exit("Usage: python play.py filename.npy")

	ai = nim.NimAI()
	ai.q = np.load(sys.argv[1], allow_pickle="True").item()

	nim.play(ai)

if __name__ == "__main__":
	main()
