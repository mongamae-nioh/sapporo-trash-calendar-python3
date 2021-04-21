correspondence_table = {
    # 燃やせるゴミ
    "燃やせる": 1,
    "燃える": 1,
    "燃やせるゴミ": 1,
    "燃えるゴミ": 1,
    "可燃物": 1,
    "可燃": 1,
    "燃やせるごみ": 1,
    "燃えるごみ":1,
    # 燃やせないゴミ,乾電池、ライター
    "燃やせない": 2,
    "燃えない": 2,
    "燃やせないゴミ": 2,
    "燃えないゴミ": 2,
    "不燃物": 2,
    "不燃": 2,
    "電池": 2,
    "乾電池": 2,
    "ライター": 2,
    "燃やせないごみ": 2,
    "燃えないごみ": 2,
    # プラ
    "プラ": 3,
    "プラ容器": 3,
    "プラスチック": 3,
    "プラスティック": 3,
    "プラゴミ": 3,
    "発泡スチロール": 3,
    "発泡": 3,
    # ビン、カン、ペット
    "ペット": 4,
    "ペットボトル": 4,
    "びん": 4,
    "缶": 4,
    "空き缶": 4,
    "スチール缶": 4,
    "アルミ缶": 4,
    # 雑がみ
    "雑がみ": 5,
    "紙": 5,
    "包装紙": 5,
    "模造紙": 5,
    "レシート": 5,
    "箱": 5,
    # 枝、葉、草
    "枝": 6,
    "葉っぱ": 6,
    "葉": 6,
    "草": 6,
    "雑草": 6,
    "枝葉": 6
}

def numbercheck(trashname) -> str:
    return correspondence_table[trashname]
