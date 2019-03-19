import re


class Jobs:

    @staticmethod
    def get_jobs(html):
        date_pub, location, title, temp_list = [],[],[],[]

        for i in html.select('li a div span'):
            match = re.search('itemTitle', str(i))
            if match:
                title.append(i.text)

        for i in html.select('li a div div span span'):
            date_pub.append(i.text)

        for i in html.select('li a div div span'):
            temp_list.append(i.text)

        temp_set = set(date_pub)

        location = [x for x in temp_list if x not in temp_set]

        for t,d,l in zip(title, date_pub, location):
            print('Job Title: ' + t)
            print('Job Location: ' + l)
            print('Pub Date: ' + d)
            print('______________________')
