from nim import train
import sys

def main():

	# Check command-line arguments
	if len(sys.argv) != 3:
		sys.exit("Usage: python train.py filename.npy 100")

	train(int(sys.argv[2]), sys.argv[1])

if __name__ == "__main__":
	main()