import gradio as gr
from utils import generate_response, set_user_response
from utils import get_context_from_pdf

# Custom CSS
custom_css = """
#chatbot {
    min-height: 400px;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}
.upload-area {
    border: 2px dashed #ccc !important;
    border-radius: 12px !important;
    padding: 20px !important;
}
.send-button {
    margin-top: 10px !important;
}
"""

def handle_input(message, chatbot, pdf_path):
    if pdf_path:
        get_context_from_pdf(pdf_path)
    return set_user_response(message, chatbot)

with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="font-weight: 600;">📄 PDF Chat Assistant</h1>
        <p style="color: #666;">Upload PDF and ask questions about the document</p>
    </div>
    """)
    
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                elem_id="chatbot",
                label="Conversation",
                avatar_images=(None, None)  # Có thể thêm avatar sau
            )
            
            with gr.Row():
                msg = gr.Textbox(
                    label="Message",
                    placeholder="Type your question about the PDF document...",
                    lines=3,
                    max_lines=5,
                    container=False,
                    scale=5
                )
                submit_btn = gr.Button("Send", variant="primary", scale=1, min_width=100, elem_classes="send-button")
                
        with gr.Column(scale=1):
            gr.Markdown("### PDF Document")
            pdf_input = gr.File(
                label=" ",
                type="filepath",
                file_types=[".pdf"],
                elem_classes="upload-area"
            )
    
    submit_event = msg.submit(
        fn=handle_input,
        inputs=[msg, chatbot, pdf_input],
        outputs=[msg, chatbot],
        queue=False
    ).then(
        fn=generate_response,
        inputs=chatbot,
        outputs=chatbot
    )
    
    submit_btn.click(
        fn=handle_input,
        inputs=[msg, chatbot, pdf_input],
        outputs=[msg, chatbot],
        queue=False
    ).then(
        fn=generate_response,
        inputs=chatbot,
        outputs=chatbot
    )

if __name__ == '__main__':
    demo.launch()