import json
import cv2
import numpy as np
import os
import sys
from pathlib import Path


# JSONLファイルのパス
jsonl_file_path = 'data.jsonl'

def main(jsonl_file_path):
    # JSONLファイルを読み込む
    with open(jsonl_file_path, 'r', encoding='utf-8') as f:
        jsonl_data = f.readlines()

    work_dir = Path(jsonl_file_path).parent
    print("work dir: {}".format(work_dir))

    # 各行を処理
    for line in jsonl_data:
        data = json.loads(line)
        ground_truth = json.loads(data['ground_truth'])
    
        file_name = os.path.join(work_dir, data['file_name'])
        bounding_boxes = ground_truth['gt_parse']['bounding_boxes']
    
        # 画像を読み込む
        image = cv2.imread(file_name)
    
        # バウンディングボックスを描画
        for box in bounding_boxes:
            # 座標を数値に変換
            points = [(int(float(coord[0])), int(float(coord[1]))) for coord in box]
            points = np.array(points, np.int32).reshape((-1, 1, 2))
        
            # ポリゴンを描画
            cv2.polylines(image, [points], isClosed=True, color=(0, 0, 255), thickness=2)
    
        # 結果を保存
        output_file_name = 'output_' + data['file_name']
        cv2.imwrite(os.path.join(work_dir,output_file_name), image)
        print(f"画像にバウンディングボックスを描画して保存しました: {output_file_name}")

if __name__=="__main__":
    args = sys.argv
    if(len(args) < 2):
        print("Need JSONL path")
        exit()
    
    main(args[1])


