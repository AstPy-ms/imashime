"""課題1"""
# グラフ描画，ベクトル計算の例を応用し，星型を描いてください．
# この課題ができれば及第点です．ただし，必ずクラスを使ってください．

import numpy as np
import matplotlib.pyplot as plt

class star:
    
    def __init__(self, x, y):
        
        pi = np.pi

        # Aの座標を計算
        # Aは内側で,x_a, y_a
        self.x_a = np.cos(3/10*pi) + x
        self.y_a = np.sin(3/10*pi) + y
        
        # Aの座標からBの座標を出す
        # Bは外側で,x_b,y_b
        self.x_b = 2*np.sin(19/60*pi)*np.cos(pi/10)
        self.y_b = 2*np.sin(19/60*pi)*np.sin(pi/10)
        
        # print(self.x_a,self.y_a, self.x_b, self.y_b)
        
    def rotation(self, x, y, theta):
    
      # x, yは回転させたい点の座標

        """
        これを表現
        | cos -sin |
        | sin  cos | 
        """
        
        a = np.cos(theta)
        b = -1 * np.sin(theta)
        c = np.sin(theta)
        d = np.cos(theta)

        return a*x + b*y, c*x + d*y


if __name__ == "__main__":

    test = star(0, 0) # 原点の座標をいれ__init__でbの座標を吐く
    
    # Aの座標を追加
    x_in = [test.x_a]
    y_in = [test.y_a]

    # Bの座標を追加
    x_out = [test.x_b]
    y_out = [test.y_b]

    # 外側の点をメリーゴーランド
    for i in range(5):
        x_tmp, y_tmp = test.rotation(x_out[i], y_out[i], 0.4*np.pi)
        x_out.append(x_tmp)
        y_out.append(y_tmp)

    # 内側の点をメリーゴーランド
    for i in range(5):
        x_tmp, y_tmp = test.rotation(x_in[i], y_in[i], 0.4*np.pi)
        x_in.append(x_tmp)
        y_in.append(y_tmp)

    # 外側と内側の点の座標をひとつの配列に格納する
    x = []
    y = []

    for i in range(5):
        x.append(x_out[i])
        x.append(x_in[i])
        y.append(y_out[i])
        y.append(y_in[i])

    # 始点と終点を結ぶために始点の座標を最後に追加
    x.append(x_out[0])
    y.append(y_out[0])

    fig = plt.figure()  # 画像を生成
    ax = fig.add_subplot(1, 1, 1)  # 1行1列の描画領域を宣言．
    x = np.array(x)  # 区間線形関数を描画．x 座標の列
    y = np.array(y) # 上記 x 座標に対応する y 座標の列
    ax.plot(x, y, label="star", color=(0, 0, 0, 1), linewidth=0.2, marker="o", markersize=1) # 色は黒，線の幅0.2, 標本点を丸，標本点の大きさを1に指定し描画．
    plt.legend() # 凡例を表示
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1) # 余白を小さく設定
    ax.set_aspect('equal') # アスペクト比を1に設定
    plt.show()
