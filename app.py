import streamlit as st
import streamlit.components.v1 as components

# Streamlit App
def main():
    # App title
    st.title("n8n Chatbot Integration")

    # Sidebar for Webhook URL input
    st.sidebar.header("n8n Webhook Configuration")
    webhook_url = st.sidebar.text_input("Enter n8n Webhook URL:", "YOUR_PRODUCTION_WEBHOOK_URL")

    # Check if the webhook URL is provided
    if webhook_url != "YOUR_PRODUCTION_WEBHOOK_URL":
        st.subheader("Chat with Nathan 👋")

        # Embed the n8n chat widget using HTML and JS
        chatbot_html = f"""
        <link href="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css" rel="stylesheet" />
        <script type="module">
            import {{ createChat }} from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';
            createChat({{
                webhookUrl: '{webhook_url}'
            }});
        </script>
        """
        # Display the chatbot in the Streamlit app using HTML component
        components.html(chatbot_html, height=600)
    else:
        st.warning("Please enter a valid Webhook URL in the sidebar to start chatting.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
