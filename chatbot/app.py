import gradio as gr
from huggingface_hub import InferenceClient

"""
Cloned from https://huggingface.co/spaces/gradio-templates/chatbot - and added the history toggle to the interface

For more information on `huggingface_hub` Inference API support, please check the docs: https://huggingface.co/docs/huggingface_hub/v0.22.2/en/guides/inference
"""

client = InferenceClient("kolbeins/model")


def respond(
    message,
    history: list[tuple[str, str]],
    system_message,
    use_history,
    max_tokens,
    temperature,
    top_p,
):
    messages = [{"role": "system", "content": system_message}]

    # Only use history if the toggle is on 
    if use_history == "Yes":
        for val in history:
            if val[0]:
                messages.append({"role": "user", "content": val[0]})
            if val[1]:
                messages.append({"role": "assistant", "content": val[1]})

    messages.append({"role": "user", "content": message})

    response = ""
    

    for message in client.chat_completion(
        messages,
        max_tokens=max_tokens,
        stream=True,
        temperature=temperature,
        top_p=top_p,
    ):
        token = message.choices[0].delta.content

        response += token
        yield response
    
    # Then add to history (even if the toggle is of)
    history.append((message, response))


demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Textbox(value="You are a friendly Chatbot.", label="System message"),
        gr.Radio(["Yes", "No"], value="Yes", label="Use chat history"),
        gr.Slider(minimum=1, maximum=2048, value=512, step=1, label="Max new tokens"),
        gr.Slider(minimum=0.1, maximum=4.0, value=0.7, step=0.1, label="Temperature"),
        gr.Slider(minimum=0.1, maximum=1.0, value=0.95, step=0.05, label="Top-p (nucleus sampling)", ),
    ],
)


if __name__ == "__main__":
    demo.launch()
