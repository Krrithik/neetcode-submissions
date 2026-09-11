class Solution:
    def encode(self, strs: List[str]) -> str:
        # Edge case: Handle a completely empty list
        if not strs:
            return "EMPTY_LIST"
            
        encode_chunks = []
        for s in strs:
            word_encoded = ""
            for char in s:
                # Convert EVERY character (including hyphens) to its ASCII number + "."
                word_encoded += f"{ord(char)}."
            encode_chunks.append(word_encoded)
            
        # Join words using a double hyphen "--" so it never collides with individual characters
        return "--".join(encode_chunks)

    def decode(self, s: str) -> List[str]:
        # Edge case: Handle a completely empty list
        if s == "EMPTY_LIST":
            return []
            
        final_list = []
        
        # Split by our clear word boundary "--"
        # If an element was an empty string, it splits cleanly as an empty chunk
        encoded_words = s.split("--")
        
        for encoded_word in encoded_words:
            if not encoded_word:
                final_list.append("")
                continue
                
            word = ""
            decoded_char = ""
            for char in encoded_word:
                if char == ".":
                    word += chr(int(decoded_char))
                    decoded_char = ""
                    continue
                decoded_char += char
                
            final_list.append(word)
            
        return final_list
