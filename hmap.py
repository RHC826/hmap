"""
    ハッシュマップを実装してみる
        - 最初ソラで一気に実装しようとしたが、出来そうにないので取り合えず連想配列を実装して調べながら改造する。
        - Python には dict がビルトインされているので、このプログラムには真っ二つの巻き藁の価値しかない。
        - ハッシュマップはクラスで実装する。
"""
from typing import Optional, Union


class ProtoHashMap:
    """
    たたき台。
        value を投げ込むリストに key と添え字の対照表リストの二つを持ち、
        key から添え字に変換することで無味乾燥な連番の記憶から解放される。
    問題
        - ハッシュマップではない。
        - 探索の際、リストを線形に舐めているので非効率的。
        - 特に工夫もなくリストに放り込んでいるので、メモリをふんだんに使用する。
        - key が重複できない。value がそれぞれ異なるとき最後の value が返る
    """

    def __init__(self):
        self.tables: list = []
        self.values: list = []

    def __str__(self):
        return str(
            [f"{self.tables[i]}:{self.values[i]}" for i in range(len(self.tables))]
        )

    def _search(self, key: str) -> Optional[int]:
        """
        key を添え字に変換する
        """
        index: Optional[int] = None
        for table in iter(self.tables):
            if key is table[0]:
                index = int(table[1])

        assert (
            len([int(table[1]) for table in iter(self.tables) if key is table[0]]) == 1
        ), "同じ key が複数あります。"

        return index

    def store(self, key="", value="") -> None:
        """
        key を添え字にして value を格納する。
        values: value
        tables: (key, 添え字の番号)
        """
        self.values.append(value)
        index = len(self.values) - 1
        self.tables.append((key, index))

        assert (
            len([int(table[1]) for table in iter(self.tables) if key is table[0]]) == 1
        ), "同じ key が複数あります。"

    def load(self, key: str) -> Union[str, bool]:
        """
        key を入力すると value が返る
        """
        index = self._search(key)

        if index is not None:
            return self.values[index]

        return False


def yama_kawa_test() -> bool:
    """
    「山！」に対して「川！」と返すテスト
    """
    hmp = ProtoHashMap()
    hmp.store("yama", "kawa")
    hmp.store("きのこ", "たけのこ")
    hmp.store("foo", "bar")

    assert hmp.load("yama") == "kawa", "「川！」が帰っていません"

    print("「山！」に対して「川！」と返すテスト: yama")
    print(hmp.load("yama"))
    print(hmp.load("きのこ"))
    print(hmp)

    return True


if __name__ == "__main__":
    yama_kawa_test()
