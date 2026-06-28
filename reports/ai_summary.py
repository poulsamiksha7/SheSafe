from decouple import config
from google import genai

def generate_area_summary(city_name,reports):
    if not reports:
        return "No reports available yet for this area"
    
    reports_text="\n".join([
        f"- {r.category} (rating {r.rating}/5): {r.description}"
        for r in reports
    ])
    prompt=f""" You are summarizing crowdsourced women's safety reports for {city_name}.
    Based on these reports, write a 3-line safety summary covering lighting, transport, and general safety advice for someone visiting at night.
    Reports:
    {reports_text}
    """
    try:
        client=genai.Client(api_key=config('GEMINI_API_KEY'))
        response=client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI summary unavailable right now. ({str(e)})"