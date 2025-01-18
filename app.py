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

        # Embed the n8n chat widget using HTML and JS in fullscreen mode
        chatbot_html = f"""
        <link href="https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css" rel="stylesheet" />
        <script type="module">
            import {{ createChat }} from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';
            createChat({{
                webhookUrl: '{webhook_url}',
                mode: 'fullscreen',  // Set to fullscreen mode
                chatInputKey: 'chatInput',
                chatSessionKey: 'sessionId',
                initialMessages: [
                    'Hi there! 👋', 
                    'My name is Nathan. How can I assist you today?'
                ],
                showWelcomeScreen: true,
            }});
        </script>
        <div id="n8n-chat" style="width: 100%; height: 100%;"></div>  // Ensure full screen
        """
        # Display the chatbot in the Streamlit app using HTML component
        components.html(chatbot_html, height=800)  # Adjust height for fullscreen experience
    else:
        st.warning("Please enter a valid Webhook URL in the sidebar to start chatting.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
