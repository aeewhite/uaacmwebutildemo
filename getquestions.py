import typeform
from static import API_KEY, FORM_ID

form = typeform.Form(api_key=API_KEY(), form_id=FORM_ID())

responses = form.get_responses(limit=100, since=1487863154)

for answer in responses[0].answers:
    print(answer.question_id)