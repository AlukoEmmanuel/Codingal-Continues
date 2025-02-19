
with open("FA1.txt", "w") as fo:
    fo.write("Hello World!\n")
    fo.write("This is a demonstration file.\n")
    fo.write("Python file operations are fun!\n")
    fo.write("Count the vowels: A, E, I, O, U.\n")


print("\n=== Full Content of f1.txt ===")
with open("FA1.txt", "r") as fo:
    print(fo.read())


print("\n=== First 5 Characters of f1.txt ===")
with open("FA1.txt", "r") as fo:
    print(fo.read(5))


vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0
with open("FA1.txt", "r") as fo:
    content = fo.read().lower()  # Read and convert to lowercase
    for char in content:
        if char in vowels:
            count += 1
print("\n=== Vowel Count ===")
print(f"Total vowels: {count}")


with open("f2.txt", "w") as fo:
    fo.write("Initial Line 1\n")
    fo.write("Initial Line 2\n")


with open("f2.txt", "a") as fo:
    fo.write("Appended Line 3\n")
    fo.write("Appended Line 4\n")


print("\n=== Final Content of f2.txt ===")
with open("f2.txt", "r") as fo:
    print(fo.read())