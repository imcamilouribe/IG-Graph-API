import pandas as pd
from openpyxl import load_workbook
from classes.defines import getCreds, makeApiCall

class Get_user:

    def __init__(self, user: str) -> None:
        self.user = user.strip()
        pass 
    
    def getAccountInfo(self):

        params = getCreds()
        fields = '{username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}'

        endpointParams = dict() # parameter to send to the endpoint
        endpointParams['fields'] = 'business_discovery.username(' + self.user + ')' + fields # string of fields to get back with the request for the account
        endpointParams['access_token'] = params['access_token'] # access token

        url = params['endpoint_base'] + params['instagram_account_id'] # endpoint url

        return makeApiCall( url, endpointParams, params['debug'] ) # make the api call
    
    def displayData(self):

        params = getCreds() # get creds
        params['debug'] = 'no' # set debug
        response = self.getAccountInfo() # hit the api for some data!

        array = []
        array.append(response['json_data']['business_discovery'])

        df = pd.DataFrame(array, columns=['followers_count','follows_count','media_count','profile_picture_url','username','name','biography','id'])

        writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
        # try to open an existing workbook
        writer.book = load_workbook('data.xlsx')
        # copy existing sheets
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        # read existing file
        reader = pd.read_excel(r'data.xlsx', engine='openpyxl')
        # write out the new sheet
        df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)

        writer.close()

        print( "\n User scrappeado \n" )