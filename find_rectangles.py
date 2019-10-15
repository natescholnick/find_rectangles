def find_rectangle(arr):
    '''
    Takes in an array of 0's and 1's. 1's are grouped in rectangles and rectangles are separated by 0's. It will return info on the upper-leftmost rectangle.
    function(array) returns [[index of upper left corner], width, height]
    '''

    # Declare a few trackers to be used throughout the code
    corner_found = False
    scanning_x = True
    scanning_y = True
    upper_left = [len(arr), len(arr[0])]

    # Begin iterating through the array: i rows outer, j columns inner
    for i in range(len(arr)):
        for j in range(len(arr[i])):

            # Find the upper left corner of the rectangle
            if corner_found==False and arr[i][j]==1:
                upper_left = [i,j]
                corner_found = True
                width = 0
                height = 0

            # Iterate through the rest of the row from upper_left index rightward
            for x in range(upper_left[1], len(arr[i])):

                # Only inspecting the top row of the rectangle, count its width
                if i==upper_left[0] and arr[i][x]==1 and scanning_x:
                    width += 1
                if x == len(arr[i])-1:
                    scanning_x = False
                    break
                if arr[i][x+1]==0:
                    scanning_x = False

        # Iterate through the rest of the column from upper_left downward
        for y in range(upper_left[0], len(arr)):

            # Only inspecting the leftmost column of the rectangle, count its height
            if arr[y][upper_left[1]]==1 and scanning_y:
                height +=1
                if y == len(arr)-1:
                    scanning_y = False
                    break
                if arr[y+1][upper_left[1]]==0:
                    scanning_y = False

    # Check if upper_left has been changed from its initialized value
    if upper_left != [len(arr), len(arr[0])]:
        return(upper_left, width, height)
    else:
        return None


def find_multiple(arr):
    output = []

    # Begin looping through the array so long as at least one entry is a 1
    while 1 in [item for sublist in arr for item in sublist]:
        start, x, y = find_rectangle(arr)
        output.append([start, x, y])

        # With a rectangle picked out and saved to output, erase it (1s to 0s)
        for i in range(start[0], start[0]+y):
            for j in range(start[1], start[1]+x):
                arr[i][j] = 0

    if output == []:
        return None
    return output


# find_multiple([[1, 0, 0, 0, 1, 1],
#               [0, 1, 0, 0, 1, 1]])
#     returns [[[0,0], 1, 1]
#               [[0,4], 2, 2]
#               [[1,1], 1, 1]]
