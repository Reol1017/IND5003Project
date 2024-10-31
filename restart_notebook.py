import papermill as pm
import time

# 设置原 Notebook 的文件名
notebook_path = 'incremental training.ipynb'

# 尝试运行 Notebook
max_retries = 10  # 设置最大重试次数
for attempt in range(max_retries):
    try:
        print(f"运行尝试 {attempt + 1}...")
        # 使用相同的文件名运行并覆盖原 Notebook
        pm.execute_notebook(notebook_path, notebook_path)
        print("Notebook 运行成功!")
        break
    except Exception as e:
        print(f"遇到错误: {e}")
        print("重新启动 Notebook...")
        time.sleep(5)  # 等待 5 秒后再尝试重新运行
else:
    print("达到最大重试次数，Notebook 未能成功完成。")
