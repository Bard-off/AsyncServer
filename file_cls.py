import aiofiles as aof
import json

class Files:
    def __init__(self):pass
    async def exist_checker_cur(self, file_name, cur):
        async with aof.open(file_name) as f:
            data = json.loads(await f.read())
            if cur in data:
                return True
        return False

    async def checker_to_cur_exist(self, file_name: str, date, cur):
        async with aof.open(file_name, "r") as f:
            data = json.loads(await f.read())
            try:
                for el in data["data"][date]:
                    if cur in el:
                        return el
            except KeyError:
                pass
        return False

    async def write_to_file(self, file_name, json_data, date):
        async with aof.open(file_name, "r+") as f:
            data = json.loads(await f.read())
            try:
                data["data"][date].append(json_data)
            except KeyError:
                data["data"][date] = list()
                data["data"][date].append(json_data)
            await f.seek(0)
            await f.write(json.dumps(data))
            await f.truncate()
    async def del_data(self, file_name):
        async with aof.open(file_name, "w") as f:
            data = {"data": {}}
            await f.write(json.dumps(data))
            await f.truncate()

file = Files()