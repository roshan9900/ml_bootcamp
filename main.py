from src.data_collection import datacollection

try:
    obj = datacollection()
    obj.data_collection()
    print('Stage data collection comp... suc...')
except Exception as e:
    raise e


