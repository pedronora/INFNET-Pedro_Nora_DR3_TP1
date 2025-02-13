class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        # Implementar aqui a função de busca
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word


if __name__ == "__main__":
    palavras = ["gato", "camelo", "elefante"]

    trie = Trie()

    for palavra in palavras:
        trie.insert(palavra)
        print(f"Inserida a palavra {palavra} na Trie!")
    print()

    palavra_buscada = "camelo"
    resultado = trie.search(palavra_buscada)
    if resultado:
        print(f"Encontrada a palavra buscada '{palavra_buscada}'!")
    else:
        print(f"NÃO encontrada a palavra buscada '{palavra_buscada}'!")

    palavra_buscada = "cachorro"
    resultado = trie.search(palavra_buscada)
    if resultado:
        print(f"Encontrada a palavra buscada '{palavra_buscada}'!")
    else:
        print(f"NÃO encontrada a palavra buscada '{palavra_buscada}'!")
