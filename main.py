# Block size (bytes)
block_size = 8192

# Number of direct blocks
direct_blocks = 12

# Block number (bytes)
block_number = 8

numbers_in_block = block_size // block_number
print(f"Numbers in a block = {numbers_in_block}")

# Number of bytes in direct blocks (No indirection)
bytes_in_direct_blocks = block_size * direct_blocks
print(f"Max file size without indirect blocks: {block_size} * {direct_blocks} = {bytes_in_direct_blocks} bytes")

# Number of bytes in a single indirect block
bytes_in_single_indirect_block = numbers_in_block * block_size + bytes_in_direct_blocks
print(f"Max file size in single indirect block: {numbers_in_block} * {block_size} + {bytes_in_direct_blocks} = {bytes_in_single_indirect_block} bytes")

# Number of bytes in a double indirect block
bytes_in_double_indirect_block = numbers_in_block * numbers_in_block * block_size + bytes_in_single_indirect_block
print(f"Max file size in double indirect block: {numbers_in_block} * {numbers_in_block} * {block_size} + {bytes_in_single_indirect_block} = {bytes_in_double_indirect_block} bytes")

# Number of bytes in a triple indirect block
bytes_in_triple_indirect_block = numbers_in_block * numbers_in_block * numbers_in_block * block_size + bytes_in_double_indirect_block
print(f"Max file size in triple indirect block: {numbers_in_block} * {numbers_in_block} * {numbers_in_block} * {block_size} + {bytes_in_double_indirect_block} = {bytes_in_triple_indirect_block} bytes")
