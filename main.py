# チェック処理(1行もしくは1列、はすかいのデータとN個の単語を受け取ってビンゴかチェックする)
def check_bingo_for_one_line(one_line_data, words):
    for word in one_line_data:
        if word not in words:
            return False
        # ビンゴになっている
        return True


# 入力されるビンゴカードのサイズを取得(S)
matrix_size = int(input())

# 2次元の配列を作成
card = []
for _ in range(matrix_size):
    one_row_data = input().split(' ')
    card.append(one_row_data)

# 入力される単語数を取得(N)
number_of_words = int(input())

# 入力された単語を保持する配列を作成
words = []
for _ in range(number_of_words):
    words.append(input())

# 単語数(N)がサイズ(S)より小さい場合
if number_of_words < matrix_size:
    print("no")
    exit()

# 行ごとにデータを抽出してチェックする
for one_row_data in card:
    if check_bingo_for_one_line(one_row_data, words):
        print("yes")
        exit()

# 列ごとにデータを抽出してチェックする
for column_index in range(matrix_size):
    one_column_data = []
    for row_index in range(matrix_size):
        one_column_data.append(card[row_index][column_index])

    if check_bingo_for_one_line(one_column_data, words):
        print("yes")
        exit()

# はすかいのデータをチェックする
# 左上から右下データ
top_left_to_bottom_right_data = []
# 右上から左下データ
top_right_to_bottom_left_data = []
for i in range(matrix_size):
    top_left_to_bottom_right_data.append(card[i][i])
    top_right_to_bottom_left_data.append(card[i][matrix_size - 1 - i])
    if check_bingo_for_one_line(top_left_to_bottom_right_data, words):
        print("yes")
        exit()
    if check_bingo_for_one_line(top_right_to_bottom_left_data, words):
        print("yes")
        exit()


print("no")
exit()
