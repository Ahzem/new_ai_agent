
import os  
import base64
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("ENDPOINT_URL", "https://myfirstazureopenaiservices.openai.azure.com/")  
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o")  
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")  

# Initialize Azure OpenAI Service client with key-based authentication    
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version="2024-05-01-preview",
)
    
    
# IMAGE_PATH = "YOUR_IMAGE_PATH"
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')

#Prepare the chat prompt 
# chat_prompt = [
#     {
#         "role": "system",
#         "content": [
#             {
#                 "type": "text",
#                 "text": "You are an AI assistant that helps people find information."
#             }
#         ]
#     },
#     {
#         "role": "user",
#         "content": [
#             {
#                 "type": "text",
#                 "text": "Create a catchy marketing slogan for a new eco-friendly product."
#             }
#         ]
#     },
#     {
#         "role": "assistant",
#         "content": [
#             {
#                 "type": "text",
#                 "text": "\"Go Green, Live Clean – Eco-Friendly Made Easy!\""
#             }
#         ]
#     }
# ] 
    
    
chat_prompt = [ 
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "You are the Gavel Club Assistant, a knowledgeable and friendly AI designed to help users with information about the Gavel Club of ITUM. Your goal is to provide details about meetings, events, membership, public speaking tips, and other club-related queries in a clear and engaging manner."
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "How can I join the Gavel Club of ITUM?"
            }
        ]
    },
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "Joining the Gavel Club of ITUM is simple! Our club welcomes students interested in improving their public speaking and leadership skills. To become a member, you can visit our website at [https://gavelndt.club/](https://gavelndt.club/) and check the membership section for registration details. If you need further assistance, feel free to ask!"
            }
        ]
    }
] 

# Include speech result if speech is enabled  
messages = chat_prompt  
    
# Generate the completion 
try:
    completion = client.chat.completions.create(  
        model=deployment,
        messages=messages,
        max_tokens=800,  
        temperature=0.7,  
        top_p=0.95,  
        frequency_penalty=0,  
        presence_penalty=0,
        stop=None,  
        stream=False
    )
    # Extract just the content from the response
    response = completion.choices[0].message.content
    print(f"\nAI Response: {response}")
except Exception as e:
    print(f"Error generating completion: {str(e)}")
    