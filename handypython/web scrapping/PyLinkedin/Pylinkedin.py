import requests

headers = {"user-agent": "your_user_agent",  } # Enter the data

company_id= 0 #Enter your target_company_id
company_link = 'https://www.linkedin.com/voyager/api/entities/companies/' + company_id

with requests.session() as s:
    s.cookies['li_at'] = "your_li_at_cookie" # Enter the data
    s.cookies["JSESSIONID"] = "your JSESSIONID" # Enter the data
    s.headers = headers
    s.headers["csrf-token"] = s.cookies["JSESSIONID"].strip('"')
    response = s.get(company_link)
    response_dict = response.json()
    print(response_dict)
