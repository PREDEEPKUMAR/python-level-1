import re


class House:

    @staticmethod
    def get_details(html):
        rent, details, title, location, pub_date, temp_list = [], [], [], [], [], []

        for i in html.select('li a div span'):
            price_match = re.search('itemPrice', str(i))
            details_match = re.search('itemDetails', str(i))
            title_match = re.search('itemTitle', str(i))
            if price_match:
                rent.append(i.text)
            elif details_match:
                details.append(i.text)
            elif title_match:
                title.append(i.text)

        for i in html.select('li a div div span span'):
            pub_date.append(i.text)

        for i in html.select('li a div div span'):
            temp_list.append(i.text)

        temp_set = set(pub_date)

        location = [x for x in temp_list if x not in temp_set]

        for t,d,r,de,l in zip(title, pub_date, rent, details, location):
            print('Title: ', t)
            print('Location: ', l)
            print('Rent: ', r)
            print('Details: ', de)
            print('Pub Date: ', d)
            print('______________________')

