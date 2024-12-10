# LAB2 - Parameter Efficient Fine-Tuning (PEFT) of a Large Language Model on a GPU  
## ID2223 KTH - Group 0  
> Ísak Arnar Kolbeins and Esha Bilal  

### LLM Trained  
[Llama-3.2 1B](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct)  

### Dataset  
[FineTome-100k](https://huggingface.co/datasets/mlabonne/FineTome-100k)  

### Training  
Training was conducted on Colab over multiple sessions, and Google Drive used to save checkpoints along the way.  

- The model was saved as LoRA adapters on Huggingface: [LoRA Model](https://huggingface.co/kolbeins/lora_model)  
- The model was then converted to GGUF format and also saved on Huggingface: [GGUF Model](https://huggingface.co/kolbeins/model)  

### LLM Interface  
The interface uses the [Gradio chatbot demo](https://huggingface.co/spaces/gradio-templates/chatbot) provided on Huggingface.
Small changes made to toogle enable/disable the use of chat history for the next response.  
