def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    total_words = word_count(file_contents)
    
    char_counts = character_count(file_contents)
            
    char_count_list = [{"character": char, "num": count} for char, count in char_counts.items()]
    char_count_list.sort(reverse=True, key=sort_on)

    print("---Begin report of books/frankenstein.txt---")
    print(f"{total_words} words found in document\n")

    for item in char_count_list:
        if item['character'].isalpha():
            print(f"The '{item['character']}' character was found {item['num']} times")

    print("---End report---")

def word_count(frankenstein):
    words = frankenstein.split()
    count = len(words)
    return count

def character_count(frankenstein):
    char_count_dict = {}
    for character in frankenstein:
        character = character.lower()
        if character in char_count_dict:
            char_count_dict[character] += 1
        else:
            char_count_dict[character] = 1
    return char_count_dict

def sort_on(char_count_dict):
    return char_count_dict["num"]  
    

if __name__ == "__main__":
    main() 