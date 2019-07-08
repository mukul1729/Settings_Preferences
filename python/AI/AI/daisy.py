import wolframalpha
import sys
inpu= input("Question: ")
app_id="WRHEKL-PGY9TJ7G28"
client=wolframalpha.Client(app_id)

res=client.query(inpu)
answer=next(res.results).text
print(answer)
input('Press Enter to exit')

