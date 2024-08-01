from dotenv import load_dotenv
#from langchain.chat_models import ChatOpenAI
#from langchain_openai import OpenAI
from langchain_aws import ChatBedrock
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
import boto3

#load_dotenv()
bedrock_runtime = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
)

client = ChatBedrock(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs=dict(temperature=0.9),streaming = True
)

memory = ConversationBufferWindowMemory(k=3, memory_key="chat_history")

def LangChain_generate(input):
  memory.chat_memory.add_user_message(input)

  template = """Your name is Rohmat ai, you are a chatbot assistant who is very good at programming, 
              you can explain complex concepts into simpler versions. 
              Your specialty is as a coding assistant but not limited to other fields. You have a fun personality,
              and usually introduced yourself
              Previous conversation: {chat_history}
              New human input: {input} 
              Response:"""
  prompt = PromptTemplate.from_template(template)

  conversation = LLMChain(
    llm=client,
    prompt=prompt,
    verbose=True,
    memory=memory
  )
  response = conversation.run(input)
  memory.chat_memory.add_ai_message(response)
  return response
