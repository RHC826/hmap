"""
    ハッシュマップを実装してみる
        - 最初ソラで一気に実装しようとしたが、出来そうにないので取り合えず連想配列を実装して調べながら改造する。
        - Python には dict がビルトインされているので、このプログラムには真っ二つの巻き藁の価値しかない。
        - ハッシュマップはクラスで実装する。
"""
from typing import Union


class ProtoHashMap:
    """
    たたき台。
        value を投げ込むリストを持つハッシュマップ、
        key から添え字に変換することで無味乾燥な連番の記憶から解放される。
    問題
        - 特に工夫もなくリストに放り込んでいるので、メモリをふんだんに使用する。
    """

    def __init__(self):
        self.max: int = 150
        self.values: list = [None] * self.max

    def __str__(self):
        return str([f"{self.values[i]}" for i in range(len(self.values))])

    def _search(self, key: str) -> int:
        """
        key を添え字に変換する
        """
        index: int = hash(key) % self.max

        return index

    def store(self, key="", value="") -> None:
        """
        key を添え字にして value を格納する。
        """
        index: int = self._search(key)
        index_2 = self._search(key + "_")

        if self.values[index_2] is None and self.values[index] is None:
            print(key)
            self.values[index] = value
            return

        print(hash(key) % self.max)
        self.store(key+"_", value)

    def load(self, key: str) -> Union[str, bool]:
        """
        key を入力すると value が返る
        """
        index = self._search(key)
        index_2 = self._search(key + "_")

        if self.values[index_2] is None:
            return self.values[index]

        self.load(key + "_")
        #return False


def yama_kawa_test() -> bool:
    """
    「山！」に対して「川！」と返すテスト
    """
    import random

    hmp = ProtoHashMap()
    hmp.store("yama", "kawa")
    hmp.store("きのこ", "たけのこ")
    hmp.store("foo", "bar")
    hmp.store(f"str({random.random()})", f"piyo:str({random.random()})")
    print(hmp)
    print(hmp.load("yama"))

    assert hmp.load("yama") == "kawa", "「川！」が帰っていません"

    print("「山！」に対して「川！」と返すテスト: yama")
    print(hmp.load("yama"))
    print(hmp.load("きのこ"))

    return True


if __name__ == "__main__":
    yama_kawa_test()
