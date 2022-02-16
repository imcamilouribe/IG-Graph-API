from openpyxl import load_workbook
import pandas as pd
from classes.defines import getCreds, makeApiCall

class Get_posts:

    def __init__(self, user: str, fecha_ini: str, fecha_fin: str) -> None:
        self.user = user
        self.fecha_ini = fecha_ini
        self.fecha_fin = fecha_fin
        pass 
    
    def getAccountPosts(self):

        params = getCreds()
        fields = '{media.limit(9999){ username, comments_count, like_count, media_url, caption, timestamp, permalink }}'

        endpointParams = dict() # parameter to send to the endpoint
        endpointParams['fields'] = 'business_discovery.username(' + self.user + ')' + fields # string of fields to get back with the request for the account
        endpointParams['access_token'] = params['access_token'] # access token

        url = params['endpoint_base'] + params['instagram_account_id'] # endpoint url

        return makeApiCall( url, endpointParams, params['debug'] ) # make the api call
    
    def displayData(self):

        params = getCreds() # get creds
        params['debug'] = 'no' # set debug
        response = self.getAccountPosts( ) # hit the api for some data!

        array = []
        for x in range(len(response['json_data']['business_discovery']['media']['data'])):
            array.append(response['json_data']["business_discovery"]["media"]["data"][x])
    
        df = pd.DataFrame(array, columns=["username","comments_count","like_count","media_url","permalink","caption","timestamp","id"])

        if ( self.fecha_ini > self.fecha_fin ):
            filtered_df = df.loc[df["timestamp"].between( self.fecha_fin, self.fecha_ini )]
        else:
            filtered_df = df.loc[df["timestamp"].between( self.fecha_ini, self.fecha_fin )]

        filtered_df["timestamp"] = filtered_df["timestamp"].str[0:10]

        print(filtered_df)

        writer = pd.ExcelWriter('posts.xlsx', engine='openpyxl')
        # try to open an existing workbook
        writer.book = load_workbook('posts.xlsx')
        # copy existing sheets
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        # read existing file
        reader = pd.read_excel(r'posts.xlsx', engine='openpyxl')
        # write out the new sheet
        filtered_df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)
        writer.close()

        print( "\n posts scrappeados \n" )
        