# ハングマン

def hangman(word):
    # 間違えた回数
    wrong = 0
    # 間違る毎に出す絵
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    # wordの文字を1文字ずつの要素に分解してリストに。残りの文字数。
    rletters = list(word)
    # スコアボード。初期状態は["_", "_", "_"]
    board = ["_"] * len(word)
    #初期状態はFalse
    win = False
    print("ハングマンへようこそ！")
    
    # 変数wrongの値がlen(stages)-1よりも小さい間繰り返す。つまりリストwrongの要素数と同じ回数を間違えたらループを終了する。
    while wrong < len(stages) - 1:
        #見た目を良くするための空行
        print("\n")
        msg = "1文字を予想してね："
        char = input(msg)
        # 正解
        if char in rletters:
            # 何番目にあるかのインデックスを取得
            cind = rletters.index(char)
            # アンダースコアを正しい文字に置き換え
            board[cind] = char
            # 複数文字対策。$に置き換え。
            rletters[cind] = '$'
        # 不正解
        else:
            wrong += 1
        # スコアボードを表示
        print(" ".join(board))
        # ハングマンの表示
        # 終了インデックスはwrongの数に1を足した値
        e = wrong + 1
        print("\n".join(stages[0:e]))
        
        # 勝利判定
        # アンダースコアがなければ処理を実行
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            # winをTrueに割り当ててループを終了
            win = True
            break
            
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))
        
hangman("cat")