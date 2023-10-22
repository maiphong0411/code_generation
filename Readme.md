
Hướng dẫn cài đặt project (BLOOM + LoRA)

1. Cài đặt các packages liên quan
```
pip install -r requirements.txt
```
2. Fine-tune mô hình BLOOM
    - Bộ dữ liệu đã được chuẩn bị sẵn ở trên google drive
    
    Chạy thử với dữ liệu test (chưa đẩy file demo lên)
    ```
    DEBUG=true torchrun --standalone --nproc_per_node=2 train.py
    ```
    Chạy với bộ dữ liệu trên google drive
   ```
    torchrun --standalone --nproc_per_node=2 train.py
    ```
** Việc huấn luyện trên 2 GPU T4 nên cần phải có tham số nproc_per_node

Sử dụng codeBLUE 

```
CodeXGLUE/Code-Code/code-to-code-trans/evaluator/CodeBLEU/
```

Chạy codeBLEU, hiện tại đã cập nhật backbone cho python nhưng không work với semantics

```
python calc_code_bleu.py --refs reference_files --hyp candidate_file --lang java ( or c_sharp) --params 0.25,0.25,0.25,0.25(default)
```