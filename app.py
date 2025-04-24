import gradio as gr
from src.utils import generate_response, set_user_response
from src.pdf_loader import get_context_from_pdf

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

def handle_input(message, chatbot, pdf_path=None):
    context = ""
    if pdf_path:
        retriever = get_context_from_pdf(pdf_path)
        relevant_docs = retriever.get_relevant_documents(message)
        context = "\n\n".join([doc.page_content for doc in relevant_docs])

    return set_user_response(message, chatbot, context)

def clear_pdf():
    return gr.update(value=None)

with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
    context_state = gr.State(None)
    gr.Markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="font-weight: 600;">PDF Chat Assistant</h1>
        <p style="color: #666;">Upload PDF and ask questions about the document</p>
    </div>
    """)
    
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                elem_id="chatbot",
                label="Conversation",
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
                elem_classes="upload-area",
            )
    
    submit_event = msg.submit(
        fn=handle_input,
        inputs=[msg, chatbot, pdf_input],
        outputs=[msg, chatbot, context_state],
        queue=False,
        api_name=False
    ).then(
        fn=generate_response,
        inputs=[chatbot, context_state], 
        outputs=chatbot
    )
    
    submit_btn.click(
        fn=handle_input,
        inputs=[msg, chatbot, pdf_input],
        outputs=[msg, chatbot, context_state],
        queue=False,
        api_name=False
    ).then(
        fn=generate_response,
        inputs=[chatbot, context_state],  
        outputs=chatbot
    ).then(
        fn=clear_pdf,
        inputs=[],
        outputs=[pdf_input]
)
    
    print("context" , context_state)

if __name__ == '__main__':
    demo.launch(share=True)
    
    