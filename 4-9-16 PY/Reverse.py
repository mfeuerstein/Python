# Defines a function to reverse the elements in a list.
# O(n) complexity

def reverse(lyst):
    left = 0
    right = len(lyst) - 1
    while left < right:
        swap(lyst, left, right)
        left += 1
        right -= 1

def swap(lyst, x, y):
    lyst[x], lyst[y] = lyst[y], lyst[x]

def main():
    lyst = list(range(4))
    reverse(lyst)
    print(lyst)
    lyst = list(range(3))
    reverse(lyst)
    print(lyst)

if __name__ == "__main__":
    main()
    
