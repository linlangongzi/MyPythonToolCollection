import argparse

def visualize_bits(number, numberOfBits):
  """Prints the binary representation of a number with bit indices"""
  result = format(number, 'b')  # Convert to binary string
  # Pad with leading zeros to ensure 32-bit representation
  padded_result = result.zfill(numberOfBits)

  # Print bit indices
  print("Binary Representation:  \n")
  for i in range(numberOfBits)[::-1]:
    if i >= 10:
      print(i, end=" | ")
    else:
      print(i, end="  | ")

  print("\n")
  # Print each bit with a space for readability
  for bit in padded_result:
    print(bit, end="  | ")


if __name__ == "__main__":
  # Parse command line arguments
  parser = argparse.ArgumentParser(description="Visualize binary representation of a number")
  parser.add_argument("leftShift", type=int, help="The number to left shit")
  parser.add_argument("--bits", type=int, default=32, help="Number of bits to display (default: 32)")
  args = parser.parse_args()

  # Validate input
  if args.bits < 0:
    print("Error: Number of leftShift cannot be negative.")
    exit(1)

  # Call the visualize_bits function with user input
  visualize_bits((1 << args.leftShift) - 1, args.bits)