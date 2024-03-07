from http import HTTPStatus
import dashscope
import json
import gradio as gr
from utils.Sentiment_Analysis import Sentiment_Analyse

def response(input, model_name):
    response = Sentiment_Analyse(input, model_name)
    return response.output.choices[0].message.content

if __name__  == "__main__":

    model_name = "qwen_max"
    input = "假设你是一个具有情感分析能力的AI助手，你的用户收到了一个消息，但他们不确定消息中的情感表达。你的任务是帮助用户理解消息中的情感。请对接下来的文本进行情感分析，并请严格按照以下格式回答：'情感：{情感类型}，信心水平：{百分比}'。待分析的文本是："

    demo = gr.Interface(
        fn = response,
        inputs=["text", "text"],
        outputs=["text"],
        title = "Sentiment Analysis",
        description = "This is a demo for sentiment analysis.",
        allow_flagging = False
    )

    demo.launch()