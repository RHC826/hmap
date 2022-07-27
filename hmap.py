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
        self.values: list = [False] * 100

    def __str__(self):
        return str([f"{self.values[i]}" for i in range(len(self.values))])

    def store(self, key="", value="") -> None:
        """
        key を添え字にして value を格納する。
        """
        index: int = _search(key)
        if self.values[index] is not None:
            self.values[index] = value

        # self.store(key+"_", value)

    def load(self, key: str) -> Union[str, bool]:
        """
        key を入力すると value が返る
        """
        index = _search(key)

        if index is not None:
            return self.values[index]

        return False

def _search(key: str) -> Optional[int]:
    """
    key を添え字に変換する
    """
    index: Optional[int] = None
    index = hash(key) % 100

    return int(index)


def yama_kawa_test() -> bool:
    """
    「山！」に対して「川！」と返すテスト
    """
    hmp = ProtoHashMap()
    hmp.store("yama", "kawa")
    hmp.store("きのこ", "たけのこ")
    hmp.store("foo", "bar")
    print(hmp)

    assert hmp.load("yama") == "kawa", "「川！」が帰っていません"

    print("「山！」に対して「川！」と返すテスト: yama")
    print(hmp.load("yama"))
    print(hmp.load("きのこ"))

    return True


if __name__ == "__main__":
    yama_kawa_test()
