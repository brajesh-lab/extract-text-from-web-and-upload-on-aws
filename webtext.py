import bs4,requests
from bs4 import BeautifulSoup
import boto3
class webext(object):
    output = ""
    def __init__(self):
      url = "https://ec.europa.eu/programmes/horizon2020/en/h2020-section/information-and-communication-technologies"
      res = requests.get(url)
      html_page = res.content
      soup = BeautifulSoup(html_page, 'html.parser')
      webext.text = soup.find_all(["h1", "h2", "h3","h4","h5","h6","p"])
    def store(self):
      for t in webext.text:
         if t.tag==(["h1", "h2", "h3","h4","h5","h6"]):
              print("head")
              webext.output += '{} '.format(t.text)
         else:
            webext.output += '{} '.format(t.text)
      
      return webext.output



class upload(webext):

    def __init__(self):
        txt=webext.output
        f= open("text.txt","w")
        f.write(txt)
        f.close()
        s3=boto3.client("s3")
        s3_client = boto3.client('s3')
        try:
          response = s3_client.upload_file("text.txt", "mybucket","webfile")
       except ClientError:
          print ("something went")
       

object1 = webext()
object1.store()
object2 = upload()


