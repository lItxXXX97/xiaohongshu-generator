from prompt_template import system_template_text,user_template_text
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from xiaohongshu_model import Xiaohonhshu
import os
os.environ["OPENAI_BASE_URL"] = "https://api.aigc369.com/v1"
def generate_xiaohongshu(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",system_template_text),
            ("user",user_template_text)
        ]
    )
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key= openai_api_key)
    output_parser = PydanticOutputParser(pydantic_object=Xiaohonhshu)
    chain = prompt | model| output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result
# print(generate_xiaohongshu("大模型",os.getenv("OPENAI_AIP_KEY")))