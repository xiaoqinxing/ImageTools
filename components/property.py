from os.path import exists
import pickle

CACHE_PERSIST_PATH = './config/property.tmp'

# 参数表
IS_NEED_AUTO_UPDATE = 0


def load_persist():
    ret = {}
    if exists(CACHE_PERSIST_PATH):
        with open(CACHE_PERSIST_PATH, "rb") as fp:
            ret = pickle.load(fp)
    return ret


def dump_persist(value):
    with open(CACHE_PERSIST_PATH, "wb") as fp:
        pickle.dump(value, fp)


def get_persist(key, default_value):
    p = load_persist()
    if key in p:
        return p[key]
    else:
        return default_value


def set_persist(key, value):
    p = load_persist()
    p[key] = value
    dump_persist(p)
