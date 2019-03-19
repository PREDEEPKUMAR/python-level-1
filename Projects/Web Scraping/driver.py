import transporter as t
import jobs as j
import house as h

# url = r'https://www.olx.in/puducherry_g4059067/data-entry-back-office_c1737?filter=job_type_eq_fulltime%2
# Csalary_period_eq_weekly'

url = r'https://www.olx.in/puducherry_g4059067/houses-villas-for-rent-houses-apartments_c1723?filter=bachelors_eq_yes%2' \
      r'Cfurnished_eq_yes%2Clisted_by_eq_owner%2Cprice_between_8000_to_12000%2Crooms_max_2%2Ctype_eq_houses'
raw_html = t.simple_get(url)

html = t.BeautifulSoup(raw_html, 'html.parser')
#comment
# j.Jobs.get_jobs(html)
h.House.get_details(html)
