from inference import generate_inference

def create_instruction(text):
    pass


model_path = 'bigscience/bloom-1b7' 
lora_weights_path = "/home/ubuntu/Documents/LoRA/LoRA/week6/distributed/assignment2/checkpoint"# TODO fill folder path
instruction = "Câu dưới đây về khía cạnh pin là tích cực đúng không ?" # TODO  fill instruction
user_inp = 'Nâng cấp nên phiên bản mới pin sụt nhanh .nghĩ mà chán....' # TODO  fill input 

generate_inference(instruction=instruction, user_inp=user_inp, model_path=model_path, lora_weights_path=lora_weights_path)