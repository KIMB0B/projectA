import openai
import config

openai.api_key = config.open_ai_api_key


def getResponse(message):
    print("입력한 요청 : ", message)

    # max_tokens 답변을 받을 수 있는 길이 (낮은 수로 설정해둔다면 말하다 끊김)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )

    generated_text = response.choices[0].message.content
    return generated_text
