class TrieNode:
    """Classe que representa um nó na Trie"""

    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False


class Trie:
    """Classe que representa a Trie"""

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
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def list_words(self):

        def _dfs(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)

        words = []
        _dfs(self.root, "", words)
        return words


if __name__ == "__main__":
    palavras = [
        "gato",
        "cachorro",
        "papagaio",
        "morcego",
        "avestruz",
        "cavalo",
        "tartaruga",
        "peixe",
        "boi",
        "aranha",
    ]

    trie = Trie()

    for palavra in palavras:
        print(f"Inserida a palavra {palavra} na Trie!")
        trie.insert(palavra)
    print()

    termo_de_busca = "cavalo"
    resultado = trie.search(termo_de_busca)
    if resultado:
        print(f"O termo de busca '{termo_de_busca}' foi encontrado!")
    else:
        print(f"O termo de busca '{termo_de_busca}' NÃO foi encontrado!")

    termo_de_busca = "pássaro"
    resultado = trie.search(termo_de_busca)
    if resultado:
        print(f"O termo de busca '{termo_de_busca}' foi encontrado!")
    else:
        print(f"O termo de busca '{termo_de_busca}' NÃO foi encontrado!")
