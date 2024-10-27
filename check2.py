import os

def get_all_files():
    # 確保資料夾存在
    if not os.path.exists('./img_bak'):
        print("Error: './img_bak' 資料夾不存在")
        return []
    
    try:
        # 獲取所有檔案並排序
        files = os.listdir('./img_bak')
        return sorted(files)
    except Exception as e:
        print(f"Error: 讀取資料夾時發生錯誤: {e}")
        return []

def check_missing_numbers():
    files = get_all_files()
    if not files:
        return
    
    # 儲存遺漏的編號
    missing_numbers = []
    
    try:
        # 取得所有檔案編號並排序
        numbers = []
        for filename in files:
            # 假設檔案格式為 "xxxxxx0000000000000{number}.xxx"
            parts = filename.split('0000000000000')
            if len(parts) >= 2:
                num = int(parts[1].split('.')[0])
                numbers.append(num)
        
        numbers.sort()
        
        # 檢查編號是否連續
        expected = numbers[0]  # 從第一個編號開始檢查
        for num in numbers:
            while expected < num:
                missing_numbers.append(expected)
                expected += 1
            expected = num + 1
        
        # 輸出結果
        if missing_numbers:
            print("發現遺漏的編號:")
            for num in missing_numbers:
                print(f"遺漏編號: {num}")
        else:
            print("所有編號都是連續的")
            
    except Exception as e:
        print(f"Error: 處理檔案時發生錯誤: {e}")

    print("檢查完成")

# 執行程式
if __name__ == "__main__":
    check_missing_numbers()