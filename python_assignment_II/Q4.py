# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

def is_anagram(st1, st2):
    '''
    checks whether given two words are anagram or not
    :param st1: String
    :param st2: String
    :return: Boolean
    '''
    if len(st1) != len(st2):
        return False
    else:
        st1_list =[]
        for _ in st1:
            st1_list.append(_)

        for s in st2:
            if s in st1_list:
                st1_list.remove(s)
            else:
                return False
    return True



if __name__ == "__main__":
    arr = input('Enter a paragraph: ').split()
    # arr = ["zoo","zooo","zzo","ozo","apple", "aeplp", "pplea", "aple"] # length => 8
    anagram_words = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if is_anagram(arr[i], arr[j]):
                l = []
                l.append(arr[i])
                l.append(arr[j])
                anagram_words.append(l)

    print('Pair of anagram words found: ',anagram_words)



# if __name__ == '__main__':
#     print(is_anagram("zooo", "zoo")) # F
#     print(is_anagram("zoo", "zooo")) # F
#     print(is_anagram("zoo", "zzo")) # F
#     print(is_anagram("zoo", "ozo")) # T
#     print(is_anagram("zoo", "oZo")) # F
#     print(is_anagram("zzo", "oZo")) # F
#     print(is_anagram("zoo", "zzo")) # F
#     print(is_anagram("zzo", "zoo")) # F
#     print(is_anagram("zoo", "ooz")) # T
#     print(is_anagram("zzo", "zoz")) # T

