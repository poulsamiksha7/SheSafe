from decouple import config
from google import genai

client=genai.Client(api_key=config('GEMINI_API_KEY'))

reports_text="""
-Street Lighting(rating2/5):Very dark after 9PM near main road, no streetlights near bus stop
-Public Transport (rating 4/5): Autos and cabs easily available till midnight near EON IT Park
"""

prompt=f"""You are summarizing crowdsourced women's safety reports for one area
Based on these reports, write a 3-line safety summary covering lighting, transport, and general safety advice for someone visiting at night

Reports:
{reports_text}
"""

response=client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt
)
print(response.text)
