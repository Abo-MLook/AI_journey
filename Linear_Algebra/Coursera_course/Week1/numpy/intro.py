import numpy as np



a1 = np.array([[1,1],
               [2,2]])
a2 = np.array([[3,3],
              [4,4]])
print(f'a1:\n{a1}')
print()
print(f'a2:\n{a2}')
print()


# Stack the arrays vertically
vert_stack = np.vstack((a1, a2))
print(vert_stack)
print()

# Stack the arrays horizontally
horz_stack = np.hstack((a1, a2))
print(horz_stack)
print()

# Split the horizontally stacked array into 2 separate arrays of equal size
horz_split_two = np.hsplit(horz_stack,2)
print(horz_split_two)
print()

# Split the horizontally stacked array into 4 separate arrays of equal size
horz_split_four = np.hsplit(horz_stack,4)
print(horz_split_four)
print()

# Split the horizontally stacked array after the first column
horz_split_first = np.hsplit(horz_stack,[1])
print(horz_split_first)
print()

# Split the vertically stacked array into 2 separate arrays of equal size
vert_split_two = np.vsplit(vert_stack,2)
print(vert_split_two)
print()

# Split the horizontally stacked array into 4 separate arrays of equal size
vert_split_four = np.vsplit(vert_stack,4)
print(vert_split_four)
print()

# Split the horizontally stacked array after the first and third row
vert_split_first_third = np.vsplit(vert_stack,[1,3])
print(vert_split_first_third)