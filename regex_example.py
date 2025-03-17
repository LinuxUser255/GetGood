import re

def regex_example():
    print("Regular Expression Examples\n")

    # Example 1: Matching a simple pattern
    pattern = r"python"
    text = "I love Python programming"
    match = re.search(pattern, text, re.IGNORECASE)
    print("1. Matching 'python' in a sentence:")
    if match:
        print(f"   Found: {match.group()} at position {match.start()}")
    else:
        print("   Not found")
    print()

    # Example 2: Extracting all occurrences of a pattern
    pattern = r"\d+"  # Matches one or more digits
    text = "There are 42 apples and 7 oranges"
    matches = re.findall(pattern, text)
    print("2. Extracting all numbers from a sentence:")
    print(f"   Numbers found: {matches}")
    print()

    # Example 3: Splitting a string using regex
    pattern = r"[,;\s]+"  # Matches commas, semicolons, or whitespace
    text = "apple,banana;  cherry,date; elderberry"
    split_result = re.split(pattern, text)
    print("3. Splitting a string with multiple delimiters:")
    print(f"   Split result: {split_result}")
    print()

    # Example 4: Replacing patterns in a string
    pattern = r"\b(\w+)(\s+\1\b)+"  # Matches repeated words
    text = "The the quick brown fox jumps over the lazy lazy dog"
    replaced = re.sub(pattern, r"\1", text, flags=re.IGNORECASE)
    print("4. Removing repeated words:")
    print(f"   Original: {text}")
    print(f"   Cleaned: {replaced}")
    print()

    # Example 5: Validating an email address
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    emails = ["user@example.com", "invalid.email@com", "another@valid.address.org"]
    print("5. Validating email addresses:")
    for email in emails:
        if re.match(pattern, email):
            print(f"   {email} is valid")
        else:
            print(f"   {email} is invalid")

#def main():
regex_example()

#if __name__ == "__main__":
#    main()