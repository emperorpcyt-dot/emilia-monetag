#(©)CodeXBotz
#recoded by its_tartaglia_Childe


import pymongo, os
from config import DB_URI, DB_NAME


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]


user_data = database['users']
verify_data = database['ad_verify']



async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return



#----------------- AD VERIFICATION -----------------#
import time

async def clear_ad_started(user_id: int):
    """One ad = one unlock: forget the ad start so it can't be reused."""
    verify_data.update_one({'_id': user_id}, {'$unset': {'ad_started': ''}})

async def set_pending(user_id: int, start_arg: str):
    """Remember which file link the user opened, so we can send it after the ad."""
    verify_data.update_one({'_id': user_id}, {'$set': {'pending': start_arg}}, upsert=True)

async def pop_pending(user_id: int):
    doc = verify_data.find_one_and_update({'_id': user_id}, {'$unset': {'pending': ''}})
    return doc.get('pending') if doc else None

async def set_ad_started(user_id: int):
    verify_data.update_one({'_id': user_id}, {'$set': {'ad_started': time.time()}}, upsert=True)

async def get_ad_started(user_id: int):
    doc = verify_data.find_one({'_id': user_id})
    return doc.get('ad_started') if doc else None
